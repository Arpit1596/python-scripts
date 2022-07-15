import pandas as pd
import xml.etree.ElementTree as ET

etree = ET.parse("./fact.xml")
etree2 = ET.parse("./ssp.xml")

root = etree.getroot()
root2 = etree2.getroot()
cols = []
names = []
comment = []
m_type = []
expr = []
for col in root.find('columns'):
    name = col.attrib.get('name')
    cols.append(name)

for measure in root2.find('measures'):
    m_name = measure.attrib.get('name')
    if m_name in cols:
        names.append(measure.attrib.get('display_string'))
        comment.append(measure.attrib.get('description'))
        m_type.append(measure.attrib.get('_type'))
        expr.append(f'SUM( [{m_name}] )')

df = pd.DataFrame(list(zip(names, comment, m_type, expr)))
df.columns = ["name", "comment", "type", "dax_expression"]
print(df.to_json(orient='records', lines=True, indent=1))
