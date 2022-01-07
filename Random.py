#Python program to generate the random password
import random #to generate the random number we have use the built in library
password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz.@!#$%{}_"
pass_length=int(input("Enter the length of the password: "))
a = "".join(random.sample(password,pass_length))
print(f"Your random password is: {a}")