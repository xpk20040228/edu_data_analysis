from pyspark.sql.functions import col
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType


def get_background_cluster_mappings():
    return [
        "expanding_opportunities",
        "growing_opportunities",
        "abundant_opportunities"
    ]

def get_score_cluster_mappings():
    return [
        "low_score",
        "normal_score",
        "high_score"
    ]


def label_mapping(df):
    background_labels = get_background_cluster_mappings()
    score_labels = get_score_cluster_mappings()

    background_udf = udf(lambda idx: background_labels[idx], StringType())
    score_udf = udf(lambda idx: score_labels[idx], StringType())

    df = df.withColumn("background_cluster_label", background_udf(df["background_cluster"]))
    df = df.withColumn("score_cluster_label", score_udf(df["score_cluster"]))

    return df
