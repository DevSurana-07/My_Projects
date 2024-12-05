print("""Welcome to the Interactive Personal Data Collector !

""")

a= str(input("Please enter your name :  "))
b = int(input("Please enter your age:  "))
c = float(input("Please enter your height in meters:  "))
d = int(input("Please enter your favourite number:  "))
print("""
Thank you ! Here is the information we collected :
""")

print("Name :  ", a ," , Type:",(type( a ))," , Memory Address: " ,(id( a )))
print("Age  :  ", b ," , Type:",(type( b ))," , Memory Address: " ,(id( b )))
print("Height  :  ", c ," , Type:",(type( c ))," , Memory Address: " ,(id( c )))
print("Favourite Number  :  ", d ," , Type:",(type( d ))," , Memory Address: " ,(id( d )))
e = 2024
f = e - b
print("""
Your birth year is approximately : " ,  "" (based on your age of 18)
""",f)
print("""
Thank you for choosing the Personal Data Collector.  Goodbye !
""")
