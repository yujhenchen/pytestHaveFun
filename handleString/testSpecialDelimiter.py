from specialDelimiter import parse_string_by_keys

import pytest


@pytest.fixture
def data():
    text = "AAA Version : 1.0.0.21 BBB Info : XXX00001 CCC Data : A1.01.010203 DDD Version : EEE Info : 0.1.0.4 FFF Data : 1.0.0.11"
    keys = ["AAA Version", "BBB Info", "CCC Data",
            "DDD Version", "EEE Info", "FFF Data"]
    return {"text": text, "keys": keys}


def testSpecialDelimiter(data):
    resultsMap = parse_string_by_keys(data["text"], data["keys"])
    for key in resultsMap:
        print(key + "_" + resultsMap[key])
