class Tax:
    pass

    def tax_calc(self):
        print(5*self)

tax = Tax()
class Shipping:
    pass

    def shipped_calc(self):
        print(5*self)

shipping = Shipping()

if __name__ == "__main__":
    print("Started")