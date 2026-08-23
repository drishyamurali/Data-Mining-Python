import math
# Data of two customers
customer_A = [25, 45000]
customer_B = [30, 52000]
# Calculate Euclidean distance
distance = math.sqrt(
    (customer_B[0] - customer_A[0]) ** 2 +
    (customer_B[1] - customer_A[1]) ** 2
)
#Print the values of Customer A, Customer B and Euclidian distance
print("Customer A:", customer_A)
print("Customer B:", customer_B)
print("Euclidean Distance:", distance)
