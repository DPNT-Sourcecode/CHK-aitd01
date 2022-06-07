from collections import defaultdict

PRICES = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15
}

OFFERS = {
    "A": {
        "count": 3,
        "price": 130
    },
    "B": {
        "count": 2,
        "price": 45
    }
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    shopping = defaultdict(int)
    for item in skus.split():
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

