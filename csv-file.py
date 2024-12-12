import csv
field_name = ['No', 'Company', 'Car Model']
car = [
 {'No': 1, 'Company': 'Ferrari', 'Car Model': 'GH'},
 {'No': 2, 'Company': 'BMW', 'Car Model': 'X5'},
 {'No': 3, 'Company': 'Maruti Suzuki', 'Car Model': 'Swift'},
 {'No': 4, 'Company': 'Audi', 'Car Model': 'RS7'},
 {'No': 5, 'Company': 'Toyota', 'Car Model': 'Fortuner'}
]
# Writing to the CSV file
with open('car.csv', 'w', newline='') as csvfile:
 write=csv.DictWriter(csvfile, fieldnames=field_name)
 write.writeheader()
 write.writerows(car)
# Reading from the CSV file
with open('car.csv', newline='') as csvfile:
 d = csv.reader(csvfile) # No need to specify delimiter='|' since it's comma-separated
 for r in d:
  print(','.join(r))
