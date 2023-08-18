# def vat():
#     price_for_item = float(input("Enter the price for an item -> "))
#     vat = float(input("Enter VAT"))
#     if price_for_item <= 0 or vat <= 0:
#        print("invalid entry pls enter a valid input")

        
def your_vat():
 
  price = float(input("Enter the price of the item: "))
  vat = float(input("Enter the VAT percentage: "))

  while price <= 0 or vat <= 0:
    print("Invalid input. Please enter a positive number for both the price and VAT.")
    price = float(input("Enter the price of the item: "))
    vat = float(input("Enter the VAT percentage: "))

  vat_amount = price * vat / 100
  vat_inclusive_price = price + vat_amount

  return vat_inclusive_price


if __name__ == "__main__":
  print(your_vat())

