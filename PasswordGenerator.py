
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password=""
ran_pass=''
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?:")) 
nr_symbols = int(input(f"How many symbols would you like?:"))
nr_numbers = int(input(f"How many numbers would you like?:"))
random_letter=''
random_number=''
random_symbol=''
for i in range(1,nr_letters+1):
    random_letter = random.choice(letters)  
    password+=random_letter
for i in range(1,nr_symbols+1):
    random_number=random.choice(numbers)
    password+=random_number
for i in range(1,nr_numbers+1):
    random_symbol=random.choice(symbols)
    password+=random_symbol

random_passwords_list=list(password)
for i in range(1,len(password)):
    random_password=random.choice(random_passwords_list)
    ran_pass+=random_password
print(f'Your password is:{ran_pass}')


    
