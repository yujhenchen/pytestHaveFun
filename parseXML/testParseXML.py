from parseXML import ParseXML


def test_print_elements_attributes():
    parseXML = ParseXML('example.xml')
    elements = parseXML.get_elements('build')
    parseXML.print_elements_attributes(
        elements, ['id', 'number', 'status', 'state', 'href'])
