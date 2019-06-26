#List Methods

numbers = [5,2,1,7,4]
numbers2 = numbers.copy()

print(f"original: {numbers}")
numbers.insert(0, 10)
print(numbers)

print("\n")

numbers.pop()
print(numbers)


number = [2,2,4,6,3,4,6,1]
uniques = []
for num in number:
    if num not in uniques:
        uniques.append(num)
print(uniques)