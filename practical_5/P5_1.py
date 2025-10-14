
import sys
import csv

    
with open('practical_5.csv', 'w') as file:

    writer = csv.writer(file)

    writer.writerow(['name','age','sex','hair','eyes'])
    writer.writerow(['herman','45','male','long','brown'])
    writer.writerow(['gill','38','female','short','brown'])
    writer.writerow(['hanna','42','female','long','blue'])
    writer.writerow(['mark','49','male','bald','blue'])
    writer.writerow([sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]])
    
