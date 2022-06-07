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
        "count"
        "B": 1
    }
}


class Shopping():

    def __init__(self):
        self.items = defaultdict(lambda : {"count": 0, "subtotal": 0})

    def add(self, item):
        self.items[item]["count"] += 1
        self.items[item]["subtotal"] += PRICES[item]

    def apply_offers(self):

        for item, deal_list in MULTIBUY.items():
            if item not in self.items:
                continue

            count = self.items[item]["count"]
            subtotal = 0
            for deal in deal_list:
                if count >= deal["count"]:
                    multibuys_count = count // deal["count"]
                    count = count % deal["count"]
                    subtotal += multibuys_count * deal["price"]
            
            self.items[item]["subtotal"] = subtotal

        #  for item, free in FREE.items():

        #     # apply freebes
        #     # if "free" in deals:

    def checkout(self, skus):
        if skus == None:
            return -1

        for item in skus:
            if item not in PRICES:
                return -1

            self.add(item)


    total = 0
    # apply offers
    for item, count in shopping.items():
        offer = OFFERS.get(item)
        if not offer:
            total += count * PRICES[item]
        else:
            if "multibuy" in offer:
                total += calc_multibuy(item, count)

            # multibuys_count = count // offer["multibuy"]["count"]
            # remainder = count % offer["count"]
            # total += multibuys_count * offer["price"] + remainder * PRICES[item]



    return total






