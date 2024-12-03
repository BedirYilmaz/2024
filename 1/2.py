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

frequencies = {}
for i in range(len(list1)):
    frequencies[list1[i]] = list2.count(list1[i])

similarity_score = 0
for key, value in frequencies.items():
    similarity_score += key * value

print(similarity_score)