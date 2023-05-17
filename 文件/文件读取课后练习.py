""" f=open("D:/wangjiale.txt","r",encoding="utf-8")
passage=f.read()
num=passage.count("TheShy")
print(f"文中出现theshy的次数是{num}")
f.close() """

#方法2
count=0
f=open("D:/wangjiale.txt","r",encoding="utf-8")
for line in f:
    line=line.strip()
    words=line.split(" ")
    for word in words:
        if word=="TheShy":
            count+=1
print(f"文中出现TheShy的次数是{count}") 
f.close()