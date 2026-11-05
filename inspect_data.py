import csv

# with open('LagosBoundary.csv', encoding = 'utf-8-sig') as f:
#     reader = csv.DictReader(f)
#     rows = list(reader)

# # print('Number of rows:', len(rows))
# # print('Columns:', list(rows[0].keys()))

# values = []
# for row in rows:
#    raw = row['Area'].strip()
#    if raw == '':
#        continue
#    values.append(float(raw))

# print('Smallest:', min(values))
# print('Largest:', max(values))
# print('count:', len(values))

def  inspect_column(filename, column):
    with open(filename, encoding= 'utf-8-sig') as f:
        rows  = list(csv.DictReader(f))

    total = 0

    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == '':
            continue
        values.append(float(raw))
        total = total + float(raw)
        

    return{
        'smallest': min(values),
        'largest': max(values),
        'Count': len(values),
        'Total': total,
        'Mean': sum(values) / len(values)
    }
result = inspect_column('LagosBoundary.csv', 'Area')
print(result)

result = inspect_column('LagosBoundary.csv', 'Area_km2')
print(result)