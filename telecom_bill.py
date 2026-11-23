customer_name = input("Enter Customer Name: ")

bill_amount = float(input("Enter Bill Amount: "))

if bill_amount > 3000:
    discount = bill_amount * 0.10
else:
    discount = 0

final_bill = bill_amount - discount

print("Customer:", customer_name)
print("Original Bill:", bill_amount)
print("Discount:", discount)
print("Final Bill:", final_bill)