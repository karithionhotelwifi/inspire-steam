# Name : Augustine Mwangi
# Date : 16/02/2026

# Program to do calculate factorials of numbers


number = int(input("Enter the number x : "))
factorial = 1 # initiate factorial on 1
for x in range (1, number+1) :
    factorial *= x

print (f"{number}! ={factorial}")