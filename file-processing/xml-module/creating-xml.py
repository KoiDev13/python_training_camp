import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, ElementTree
from xml.dom.minidom import parseString


def create_employee(name, age, years_with_company=0):
    employee = Element("employee")
    # employee.set('name', name)

    name_tag = ET.SubElement(employee, 'name')
    name_tag.text = str(name)

    age_tag = ET.SubElement(employee, 'age')
    age_tag.text = str(age)

    years_tag = ET.SubElement(employee, 'years_with_company')
    years_tag.text = str(years_with_company)

    return employee

# ET.dump(create_employee('Khoi', 29,3))

employees =[
    {'name':'Khoi 1', 'age':29, 'years_with_company':3},
    {'name':'Khoi 2', 'age':30, 'years_with_company':4},
    {'name':'Khoi 3', 'age':31, 'years_with_company':5},
]

root = Element('employees')

for employee in employees:
    employee_tag = create_employee(**employee)
    root.append(employee_tag)

tree = ElementTree(element=root)
tree.write("output.xml",
            encoding="UTF-8",
            xml_declaration=True)
# ET.dump(root)

xml_string = ET.tostring(root)
dom = parseString(xml_string)

prety_xml = dom.toprettyxml(encoding="UTF-8")
with open("pretty.xml",'wb') as f:
    f.write(prety_xml)