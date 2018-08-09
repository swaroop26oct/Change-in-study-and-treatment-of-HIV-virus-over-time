import csv
...


with open('date_plus_abstract_hiv.csv',encoding='utf-8') as input, open('actual_new.csv', 'w',encoding='utf-8', newline='') as output:
     writer = csv.writer(output)
     for row in csv.reader(input):
         if any(field.strip() for field in row):
             writer.writerow(row)
