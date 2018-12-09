print ("vvedite slovo ili frazu celikom")
s=input()
print ("vvedite smeshenie")
d=int(input())
out=""
i=0
while i<len(s):
  if s[i]==" ":
      out+=" "
  else:
    out+=chr(97+((ord(s[i])-97)+d)%26)
  i+=1
print(out)
