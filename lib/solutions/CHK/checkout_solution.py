from collections import defaultdict

PRICES = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40
}

MULTIBUY = {
    "A": [
            {
                "count": 5,
                "price": 200
            },
            {
                "count": 3,
                "price": 130
            },
        ],
    "B": [
            {
                "count": 2,
                "price": 45
            },
        ]
}

FREE = {
    "E": {
        "count": 2,
        "items": {
            "B": 1
        }
    }
}


class Shopping():

    def __init__(self):
        self.basket = defaultdict(lambda : {"count": 0, "subtotal": 0})

    def add(self, item):
        self.basket[item]["count"] += 1
        self.basket[item]["subtotal"] += PRICES[item]

    def apply_offers(self):
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


        # for item, free_deal in FREE.items():
        #     if item not in self.basket:
        #         continue

        #     free_multiple = self.basket[item]["count"] // free_deal["count"]
        #     # for freebe, count in free_deal["items"]:
        #     #     //self.basket

        #     self.basket[]
        #     # apply freebes
        #     # if "free" in deals:

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

        self.apply_offers()

        return self.total()


def checkout(skus):
    shopping = Shopping()
    return shopping.checkout(skus)
    


    # total = 0
    # # apply offers
    # for item, count in shopping.items():
    #     offer = OFFERS.get(item)
    #     if not offer:
    #         total += count * PRICES[item]
    #     else:
    #         if "multibuy" in offer:
    #             total += calc_multibuy(item, count)

    #         # multibuys_count = count // offer["multibuy"]["count"]
    #         # remainder = count % offer["count"]
    #         # total += multibuys_count * offer["price"] + remainder * PRICES[item]



    # return total
