print(range(5))
# Output: range(0, 5)
# Because range(5) is a range object, not the actual values.

print("\n")

print(*range(5))
# The * (asterisk) unpacks the range object into individual numbers.
# So this becomes: print(0, 1, 2, 3, 4)
# Output: 0 1 2 3 4

print("\n")


print(*range(5), end=",")
# print() is called ONLY ONCE.
# All values are printed in one line.
# end="," means: after EVERYTHING is printed, add a comma once.
# Output: 0 1 2 3 4,

print("\n")

print(*range(5), sep=",")
# The * unpacks the range object into individual numbers.
# sep="," means: put a comma BETWEEN each number, not before or after, but only in MIDDLE.
# Output: 0,1,2,3,4

print("\n")

for i in range(5):
    print(i, end=",")
# print() is called MULTIPLE TIMES (once per loop iteration).
# end="," runs every time print() is called.
# So after EACH number, a comma is added.
# Output: 0,1,2,3,4,

print("\n")

for i in range(5):
    print(i, end=" ")