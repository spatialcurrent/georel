# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2018 Spatial Current, Inc.
#
#########################################################################
import unittest

test_cases = {
    "simple": {
        "input": [
            {"value": "1000"},
            {"value": "1,000"}
        ],
        "output": {"value": 1000, "units": None}
    },
    "source": {
        "input": [
            {"value": "1000", "units": "mtrs"},
            {"value": "1000", "units": "meter"},
            {"value": "1,000", "units": "meters"},
            {"value": "1000", "units": "m"},
            {"value": "1,000", "units": "mtrs"}
        ],
        "output": {"value": 1000, "units": "meter"}
    },
    "transform": {
        "input": [
            {"value": "1000", "src": "mtrs", "dst": "mi"},
            {"value": "1000", "src": "meter", "dst": "mi"},
            {"value": "1000", "src": "m", "dst": "mile"},
            {"value": "1,000", "src": "mtrs", "dst": "miles"}
        ],
        "output": {"value": 0.621371, "units": "mile"}
    },
}


class TestGeorel(unittest.TestCase):
    """
    TestGeorel is used for testing georel
    """

    def test_simple(self):
        import georel

        for x in test_cases["simple"]["input"]:
            try:
                self.assertEqual(georel.parse(x["value"], None), test_cases["simple"]["output"])
            except Exception as err:
                print "Input Object:", x
                print "Calculated Value:", georel.parse(x["value"], None)
                print "Valid Value:", test_cases["simple"]["output"]
                raise err

    def test_source(self):
        import georel

        for x in test_cases["source"]["input"]:
            try:
                self.assertEqual(georel.parse(x["value"], x["units"]), test_cases["source"]["output"])
            except Exception as err:
                print "Input Object:", x
                print "Calculated Value:", georel.parse(x["value"], x["units"])
                print "Valid Value:", test_cases["source"]["output"]
                raise err

    def test_transform(self):
        import georel

        for x in test_cases["transform"]["input"]:
            try:
                self.assertEqual(georel.parse(x["value"], x["src"], x["dst"]), test_cases["transform"]["output"])
            except Exception as err:
                print "Input Object:", x
                print "Calculated Value:", georel.parse(x["value"], x["src"], x["dst"])
                print "Valid Value:", test_cases["transform"]["output"]
                raise err


if __name__ == '__main__':
    unittest.main()
