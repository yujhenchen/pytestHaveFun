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
