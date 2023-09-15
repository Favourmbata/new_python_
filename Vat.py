def your_vat():
    price = int(input("Enter price of an item"))
    vat = int(input("Enter value of vat"))
    price_inclusive = price + price * vat / 100
    print(price_inclusive)
