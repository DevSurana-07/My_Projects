print("""
GST calculator  of electronic items :---
""")
a= int(input ("enter the price of the Television  : "))
a1=int(input ("enter the price of the mobile : "))
b=18/100
c = a*b
a2 = a1*b
e = a + c + a2
print("GST on television :  ",c)
print("GST on mobile :  ",a2)
print("total amount : ",e)
