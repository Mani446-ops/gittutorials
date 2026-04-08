for i in range(1,5):
    print(i)

list=[2,4,5,8]

for num in list:
    print(num)

string="Python"

for ch in string:
    print(ch)



i = 1

while i <= 5:
    print(i)
    i += 1





for i in range(1,11):
    if i %2==0:
        print(i)

total = 0

for i in range(1,6):
   
    total +=i
    print("Sum:", total)



for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end=" ")
    print()

for i in range(1,6):
    print("*" * i)

for i in range(1,10):
    if i == 5:
        break
    print(i)

for i in range(1,7):
    if i == 3:
        continue
    print(i)

numbers=[10,87,45,6,78]
largest=numbers[0]

for num in numbers:
    if num>largest:
        largest=num

print("Largest:",largest)

text="python programming"
count=0

for ch in text:
    if ch in 'aeiou':
        count +=1
print("Vowels:", count)

text = "python programming"

count = 0

for ch in text:
    if ch in "aeiou":
        count += 1

print("Vowels:", count)

total=0

for i in range(3):
    num=int(input("Enter number:"))
    total+=num
print("Total:", total)

