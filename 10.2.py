name = input("Enter file:")
lst=[]
num=dict()
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    line.rstrip
    if not line.startswith("From "):
        continue
    else:
        words=line.split()
        wh=line.find(':')
        hold=line[wh-2:wh]
        if hold not in num:
            num[hold]=1
        else:
            num[hold]=num[hold]+1
for x in num:
    lst.append(x+" "+str(num[x]))
lst.sort()
count=0
for x in lst:
    print(lst[count])
    count=count+1