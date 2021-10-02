import csv
with open('main.csv ','rt')as f:
  data = csv.reader(f)
  attributes = next(data)
  l=[]
  for row in data:
      l.append(row)
res=[]
c=0
n=len(attributes)
newl=[0]*(n-1)
for i in l:
    if c<=10:
        if c==0:
            newl[0]=i[0]
        newl[1]+=int(i[2])
        newl[2]+=int(i[3])
        newl[3] += int(i[4])
        newl[4] += int(i[5])
        newl[5] += int(i[6])
        newl[6] += int(i[7])
        newl[7] += int(i[8])
        newl[8] += int(i[9])
        newl[9] += int(i[10])
        newl[10] += int(i[11])
        c+=1
        if c==10:
            c=0
            res.append(newl)
            newl=[0]*(n-1)
res.append(newl)
attributes.remove('Total')
attributes[0]=''
filename='solution1.csv'
with open(filename, 'w') as file:
    for header in attributes:
        file.write(str(header) + ', ')
    file.write('\n')
    for row in res:
        for x in row:
            file.write(str(x) + ', ')
        file.write('\n')

