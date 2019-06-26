# Lists

names = ['John', 'Bob', 'Sarah', 'Chris', 'Kyle']
print(names)
print(names[2])
print(names[-2])
print(names[2:])
print(names[2:4])

names[0]= 'Jon'
print(names)
print('\n')


numbers = [3,6,2,8,4,10] #largest number is 10 in the numbers list.
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)