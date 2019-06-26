#Keyword Arguments
# parameters
def greet_user(first_name, last_name):
    print(f'Hi there {first_name} {last_name}!')
    print('Welcome aboard')

print("Start")
greet_user(last_name = "Smith", first_name = "John") # keyword arguments
greet_user("Mary","Johnson") # positional arguments
print("Finish")