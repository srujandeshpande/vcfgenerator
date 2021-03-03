import csv
delimiter = ','
filename = 'res.csv'

with open(filename, newline='') as f:
    reader = csv.reader(f, delimiter=delimiter)
    data = list(reader)

print(data)
vd = ""
for i in data:
    vd+="BEGIN:VCARD\nVERSION:3.0\nREV:2021-02-24 09:56:28\n"
    vd+="EMAIL;TYPE=internet,pref:"+i[1]+"\n"
    vd+="NICKNAME:"+i[2]+"\n"
    vd+="TEL;TYPE=cell,voice:"+i[4]+"\n"
    vd+="ORG:IO2\n"
    vd+="N:;"+i[3]+";;;;\n"
    vd+="FN:"+i[3]+"\n"
    vd+="END:VCARD\n"


with open('out.vcf', "w") as f:
    f.write(vd)





# BEGIN:VCARD
# VERSION:3.0
# REV:2021-02-24 09:56:28
# PRODID:-//class_vcard from thewebvendor.com//NONSGML Version 1//EN
# EMAIL;TYPE=internet,pref:
# NICKNAME:PES2UG20CS401
# TEL;TYPE=cell,voice:7337677575
# ORG:IO2
# N:;Zain;;;;
# FN:Zain 
# END:VCARD
