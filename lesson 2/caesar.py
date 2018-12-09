alph=[]
n=97
while n<=122:
    alph+=[n]
    n+=1
print (alph)
print (len(alph))
new_alph=[]
d=2
i=0
while i<len(alph):
    new_alph+=[alph[(i+d)%26]]
    i+=1
print (new_alph)
