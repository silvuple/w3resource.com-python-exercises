# 1. Write a Python program to read each row from a given csv file and print a list of strings. 
import sys
import csv
with open('departments.csv', newline='') as csvfile:
 data = csv.reader(csvfile, delimiter=' ', quotechar='|')
 for row in data:
   print(', '.join(row))
'''
department_id,department_name,manager_id,location_id
10,Administration,200,1700
20,Marketing,201,1800
30,Purchasing,114,1700
40,Human Resources,203,2400
50,Shipping,121,1500
60,IT,103,1400
70,Public Relations,204,2700
80,Sales,145,2500
90,Executive,100,1700
100,Finance,108,1700
110,Accounting,205,1700
120,Treasury,,1700
130,Corporate Tax,,1700
140,Control And Credit,,1700
150,Shareholder Services,,1700
160,Benefits,,1700
170,Manufacturing,,1700
180,Construction,,1700
190,Contracting,,1700
200,Operations,,1700
210,IT Support,,1700
220,NOC,,1700
230,IT Helpdesk,,1700
240,Government Sales,,1700
250,Retail Sales,,1700
260,Recruiting,,1700
270,Payroll,,1700
'''

# 2. Write a Python program to read a given CSV file having tab delimiter. 
import csv
with open('countries.csv', newline='') as csvfile:
 data = csv.reader(csvfile, delimiter='\t')
 for row in data:
   print(', '.join(row))
'''
country_id country_name region_id
AR Argentina 2
AU Australia 3
BE Belgium 1
BR Brazil 2
CA Canada 2
CH Switzerland 1
CN China 3
DE Germany 1
DK Denmark 1
EG Egypt 4
FR France 1
HK HongKong 3
IL Israel 4
IN India 3
IT Italy 1
JP Japan 3
KW Kuwait 4
MX Mexico 2
NG Nigeria 4
N Netherlands 1
SG Singapore 3
UK United Kingdom 1
US United States of America 2
ZM Zambia 4
ZW Zimbabwe 4
'''

# 3. Write a Python program to read a given CSV file as a list.
import csv
with open('employees.csv', newline='') as f:
   reader = csv.reader(f)
   data_list = list(reader)
