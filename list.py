num=[1,2,3]
names=["Anil", "Vamsi", "Vishnu"]
mixed=["Manoj", 1, 3, "Enoch"]

print(num[0])
print(names[1])
print(mixed[3])
names[1]="Rahul"
print(names)

numbers=[10,50,80]
numbers.append(34)
print(numbers)
numbers.insert(1,30)
print(numbers)
numbers.remove(80)
numbers.pop(1)
print(numbers)

names=["Anil","Vaibhav","Manoj"]

for name in names:
    print(name)

print("Anil" in names)

numbers=[6,2,9]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
print(numbers[0:2])

num=[2,5,6,3,8,9]
print(num[-1])
print(num[1:3])
print(num[:3])
print(num[2:])

a=[1,2,3,4]
b=a.copy()

matrix=[
    [2,3],
    [6,7]
]

print(matrix[0][1])
marks=[]
marks.append(30)
marks.append(50)
marks.append(60)
print("Total marks:", sum(marks))
print("Average marks:", sum(marks)/len(marks))

colors=["Red","Pink","Green","Yellow"]
print(colors)
print(colors[1:3])
colors[2]="Grey"
print(colors[-1])
tasks=[]
tasks.append("Learn Python")
tasks.append("Add git")
print(tasks)

tasks.insert(1,"Learn Git")
print(tasks)
tasks.pop()
print(tasks)

students=["Mani","Manoj","Murali"]
for student in students:
    print("student:", student)

numbers=list(range(1,6))
print(numbers)