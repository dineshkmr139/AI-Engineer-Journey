try:
    name = input("Enter the Customer name :")
    bill = float(input("enter the bill amount :"))

    discount = 0
    if bill > 3000:
        bill = bill - (bill * 0.10)

    print("Your final bill is ", bill)
except ValueError:
    print("enter a valid value :")
finally:
    print("thank you for using this code program")