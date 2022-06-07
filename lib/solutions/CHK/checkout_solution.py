from collections import defaultdict

PRICES = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40
}

OFFERS = {
    "A": {
        "multibuy": [
            {
                "count": 3,
                "price": 130
            },
            {
                "count": 5,
                "price": 200
            }
        ]
    },
    "B": {
        "multibuy": [
            {
                "count": 2,
                "price": 45
            },
        ]
    },
    "E": {
        "free": {
            "B": 1
        }
    }
}


class Shopping():

    def __init__(self):
        self.items = defaultdict(lambda : {"count": 0, "subtotal": 0})

    def add(self, item):
        self.items[item]["count"] += 1
        self.items[item]["subtotal"] += PRICES[item]




# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if skus == None:
        return -1

    shopping = defaultdict(lambda : {"count": 0, "subtotal": 0})
    for item in skus:
        if item not in PRICES:
            return -1

        shopping[item]["count"] += 1
        shopping[item]["subtotal"] += PRICES[item]


    total = 0
    # apply offers
    for item, deals in OFFERS:
        if item not in shopping:
            continue

        # # apply freebes
        # if "free" in deals:




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