print(data_list)
'''
employ_id,first_name,last_name,email,phone_number,hire_date,job_id,salary,commission_pct,manager_id,department_id
100,Steven,King,SKING,515.123.4567,1987-06-17,AD_PRES,24000,,,90
101,Neena,Kochhar,NKOCHHAR,515.123.4568,1987-06-18,AD_VP,17000,,100,90
102,Lex,De Haan,LDEHAAN,515.123.4569,1987-06-19,AD_VP,17000,,100,90
103,Alexander,Hunold,AHUNOLD,590.423.4567,1987-06-20,IT_PROG,9000,,102,60
104,Bruce,Ernst,BERNST,590.423.4568,1987-06-21,IT_PROG,6000,,103,60
105,David,Austin,DAUSTIN,590.423.4569,1987-06-22,IT_PROG,4800,,103,60
106,Valli,Pataballa,VPATABAL,590.423.4560,1987-06-23,IT_PROG,4800,,103,60
107,Diana,Lorentz,DLORENTZ,590.423.5567,1987-06-24,IT_PROG,4200,,103,60
108,Nancy,Greenberg,NGREENBE,515.124.4569,1987-06-25,FI_MGR,12000,,101,100
109,Daniel,Faviet,DFAVIET,515.124.4169,1987-06-26,FI_ACCOUNT,9000,,108,100
110,John,Chen,JCHEN,515.124.4269,1987-06-27,FI_ACCOUNT,8200,,108,100
111,Ismael,Sciarra,ISCIARRA,515.124.4369,1987-06-28,FI_ACCOUNT,7700,,108,100
112,Jose Manuel,Urman,JMURMAN,515.124.4469,1987-06-29,FI_ACCOUNT,7800,,108,100
113,Luis,Popp,LPOPP,515.124.4567,1987-06-30,FI_ACCOUNT,6900,,108,100
114,Den,Raphaely,DRAPHEAL,515.127.4561,1987-07-01,PU_MAN,11000,,100,30
115,Alexander,Khoo,AKHOO,515.127.4562,1987-07-02,PU_CLERK,3100,,114,30
116,Shelli,Baida,SBAIDA,515.127.4563,1987-07-03,PU_CLERK,2900,,114,30
117,Sigal,Tobias,STOBIAS,515.127.4564,1987-07-04,PU_CLERK,2800,,114,30
118,Guy,Himuro,GHIMURO,515.127.4565,1987-07-05,PU_CLERK,2600,,114,30
119,Karen,Colmenares,KCOLMENA,515.127.4566,1987-07-06,PU_CLERK,2500,,114,30
120,Matthew,Weiss,MWEISS,650.123.1234,1987-07-07,ST_MAN,8000,,100,50
121,Adam,Fripp,AFRIPP,650.123.2234,1987-07-08,ST_MAN,8200,,100,50
122,Payam,Kaufling,PKAUFLIN,650.123.3234,1987-07-09,ST_MAN,7900,,100,50
123,Shanta,Vollman,SVOLLMAN,650.123.4234,1987-07-10,ST_MAN,6500,,100,50
124,Kevin,Mourgos,KMOURGOS,650.123.5234,1987-07-11,ST_MAN,5800,,100,50
125,Julia,Nayer,JNAYER,650.124.1214,1987-07-12,ST_CLERK,3200,,120,50
126,Irene,Mikkilineni,IMIKKILI,650.124.1224,1987-07-13,ST_CLERK,2700,,120,50
127,James,Landry,JLANDRY,650.124.1334,1987-07-14,ST_CLERK,2400,,120,50
128,Steven,Markle,SMARKLE,650.124.1434,1987-07-15,ST_CLERK,2200,,120,50
129,Laura,Bissot,LBISSOT,650.124.5234,1987-07-16,ST_CLERK,3300,,121,50
130,Mozhe,Atkinson,MATKINSO,650.124.6234,1987-07-17,ST_CLERK,2800,,121,50
131,James,Marlow,JAMRLOW,650.124.7234,1987-07-18,ST_CLERK,2500,,121,50
132,TJ,Olson,TJOLSON,650.124.8234,1987-07-19,ST_CLERK,2100,,121,50
133,Jason,Mallin,JMALLIN,650.127.1934,1987-07-20,ST_CLERK,3300,,122,50
134,Michael,Rogers,MROGERS,650.127.1834,1987-07-21,ST_CLERK,2900,,122,50
135,Ki,Gee,KGEE,650.127.1734,1987-07-22,ST_CLERK,2400,,122,50
136,Hazel,Philtanker,HPHILTAN,650.127.1634,1987-07-23,ST_CLERK,2200,,122,50
137,Renske,Ladwig,RLADWIG,650.121.1234,1987-07-24,ST_CLERK,3600,,123,50
138,Stephen,Stiles,SSTILES,650.121.2034,1987-07-25,ST_CLERK,3200,,123,50
139,John,Seo,JSEO,650.121.2019,1987-07-26,ST_CLERK,2700,,123,50
140,Joshua,Patel,JPATEL,650.121.1834,1987-07-27,ST_CLERK,2500,,123,50
141,Trenna,Rajs,TRAJS,650.121.8009,1987-07-28,ST_CLERK,3500,,124,50
142,Curtis,Davies,CDAVIES,650.121.2994,1987-07-29,ST_CLERK,3100,,124,50
143,Randall,Matos,RMATOS,650.121.2874,1987-07-30,ST_CLERK,2600,,124,50
144,Peter,Vargas,PVARGAS,650.121.2004,1987-07-31,ST_CLERK,2500,,124,50
145,John,Russell,JRUSSEL,011.44.1344.429268,1987-08-01,SA_MAN,14000,0.4,100,80
146,Karen,Partners,KPARTNER,011.44.1344.467268,1987-08-02,SA_MAN,13500,0.3,100,80
147,Alberto,Errazuriz,AERRAZUR,011.44.1344.429278,1987-08-03,SA_MAN,12000,0.3,100,80
148,Gerald,Cambrault,GCAMBRAU,011.44.1344.619268,1987-08-04,SA_MAN,11000,0.3,100,80
149,Eleni,Zlotkey,EZLOTKEY,011.44.1344.429018,1987-08-05,SA_MAN,10500,0.2,100,80
150,Peter,Tucker,PTUCKER,011.44.1344.129268,1987-08-06,SA_REP,10000,0.3,145,80
'''

# 4. Write a Python program to read a given CSV file as a dictionary. 
data = csv.DictReader(open("departments.csv"))
print("CSV file as a dictionary:\n")
for row in data:
   print(row)
'''
department_id, department_name,  manager_id,  location_id
10, Administration, 200, 1700
20, Marketing, 201, 1800
30, Purchasing, 114, 1700
40, Human Resources, 203, 2400
50, Shipping, 121, 1500
60, IT, 103, 1400
70, Public Relations, 204, 2700
80, Sales, 145, 2500
'''

# 5. Write a Python program to read a given CSV files with initial spaces after a delimiter and remove those initial spaces. 
print("\nWith initial spaces after a delimiter:\n")
with open('departments.csv', 'r') as csvfile:
   data = csv.reader(csvfile, skipinitialspace=False)
   for row in data:
     print(', '.join(row))
