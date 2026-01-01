# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]

l = ["Harry", "Soham", "Sachin", "Rahul"]

for i in l:
    if i.lower().startswith("s"):
        print(f"Welcome dear, {i}!")
        
for i in l:
    if i.startswith("S"):
        print(f"Welcome dear, {i}!")