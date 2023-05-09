nums = [5, 2, 7, "50", False]

for el in nums:
    el *= 2
    print

n = int(input("Enter length: "))
user_list = []

i = 0
while i < n:
    string = "Enter element #" + str(i+1) + ":"
    user_list.append(input(string))
    i += 1
print(user_list)