import xml.etree.ElementTree as ET

tree = ET.parse('SYSADMIN.xml')
root = tree.getroot()
elem = root.find('mainsection')[0]
for subelem in elem:
    print(subelem.tag)
    print(subelem.attrib)
a = 0
print(elem.tag)
print(elem.attrib)

# for ttt in elem:
#     print(ttt)
#     a += 1
#     print(ttt.attrib)
#     #print(ttt.text)
#     print(ttt.tag)
#     print(a)