print("\n\nWithout initial spaces after a delimiter:\n")
with open('departments.csv', 'r') as csvfile:
   data = csv.reader(csvfile, skipinitialspace=True)
   for row in data:
     print(', '.join(row))
'''
CSV REFER DEPTARTMENT
'''

# 6. Write a Python program that reads a CSV file and remove initial spaces, quotes around each entry and the delimiter. 
csv.register_dialect('csv_dialect',
                     delimiter='|',
                     skipinitialspace=True,
                     quoting=csv.QUOTE_ALL)
with open('temp.csv', 'r') as csvfile:
   reader = csv.reader(csvfile, dialect='csv_dialect')
   for row in reader:
       print(row)
'''
"country_id"|"country_name"|"region_id"
"AR"|"Argentina"| 2
"AU"|"Australia"| 3
"BE"|"Belgium"| 1
"BR"|"Brazil"| 2
"CA"|"Canada"| 2

'''

# 7. Write a Python program to read specific columns of a given CSV file and print the content of the columns. 
with open('departments.csv', newline='') as csvfile:
 data = csv.DictReader(csvfile)
 print("ID Department Name")
 print("---------------------------------")
 for row in data:
   print(row['department_id'], row['department_name'])
'''
department_id,department_name,manager_id,location_id
10,Administration,200,1700
20,Marketing,201,1800
30,Purchasing,114,1700
40,Human Resources,203,2400
50,Shipping,121,1500
60,IT,103,1400
70,Public Relations,204,2700
80,Sales,145,2500
90,Executive,100,1700
100,Finance,108,1700
110,Accounting,205,1700
120,Treasury,,1700
130,Corporate Tax,,1700
140,Control And Credit,,1700
150,Shareholder Services,,1700
160,Benefits,,1700
170,Manufacturing,,1700
180,Construction,,1700
190,Contracting,,1700
200,Operations,,1700
210,IT Support,,1700
220,NOC,,1700
230,IT Helpdesk,,1700
240,Government Sales,,1700
250,Retail Sales,,1700
260,Recruiting,,1700
270,Payroll,,1700
'''

# 8. Write a Python program that reads each row of a given csv file and skip the header of the file. Also print the number of rows and the field names. 
fields = []
rows = []
with open('departments.csv', newline='') as csvfile:
 data = csv.reader(csvfile, delimiter=' ', quotechar=',')
 # Following command skips the first row of the CSV file.
 fields = next(data)
 for row in data:
   print(', '.join(row))
print("\nTotal no. of rows: %d" % (data.line_num))
print('Field names are:')
print(', '.join(field for field in fields))
'''
CSV FILE SAME AS ABOVE
'''

# 9. Write a Python program to create an object for writing and iterate over the rows to print the values.
with open('temp.csv', 'wt') as f:
    writer = csv.writer(f)
    writer.writerow(('id1', 'id2', 'date'))
    for i in range(3):
        row = (
            i + 1,
            chr(ord('a') + i),
            '01/{:02d}/2019'.format(i + 1),)
        writer.writerow(row)
print(open('temp.csv', 'rt').read())

'''
"country_id"|"country_name"|"region_id"
"AR"|"Argentina"| 2
"AU"|"Australia"| 3
"BE"|"Belgium"| 1
"BR"|"Brazil"| 2
"CA"|"Canada"| 2

'''

# 10. Write a Python program to write a Python list of lists to a csv file. After writing the CSV file read the CSV file and display the content. 
data = [[10, 'a1', 1], [12, 'a2', 3], [
    14, 'a3', 5], [16, 'a4', 7], [18, 'a5', 9]]
with open("temp.csv", "w", newline="") as f:
   writer = csv.writer(f)
   writer.writerows(data)
with open('temp.csv', newline='') as csvfile:
 data = csv.reader(csvfile, delimiter=' ')
 for row in data:
   print(', '.join(row))
'''
CSV SAME AS ABOVE
'''

# 11. Write a Python program to write a Python dictionary to a csv file. After writing the CSV file read the CSV file and display the content. 
csv_columns = ['id', 'Column1', 'Column2', 'Column3', 'Column4', 'Column5']
dict_data = {'id': ['1', '2', '3'],
             'Column1': [33, 25, 56],
             'Column2': [35, 30, 30],
             'Column3': [21, 40, 55],
             'Column4': [71, 25, 55],
             'Column5': [10, 10, 40], }
csv_file = "temp.csv"
try:
   with open(csv_file, 'w') as csvfile:
       writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
       writer.writeheader()
       for data in dict_data:
           writer.writerow(dict_data)
except IOError:
   print("I/O error")
data = csv.DictReader(open(csv_file))
print("CSV file as a dictionary:\n")
for row in data:
   print(row)
'''
CSV SAME AS ABOVE
'''
