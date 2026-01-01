# Quick Quiz: Write a program to print the content of a list.

my_list = [1,"Mary","Girl",2,3,4,7]
print("\nList")
print(my_list)

print("\nContents of List")
print(*my_list)

print("\nContents of List using sep")
print(*my_list, sep=", ")

# Quick Quiz: Write a program to print the content of a list using while and for loops.

for i in range(len(my_list)):
    print(my_list[i])

i = 0
while(i < len(my_list)):
    print(my_list[i])
    i+=1