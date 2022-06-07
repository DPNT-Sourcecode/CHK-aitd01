PRICES = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,    |                        |
    "H": 10,    | 5H for 45, 10H for 80  |
    "I": 35,    |                        |
    "J": 60,    |                        |
    "K": 80,    | 2K for 150             |
    "L": 90,    |                        |
    "M": 15,    |                        |
    "N": 40,    | 3N get one M free      |
    "O": 10,    |                        |
    "P": 50,    | 5P for 200             |
    "Q": 30,    | 3Q for 80              |
    "R": 50,    | 3R get one Q free      |
    "S": 30,    |                        |
    "T": 20,    |                        |
    "U": 40,    | 3U get one U free      |
    "V": 50,    | 2V for 90, 3V for 130  |
    "W": 20,    |                        |
    "X": 90,    |                        |
    "Y": 10,    |                        |
    "Z": 50,    |                        
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
        ],
    "H": [
        {
            "count": 10,
            "price": 80
        },
        {
            "count": 5,
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
    },
    "F": {
        "count": 3,
        "items": {
            "F": 1
        }
    }
}