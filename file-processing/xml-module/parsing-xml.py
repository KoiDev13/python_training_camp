import sys
import defusedxml.ElementTree as ET

file_name = 'dataset.xml'

try:
    tree = ET.parse(file_name)
except FileNotFoundError:
    print(f'File {file_name} is not found!')
    sys.exit(1)

for product in tree.findall("record"):
    idProd = product.findtext("id")
    name = product.findtext("product")
    price = product.findtext("price")
    # currency = price.get("currency") or "USD"

    # if currency == "EUR":
    #     price_text = f"{price.text.replace('.',',')} \u20ac"
    # else:
    #     price_text = f"${price.text}"

    message = f"""
        {idProd} - {name} - {price} 
    """

    print(message)