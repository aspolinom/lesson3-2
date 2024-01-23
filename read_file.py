gw = open('write_txt.txt','w')
a=[]
with open('text_read.txt', 'rt', encoding='utf-8') as f:
    data = f.read()
    stri1 = data.split('\t')
#    a.append(stri1)
    a=a+stri1
b=[]
for new in a:
    if len(new)!= 0:
        if new[-1]=='\n':
            new=new[0:-1]
    else:
        continue
    if new in b:
        continue
    else:
        b.append(new)
k=0
for stroca in b:
   gw.write('"'+stroca+'", ')
   k=k+1
   if k % 8==0:
       gw.write('\n')

print(b)
f.close
gw.close