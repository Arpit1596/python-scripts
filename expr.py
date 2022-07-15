import pandas as pd
import xml.etree.ElementTree as ET

etree = ET.parse("./ssp.xml")
dim_rows = []
expr_rows = []
expression = []
type = []
root = etree.getroot()
for dim, expr in zip(root.find('dim_attributes'), root.find('expressions')):
    # dim_rows.append(dim.attrib.copy())
    if str(expr.find('expr_spec').get('expr')).__contains__('sum') or str(
            expr.find('expr_spec').get('expr')).__contains__('.') or str(
            expr.find('expr_spec').get('expr')).__contains__('SUM'):
        pass
    else:
        type.append(expr.attrib.get('_type'))
        expr_rows.append(expr.attrib.get('name'))
        expression.append(expr.find('expr_spec').get('expr'))

expr_df = pd.DataFrame(list(zip(expr_rows, type, expression)))
expr_df.columns = ["name", "type", "expression"]

print(expr_df.to_json(orient='records', lines=True, indent=1))
