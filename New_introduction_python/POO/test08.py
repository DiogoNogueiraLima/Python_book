# oop/class.price.py
class Price:
    def final_price(chaluba, vat, discount=0):
        """Returns price after applying vat and fixed disc"""
        return (chaluba.net_price * (100 + vat) / 100) - discount
p1 = Price()
p1.net_price = 100
print(Price.final_price(p1, 20, 10)) # 110 (100 * 1.2 - 1
print(p1.final_price(20, 10)) # equivalent