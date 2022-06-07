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

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if skus == None:
        return -1

    shopping = defaultdict(int)
    for item in skus:
        if item not in PRICES:
            return -1

        shopping[item] += 1

    total = 0
    for item, count in shopping.items():
        offer = OFFERS.get(item)
        if not offer:
            total += count * PRICES[item]
        else:
            multibuys_count = count // offer["count"]
            remainder = count % offer["count"]
            total += multibuys_count * offer["price"] + remainder * PRICES[item]

    return total



