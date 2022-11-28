import xml.sax


class ParserUse(xml.sax.ContentHandler):
    def startElement(self, tag, attrs):
        self.current = tag
        if tag == "Employee":
            print(f"\nEmployee: {attrs['id']}")

    def characters(self, tag):
        if self.current == "name":
            self.name = tag
        elif self.current == "position":
            self.position = tag
        elif self.current == "number":
            self.number = tag

    def endElement(self, tag):
        if self.current == "name":
            print(f"Name: {self.name}")
        elif self.current == "position":
            print(f"Position: {self.position}")
        elif self.current == "number":
            print(f"Number: {self.number}")
        self.current = ''


if __name__ == '__main__':
    handler = ParserUse()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse('examplexml.xml')
