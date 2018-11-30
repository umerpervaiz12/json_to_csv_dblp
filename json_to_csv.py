import json
import csv

with open('test1.json') as lines, open('data3.csv', 'w',encoding='utf-8') as output:
    output = csv.DictWriter(output, ['abstract','authors','n_citation',"references","title","venue","year",'id'],lineterminator='\n')
    output.writeheader()
    for line in lines:
        line = line.strip()
        if line[0] == '{' and line[-1] == '}':
            output.writerow(json.loads(line))