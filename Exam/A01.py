#ETL process in sales data

#Extract
sales=["1500","2750","600","1900","2000"]
print("Original Sales Data:")
print(sales)

#Transform
transformed_sales=[int(value) for value in sales]

#Load
print("Transformed Sales Data:")
print(transformed_sales)