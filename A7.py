transactions=[
    ["milk","bread"],
    ["milk","eggs"],
    ["milk","bread","butter"],
    ["bread","butter"],
    ["milk","bread"]
    ]
itemset=["milk","bread"]
count=0
for transaction in transactions:
    if all(item in transaction for item in itemset):
        count+=1
        support=count/len(transaction)
print("itemset:",itemset)
print("number of transactions containing itemset:",count)
print("total transactions:",len(transactions))
print("support:",support)
