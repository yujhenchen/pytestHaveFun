import xml.etree.ElementTree as ET


class ParseXML(object):
    def __init__(self, xmlFile):
        super().__init__()
        self.tree = ET.parse(xmlFile)
        self.root = self.tree.getroot()

    def get_elements(self, text):
        return self.root.findall(text)

    def print_elements_attributes(self, elements, attributes):
        for element in elements:
            for attribute in attributes:
                attributeText = element.get(attribute)
                print(attributeText)
            print()
