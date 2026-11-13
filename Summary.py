import csv

def clean_data(filename):
    with open(filename, encoding= 'utf-8-sig') as f:
    
       rows = (list(csv.DictReader(f)))
       return(rows)
 
def data_value(rows, column, name_column):
    value = []
    Largest_area = 0
    Location_with_largest_area = ''
    for row in rows:
        if 'Name' in row:
            row['Name'] = row['Name'].replace('en:', '')
        raw = row[column].strip()
        if len(row[column].strip()) == 0:
            continue

        current_area = float(row[column])

        current_location =  row[name_column]
        if current_area > Largest_area:
            Largest_area = current_area
            Location_with_largest_area = current_location
        value.append(current_area)
    return(value, Largest_area, Location_with_largest_area)
       

def summary(value, max_location):
    total = 0



    if len(value) == 0:
        return{'count': 0, 'smallest': None, 'maximum': None, 'Average': None}
    return{
        'smallest': min(value) ,
        'largest': max(value),
        'count': len(value),
        'Average': sum(value) / len(value),
        'Largest_area': max_location
    }

def summarise_all(filename, columns):
    row = clean_data(filename)
    report = {}
    for column in columns:
        value_list, max_area, max_location = data_value(row, column, 'Name')
        report[column] = summary(value_list, max_location)
    return(report)

report = summarise_all('LagosBoundary.csv', ['Area', 'Area_km2'])

for column, stats in report.items():
    print(column, '->', stats)




