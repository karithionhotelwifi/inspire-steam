# Name : Augustine Mwangi
# Date : 11/02/2026

# String formating


sentence = "I watch anime"

string_length = len(sentence)

print(f"The length is: {string_length}")

#Spliting a string
sentence_2= "Mathematics Physics"
split = sentence_2.split(" ")

print(f"the first subject is:", split[1])

# Make everything CAPS
mpesa_code = "UABCJ67DDSFHG"

lowercase = mpesa_code.lower()

print(f"New mpesa_code: {lowercase}")

# Replacing characters in a string

balance = "100 Kes"
amount_added = "50 Kes"

cleaned_balance = balance.replace("Kes", "") 

print(f"Cleaned_balance:{cleaned_balance}")

cleaned_amount_added = amount_added.replace("Kes", "")

print(f"cleaned_amount_balance: {cleaned_amount_added}")

new_balance = int(cleaned_balance) + int(cleaned_amount_added)

print(f"the new balance is: {new_balance}")

# Assignment
sentence_3 = "CONFIRMED You have Received 40Kes From Phillip"

split = sentence_3.split(" ")
print(f"New Mpesa text is:" , split[4],)


balance = "12.02Kes"
amount_added = "40Kes"
cleaned_balance =balance.replace ("Kes", "")
print(f"cleaned_balance:{cleaned_balance}")

cleaned_amount_added =amount_added.replace ("Kes", "")
print(f"cleaned_amount_added:{cleaned_amount_added}")

new_balance = float(cleaned_balance) + int(cleaned_amount_added)

print(f"new_balance is: {new_balance}")