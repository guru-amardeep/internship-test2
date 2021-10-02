import csv
with open('main.csv','rt')as f:
  data = csv.reader(f)
  attributes = next(data)
  l=[]
  rowno=0
  for row in data:
      newl=[row[31],row[30],row[0]]
      l.append(newl)
header=[attributes[31],attributes[30],attributes[0]]
l.sort(reverse=True)
n=len(attributes)
print(l)
filename='solution3.csv'
with open(filename, 'w') as file:
    for header in header[::-1]:
        file.write(str(header) + ', ')
    file.write('\n')
    for row in l:
        for x in row[::-1]:
            file.write(str(x) + ', ')
        file.write('\n')