name = input("Enter file:")
num=dict()
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    for letter in line:
        if letter.isalpha() and letter not in num:
            num[letter]=1
        elif letter.isalpha():
            num[letter]=num[letter]+1
hold=list()
for a, b in num.items():
    hold.append( (b,a) )
hold=sorted(hold,reverse=True)
print(hold)