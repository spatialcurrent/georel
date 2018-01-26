DISTANCE_STOP_WORDS = ["a", "an", "the"]

NUMBERS_AS_WORDS = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten"
    "eleven"
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventenn",
    "eighteen",
    "nineteen",
    "twenty"
]

UNITS_MATRIX = {
    "meter": {
        "words": ["meters", "metres", "mtrs", "meter", "metre", "m"],
        "multiplier": {
            "foot": 3.28084,
            "kilometer": 0.001,
            "mile": 0.000621371
        }
    },
    "foot": {
        "words": ["foot", "feet", "ft"],
        "multiplier": {
            "meter": 0.3048,
            "kilometer": 0.0003048,
            "mile": 0.000189394
        }
    },
    "kilometer": {
        "words": ["kilometers", "kilometer", "km", "kms"],
        "multiplier": {
            "foot": 3280.84,
            "meter": 1000,
            "mile": 0.621371
        }
    },
    "mile": {
        "words": ["miles", "mile", "mi"],
        "multiplier": {
            "foot": 5280,
            "meter": 1609.34,
            "kilometer": 1.60934
        }
    }
}
