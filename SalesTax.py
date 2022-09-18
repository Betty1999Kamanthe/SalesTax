
import math
#Ceate a dictionary of the products at the store
products = [{"id": 1,
            "name":"box of chocolates",
            "category":"Food",
            "price":10.00,
            "imported":False,
            },
            
            {"id":2,
              "name":"box of chocolates",
              "category":"Food",
              "price":11.25,
              "imported":True,
            },

            {"id":3,
            "name":"chocolates bar",
            "category":"Food",
            "price":0.85,
            "imported":False,
            },

            {"id":4,
            "name":"book",
            "category":"Book",
            "price":12.49,
            "imported":False,
            },
            
            {"id":5,
            "name":"music CD",
            "category":"Music",
            "price":14.99,
            "imported":False,
            },
            
            {"id":6,
            "name":"bottle of perfume",
            "category":"fragrence",
            "price":47.50,
            "imported":True,
            },

            {"id":7,
            "name":"bottle of perfume",
            "category":"fragrence",
            "price":18.99,
            "imported":False,
            },
            
            {"id":8,
            "name":"bottle of perfume",
            "category":"fragrence",
            "price":27.99,
            "imported":True,
            },

            {"id":9,
            "name":"headache pills",
            "category":"medicine",
            "price":9.75,
            "imported":False,
            }]

#Create a shopping basket class that users can add product to. 
class shopping_basket():
  def __init__(self):
    self.basket = [] # Empty shopping basket
  
  def add(self):
    #adding items to the basket
    enterItem = 1
    while(enterItem): #Loop whenever control variable 'enterItem' evaluates to True
      product_id = int(input("Enter the product id to add:\n"))
      quantity = int(input("Enter the quantity:\n"))
      order = (product_id, quantity)
      if(self.productExists(product_id)): #check if product id exists in the product dictionary
        self.basket.append(order)
      else:
        print("The product id you entered does not exist.")

      enterItem = int(input("Do you want to add another product?\n No - Press 0 \n Yes - Press 1\n"))

  def productExists (self, product_id): #check if product id exists in the product dictionary

    for product in products:
      if(product['id'] == product_id):
        return True

    return False

  def roundUp (self, num): # Round up to the nearest 0.05
    return math.ceil(num / 0.05) * 0.05

  def calculateSalesTax (self, price, category): #Calculate the 10% sales tax
    exemptGoods = ['Food', 'Book', 'Medicine']
    if category not in exemptGoods:
      salestax = 0.1 * price
      return self.roundUp(salestax)
    else:
      return 0

  def calculateImportTax (self, price, isImported): # Calculate import tax
    if isImported:
      importtax = 0.05 * price
      return self.roundUp(importtax)

    else:
      return 0

  def displayReceipt(self): 
    print("Input basket")
    for product in self.basket:
      product_id = product[0]
      quantity = product[1]
      for productDesc in products:
        if(productDesc['id'] == product_id):
          # Display products in the basket
          print(str(quantity) + ' ' + productDesc['name'] + ' at ' + str(productDesc['price']) + '\n')

    print("Output for Basket")
    total_tax = 0
    total_price = 0
    for product in self.basket:
      product_id = product[0]
      quantity = product[1]

      for productDesc in products:
        if(productDesc['id'] == product_id):
          #Calculate sales tax
          sales_tax = quantity*self.calculateSalesTax(productDesc['price'], productDesc['category'])
          #Calculate import tax
          import_tax = quantity*self.calculateImportTax(productDesc['price'], productDesc['imported'])
          #get total tax by adding sales tax, import tax
          total_tax = total_tax + sales_tax + import_tax
          #get total product price by adding tax to the price
          productTotalPrice = (quantity * productDesc['price']) + sales_tax + import_tax
          total_price = total_price + productTotalPrice

          print(str(quantity) + ' ' + productDesc['name'] + ': ' + "{:.2f}".format(productTotalPrice) + '\n')

    print("Sales Taxes: " + "{:.2f}".format(total_tax) + '\n')
    print("Total: " + "{:.2f}".format(total_price) + '\n')

a = shopping_basket()
a.add()
a.displayReceipt()