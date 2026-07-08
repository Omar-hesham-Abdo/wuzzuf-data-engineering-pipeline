from delta.tables import DeltaTable

def load(df, spark):

    spark_df = spark.createDataFrame(df)

    delta_table = DeltaTable.forName(spark, "python_jobs")

    (delta_table.alias("old")
        .merge(
            spark_df.alias("new"),
            "old.Job_URL = new.Job_URL"
        )
        .whenMatchedUpdateAll()
        .whenNotMatchedInsertAll()
        .execute())