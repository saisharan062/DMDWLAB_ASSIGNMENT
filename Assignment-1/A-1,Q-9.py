class Product:
    def input(self):
        self.product_no=int(input("enter the product number:"))
        self.product_name=input("enter the name:")
        self.cost=int(input("enter the cost:"))
        self.quantity=int(input("enter the qty:"))
    def calculator(self):
        self.total_amount=self.cost*self.quantity;
    def display(self):
        print("product_no-",self.product_no)
        print("product_name-",self.product_name)
        print("cost-",self.cost)
        print("quantity-",self.quantity)
        print("Total_amount-",self.total_amount)
pk=[]
for i in range(5):
    print("Enter the product:",i+1)
    p=Product()
    p.input()
    p.calculator()
    pk.append(p)
high=pk[0]
#pn=pk[0]
for i in pk:
    if p.total_amount>high.total_amount:
        high=p
        pn=p
print("\n Highest cost:")
high.display()
#pn.display()
