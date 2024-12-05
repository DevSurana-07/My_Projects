print("CALCULATION OF COMPOUND INTEREST :--\n")

p = int(input("enter the principal amount :--   "))
r = int(input("enter the monthly interest :--   "))
n = int(input("enter the compounded interest :--   "))
t = int(input("number of years:--   "))
a = 1
b = r/100
c = p*(a+b/n)**(n*t)
d = c-p 
print("THE TOTAL PAYABLE AMOUNT IS :--",c)
print("THE COMPOUND INTEREST IS :--",d)
