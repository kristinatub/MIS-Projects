import csv
from nltk.corpus import stopwords
import re
import string
from collections import defaultdict

stop = stopwords.words('english')

inter1 = []
sentences_all = []
sentences_clean = []
sentences_unpun = []
highest_list=[]

dictionary1 = {}
d2_dict = defaultdict(dict)

with open('yelp_sentistrength.csv','rU') as f:
    rows = csv.reader(f, delimiter = ',')
    for row in rows:
        inter1.append(row[6])

for row in inter1:
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', row)
    num1=inter1.append(row[6])
    num2=inter1.append(row[7])
    num1+num2=num3
    highest_list.append(num3)
    print(highest_list.max)


writer = csv.writer(open('highest_sentistrength.csv', 'wb'))

print "written to wsentistrength.csv"
