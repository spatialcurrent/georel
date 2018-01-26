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
            "kilometer": 0.001,
            "mile": 0.000621371
        }
    },
    "kilometer": {
        "words": ["kilometers", "kilometer", "km", "kms"],
        "multiplier": {
            "meter": 1000,
            "mile": 0.621371
        }
    },
    "mile": {
        "words": ["miles", "mile", "mi"],
        "multiplier": {
            "meter": 1609.34,
            "kilometer": 1.60934
        }
    }
}
