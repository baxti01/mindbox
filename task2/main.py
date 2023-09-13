from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('ProductCategory').getOrCreate()

product_data = [('Watch',), ('Sneakers',), ('Adidas Tango',), ('Apple',)]
product_df = spark.createDataFrame(product_data, ['Product'])

category_data = [
    ('Electronics',), ('Accessories',),
    ('Footwear',), ('Sport',), ('Clothes',)
]
category_df = spark.createDataFrame(category_data, ['Category'])

relation_data = [
    ('Watch', 'Electronics'),
    ('Watch', 'Accessories'),
    ('Sneakers', 'Footwear'),
    ('Sneakers', 'Sport'),
    ('Adidas Tango', 'Sport'),
    ('Adidas Tango', 'Clothes'),
]
relation_columns = ['Product', 'Category']
relation_df = spark.createDataFrame(relation_data, relation_columns)

full_product_df = product_df.join(relation_df, 'Product', 'left').select('Product', 'Category')
full_product_df.show()

spark.stop()
