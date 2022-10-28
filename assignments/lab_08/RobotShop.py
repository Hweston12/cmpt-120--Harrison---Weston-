from math import prod


class ProductInformation:
    #constructor 
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def in_stock(self, quantity):
        return self.quantity >= quantity

    def deduct(self, quantity):
        self.quantity -= quantity
  
    def total_cost(self):
        return self.price * self.quantity


p1 = ProductInformation(0, "Ultrasonic range finder", 2.50, 4)
p2 = ProductInformation(1, "Serveo Motor", 14.99, 10)
p3 = ProductInformation(2, "Servo Controller", 44.95, 5)
p4 = ProductInformation(3, "Microcontroller Board", 34.95, 7)
p5 = ProductInformation(4, "Laser range finder", 149.99, 2)
p6 = ProductInformation(5, "Lithium polymer battery", 8.99, 8) 

products = [p1, p2, p3, p4, p5, p6]

def print_stock():
    print("\nAvailable Product")
    print("-------------")
    for i in range(0, len(products)):
        if products[i].quantity > 0:
            print(f"{str(i)}) {products[i].name}, ${products[i].price}, {products[i].quantity} in stock")
    print()

def main():
    cash = float(input("How much moiney do you have? $"))
    while cash > 0:
        print_stock()
        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")
        if vals[0] == "quit": break

        prod_id = int(vals[0])
        count = int(vals[1])

        product = None
        for p in products:
            if p.id == prod_id:
                product = p
        
        if product == None:
            print(f"Product with id {prod_id} not found.")
            continue

        if not product.in_stock(count):
            print("Not enough quantity!")
            continue

        price = product.price * count

        if cash < price:
            print("Not enough money!")
        
        product.deduct(count)
        cash -= price

        print("You have {0:.2f} remaining.".format(cash))

        # if product_quantites[prod_id] >= count:
        #     if cash >= product_prices[prod_id]:
        #         product_quantites[prod_id] * count
        #         cash -= product_prices[prod_id] * count
        #         print("You purchase", count, product_names[prod_id] + ".")
        #         print("You have $", "{0:.2f}".format(cash), "remaning.")
        #     else:
        #         print("Sorry, you cannot afford that product")
        # else: 
        #     print("Sorry, we are sold out of", product_names[prod_id])


main()
