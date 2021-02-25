"""
speccy xml_to_html
Переводит XML вывод от Speccy в htlm таблицу

"""

import xml.etree.ElementTree as ET
import glob
import os
import sys
sys.stdout=open("test.html","w") # запись в файл вывода программы



fields = ['Motherboard', 'CPU', 'RAM', 'Graphics', 'Storage'] # какие поля выводить в таблицу

print("<html><head><style type='text/css'>table{font-family:sans-serif;font-size:x-small;}</style></head><body>")
print("<table border="'1'">")
print("<thead>")
print("<th>Machine</th>")
for field in fields:
    print("<th>" + field + "</th>")
print("</thead>")
print("<tbody>")

files = glob.glob('*.xml')

for file in files:
    root = ET.parse(file).getroot()
    file_clr = os.path.splitext(file)[0] # убираем расширение .xml
    print("<tr>")
    print("<td>" + file_clr + "</td>")

    for field in fields:
        print("<td>")
        sections = root.findall("./mainsection/section[@title='" + field + "']/entry")
        for s in sections:
            print(s.get('title') + "<br />")
        print("</td>")

    print("</tr>")

print("</tbody>")
print("</table>")
print("</body></html>")
sys.stdout.close()