import time

#stat changable ;)
number_of_digit = 4

#user password
password = input(f"\nenter a {number_of_digit} digit password.\n>  ")


while len(str(password)) != number_of_digit or type(password) != int:
    if len(password) != number_of_digit:
        password = input(f"\nenter a {number_of_digit} digit password.\n\nthis is not a {number_of_digit} digit password. please try again.>  ")
    elif type(password) != int:
        try:
            password = int(password)
        except ValueError:
            print("\nyour password must only be with digit (0-9), try again.")
            password = input(f"\nenter a {number_of_digit} digit password.\n>  ")
    
    
            

      
    

password = int(password)
#guessing
start = time.time()
guess_password = 0
while guess_password != password:
    guess_password += 1
end = time.time()
totaltime = end - start

#showing founded password
guess_password = str(guess_password)
for i in range(number_of_digit-len(guess_password)):
    guess_password = f"0{guess_password}"
print(f"found it in {totaltime:.6f} sec! your password is {guess_password}")