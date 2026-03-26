import re

n = int(input())

barcode_pattern = r'@#+([A-Z][A-Za-z0-9]{4,})[A-Z]@#+'

for _ in range(n):
    barcode = input()
    match = re.match(barcode_pattern, barcode)

    if match:
        core = match.group(1)
        product_group = ''.join(re.findall('\d', core)) or '00'
        # product_group = ''.join(filter(str.isdigit, core)) or '00'
        print(f"Product group: {product_group}")
    else:
        print('Invalid barcode')