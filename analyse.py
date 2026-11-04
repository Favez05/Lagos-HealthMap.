from pathlib import Path
csv_path = Path(__file__).parent / 'wards.csv'
with open (csv_path) as f:
    lines = f.readlines()
#print('Number of lines:', len(lines))
total = 0
for line in lines:
    print(line.strip())
def classify(area_km2):
     if area_km2 > 500:
        return 'large'
     elif area_km2 <= 300:
        return 'small'
     else:
        return 'medium'
for line in lines[1:]:
    parts = line.strip().split(',')
    wards = parts[0]
    area = parts[1]
    #print(wards, 'has area', area)
    area_km2 = float(parts[1])
    size =  classify(area_km2)
    total = total + area_km2
    area_hectares = area_km2 * 100
    print(wards, 'is', area_hectares )
    print(wards, 'is', size)
print('total area equals', total)
