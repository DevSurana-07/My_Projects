print(""" EMI calculator :----
""")
P = int(input("enter the loan amount :-  "))
a = int(input("enter the monthly interest on the product :- "))
N= int(input("enter the tenure in months :-  "))
R = a/100
b = 1
c = float(P * R )* (b+R)**(N)/(b+R)**(N-b)
print("The total amount of the emi :-  ",c)



