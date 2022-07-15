import pandas as pd
import xml.etree.ElementTree as ET

#etree = ET.parse("./ssp.xml")
#dim_rows = []
#expr_rows = []
#expression = []
#root = etree.getroot()
#for dim, expr in zip(root.find('dim_attributes'), root.find('expressions')):
#    dim_rows.append(dim.attrib.copy())
#    expr_rows.append(expr.attrib.copy())
#    expression.append(expr.find('expr_spec').get('expr'))

#dim_df = pd.DataFrame(dim_rows)
#expr_df = pd.DataFrame(expr_rows)
#expr_df['expr'] = expression

#print(expr_df.to_string())

etree = ET.parse("./fact.xml")
etree2 = ET.parse("./ssp.xml")
root = etree.getroot()
root2 = etree2.getroot()
cols = []
comments = []
types = []
des = []
for col in root.find('columns'):
    name = col.attrib.get('name')
    type = col.attrib.get("_type")
    comment = col.attrib.get('comment')
    cols.append(name)
    types.append(type)
    for dim in root2.find('dim_attributes'):
        if dim.attrib.get('name') == name:
            comment = dim.attrib.get("description")
        else:
            pass
    comments.append(comment)




expr_df = pd.DataFrame(list(zip(cols, types, comments)))
print(expr_df.to_string())
expr_df.columns = ["name","type","description"]


print(expr_df.to_json(orient ='records',lines=True,indent = 1))



