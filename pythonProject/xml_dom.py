import xml.dom.minidom


if __name__ == '__main__':
    dom = xml.dom.minidom.parse('examplexml.xml')
    people = dom.documentElement
    employees = people.getElementsByTagName('Employee')
    for employee in employees:
        print(f"\nEmployee: {employee.getAttribute('id')}")

        name = employee.getElementsByTagName('name')[0].childNodes[0].nodeValue
        position = employee.getElementsByTagName('position')[0].childNodes[0].nodeValue
        number = employee.getElementsByTagName('number')[0].childNodes[0].nodeValue

        print(f"Name: {name}")
        print(f"Position: {position}")
        print(f"Number: {number}")