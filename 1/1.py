list1 = []
list2 = []
with open("1/input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        num1, num2 = line.split("   ")
        list1.append(int(num1))
        list2.append(int(num2))
        
list1.sort()
list2.sort()

sum_of_distances = 0
for i, j in zip(list1, list2):
    sum_of_distances += abs(i - j)
print(sum_of_distances)
