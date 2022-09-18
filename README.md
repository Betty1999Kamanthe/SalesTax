# SalesTax
Basic sales tax is applied at a rate of 10% on all goods, except books,food, and medical products, which are exempt. An import duty is an additional sales tax applicable on all imported goods at a rate of 5%, with no exemptions.
When I purchase items, I receive a receipt that lists the name of all the items and their price (including tax), along with the total cost of the items, and the total amounts of the taxes paid. The rounding rules for sales tax are as follows; for a tax rate of n%, a shelf price of p contains (np/100 rounded up to the nearest 0.05) amount of sales tax.

Write an application that prints out the receipt details for these shopping

Baskets:

Input Basket #1:

  1 book at 12.49
  
  1 music CD at 14.99
  
  1 chocolate bar at 0.85
  
Input Basket #2:

1 imported box of chocolates at 10.00

1 imported bottle of perfume at 47.50

Input Backet #3:

1 imported bottle of perfume at 27.99

1 bottle of perfume at 18.99

1 packet of headache pills at 9.75

1 box of imported chocolates at 11.25

The calculator should produce the following output.

Output for Basket #1:

1 book: 12.49

1 music CD: 16.49

1 chocolate bar: 0.85

Sales Taxes: 1.50

Total: 29.83

Output for Basket #2:

1 imported box of chocolates: 10.50

1 imported bottle of perfume: 54.65

Sales Taxes: 7.65

Total: 65.15

Output for Basket #3:

1 imported bottle of perfume: 32.19

1 bottle of perfume: 20.89

1 packet of headache pills: 9.75

1 imported box of chocolates: 11.85

Sales Taxes: 6.70

Total: 74.68

============================

# Solution

First I created a python dictionary that contains all the products available in the store. Then created a Class called Shopping Basket. The user can add products into the basket using the product id.

If the id doesn't exist then a message "Product doesn't exist" message is displayed. After items have been added to the basket then the tax and total price are calculated.
