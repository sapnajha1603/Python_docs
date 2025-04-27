

class business():
  def __init__(self, sale, profit, ad):
    self.sale = sale
    self.profit = profit
    self.ad = ad

rajeev = business(6000,2000,1000)
vikrant = business(8000,2000,1000)
sapna = business(20000,2000,1000)


print(f"Rajeev made a sale of: {rajeev.sale}")
print(f"Vikrant made a sale of: {vikrant.sale}")
print(f"Sapna made a sale of: {sapna.sale}")
# sales1 = 6000
# profit1 = 2000
# ad1 = 1000
# # rajeev.sales

# sales2 = 6000
# profit2 = 2000
# ad2 = 1000 
# # vikrant.sales

# sales3 = 6000
# profit3 = 2000
# ad3 = 1000
'''
Instead of creating sales for 3 diff people we could create a class with requirements and multiple objects say rajeev, vikrant and dhruv
which will have all the req present in the class'''
 
# RailwayForm   ---> Class [blueprint]
# harry --> harry ki info wala form --> Object [entity]
# tom --> tom ki info wala form --> Object [entity]
# shubham -- shubham ki info wala form --> Object [entity]
# # shubham.changeName("Shubhi")