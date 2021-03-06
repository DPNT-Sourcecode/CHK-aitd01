from collections import defaultdict
from .products import PRICES, MULTIBUY, FREE, BUYANY



class Shopping():

    def __init__(self):
        self.basket = defaultdict(lambda : {"count": 0, "subtotal": 0})


    def add(self, item):
        self.basket[item]["count"] += 1
        self.basket[item]["subtotal"] += PRICES[item]


    def apply_freebes(self):
        for item, free_deal in FREE.items():
            if item not in self.basket:
                continue

            deal_multiple = self.basket[item]["count"] // free_deal["count"]
            for freebe, count in free_deal["items"].items():
                self.basket[freebe]["count"] -= deal_multiple * count
                if self.basket[freebe]["count"] < 0:
                    self.basket[freebe]["count"] = 0

                self.basket[freebe]["subtotal"] = self.basket[freebe]["count"] * PRICES[freebe]


    def apply_multibuy(self):
        for item, deal_list in MULTIBUY.items():
            if item not in self.basket:
                continue

            remainder = self.basket[item]["count"]
            subtotal = 0
            for deal in deal_list:
                if remainder >= deal["count"]:
                    multibuys_count = remainder // deal["count"]
                    remainder = remainder % deal["count"]
                    subtotal += multibuys_count * deal["price"]

            self.basket[item]["subtotal"] = subtotal + remainder * PRICES[item]


    def apply_buyany(self):
        for any_of_list, any_deal in BUYANY.items():
            purchased = ""
            for item in any_of_list:
                purchased += self.basket[item]["count"] * item

            while purchased:
                count = any_deal["count"]
                anybuy = purchased[:count]
                purchased = purchased[count:]
                if len(anybuy) == count:
                    self.basket[anybuy]["count"] += 1
                    self.basket[anybuy]["subtotal"] += any_deal["price"]

                    for item in anybuy:
                        self.basket[item]["count"] -= 1
                        self.basket[item]["subtotal"] -= PRICES[item]


    def total(self):
        cost = 0
        for _, items in self.basket.items():
            cost += items["subtotal"]

        return cost

    def checkout(self, skus):
        if skus == None:
            return -1

        for item in skus:
            if item not in PRICES:
                return -1

            self.add(item)

        self.apply_freebes()
        self.apply_buyany()
        self.apply_multibuy()

        return self.total()


def checkout(skus):
    shopping = Shopping()
    return shopping.checkout(skus)
