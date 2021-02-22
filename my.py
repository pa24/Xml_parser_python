import xml.dom.minidom

dom = xml.dom.minidom.parse("SYSADMIN.xml");
dom.normalize()

Section = dom.getElementsByTagName("entry")
for title in Section:
    print(title.getAttribute("title"))

# if title.getAttribute("title") == "8,00ГБ":
#   print("work")
