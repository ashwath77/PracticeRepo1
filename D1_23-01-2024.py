# from pyspark import SparkSession
from pyspark.sql.types import StructType,StructField,StringType,IntegerType
from pyspark.sql.functions import lit, col

df=spark.read.format("csv").load("dbfs:/dbfs/FileStore/Country_table.csv")
df.display()

schema=StructType([
    StructField("country_code",StringType(),False),
    StructField("country_name",StringType(), False)
])

#Reading the file with schema
df=spark.read.format("csv").schema(schema).load('dbfs:/dbfs/FileStore/Country_table.csv')
df.display()

#Renaming the column
df=df.withColumnRenamed("country_code","code").withColumnRenamed("country_name","name")
df.show()

#Add the columns as company ('Diiggibyte')
df=df.withColumn("company",lit("Diiggibyte"))
df.display()

#Filter by and and or operater
df1 = df.filter((col("code") == "ny") & (col("name") == "newyork"))
df2 = df.filter((col("code") == "ny") | (col("name") == "Russia"))
df1.display()
df2.display()

#Cast the datatype
df = df.withColumn("code", col("code").cast(StringType()))
df.display()