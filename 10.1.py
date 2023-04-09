name = input("Enter file:")
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
        hold=words[1]
        if hold not in num:
            num[hold]=1
        else:
            num[hold]=num[hold]+1
hold=list()
for a, b in num.items():
    hold.append( (b,a) )
hold=sorted(hold,reverse=True)
print(hold[0])