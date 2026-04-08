list = [1,2,3,4]
print(list[2])

tuple = (1,2,3,5) 
print(tuple[1])

set={1,2,3,4,5}
print(set)

dict = {
    "name":"Rajesh",
    "age":26,
    "Profession":"SAP Developer"
}
print(dict["age"])

cities = ["Mumbai","Delhi","Hyd","Bang"]
print(cities)
cities.append("Chennai")
print(cities)
cities.remove("Hyd")
print(cities)

diminesions=[1234,7895]
width=diminesions[1]
length=diminesions[0]
print(width,length)

skills={"python", "AI", "GenAI", "MLOps"}
skills.add("docker")
print("skills")

students=[
    {"name":"Mani","age":34},
    {"name":"Rajesh","age":78},
    {"name":"manoj","age":54}
]


for student in students:
    print(student["name"],student["age"])

numbers=[1,5,2,6,9,4]
largest_number=max(numbers)
print("Largest_number:",largest_number)

tuple=("white","red","black")
print(tuple[1])

set={1,3,2,5,2,3,6,7}
unique_numbers=print(set)

car={
    "brand":"tata",
    "model":2026,
    "colour":"black"
    }

print(car["model"])

marks=[23,57,89,43,67]

print("Highest marks:", max(marks))
print("Lowest marks:",min(marks))

for mark in marks:
    if mark>=80:
        print("Excellent",mark)

list=[23,56,78,56,90,56]
unique_numbers=[]
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(unique_numbers)

employe=("rajesh",26,"SAP Developer")
name,age,job=employe
print("Name:",name)
print("age:",age)
print("Job:",job)

students={
    "Raj":{"math":56,"science":67},
    "Satish":{"math":67,"science":89}
}

for student,marks in students.items():
    total=marks["math"]+marks["science"]
    print("student","total_marks:",total)

employees=[
    {"name":"rajesh","salary":56000},
    {"name":"kishore","salary":84000},
    {"name":"ashiq","salary":89000}   
]

highest_salary=0
top_employe=""

for emp in employees:
    if emp["salary"]>highest_salary:
        highest_salary=emp["salary"]
        top_employe=emp["name"]

print("highest_salary:",highest_salary,top_employe)
        


    