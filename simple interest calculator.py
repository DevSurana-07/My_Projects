print("""Simple Interest calculator :--
""")

P = int(input("ENTER THE PRINCIPAL AMOUNT :--  "))
r = int(input("ENTER THE MONTHLY INTEREST RATE :-- "))
t = int(input("ENTER THE YEARS :---  "))
a =P* r * t /100
print("""
THE SIMPLE INTEREST IS  :-- """,
a)
