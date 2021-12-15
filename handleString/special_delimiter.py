def parse_string_by_keys(text, keys):
    dataMap = {}
    delimiter = " : "
    emptyDelimiter = " "

    for key in keys:
        # print(key)

        # Get the index in text where sub text is key+delimiter
        # Get sub text from that index + 1 until before reach the first empty
        indexOfKey = text.index(key + delimiter)
        indexOfValue = indexOfKey + len(key) + len(delimiter)
        value = ""
        for i in range(indexOfValue, len(text)):
            if text[i] == emptyDelimiter:
                break
            value += text[i]
        dataMap[key] = value
    return dataMap


text = "AAA Version : 1.0.0.21 BBB Info : XXX00001 CCC Data : A1.01.010203 DDD Version : EEE Info : 0.1.0.4 FFF Data : 1.0.0.11"
keys = ["AAA Version", "BBB Info", "CCC Data",
        "DDD Version", "EEE Info", "FFF Data"]

resultsMap = parse_string_by_keys(text, keys)
for key in resultsMap:
    print(key + "_" + resultsMap[key])
