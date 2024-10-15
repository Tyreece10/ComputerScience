#Amazon free shipping aliibilty system
#prime customers OR purchases of over $25
#under 18, you need parent consent to purchase

def free_shipping(prime, cost, age, consent):
    # Check eligibility for free shipping
    if (prime or cost >= 25) and (age >= 18 or consent):
        return "Free shipping applied!"
    else:
        return "Ineligible for free shipping"

# Collect input and convert to appropriate types
p = input("Are you a prime member? (yes/no)\n>").lower() == "yes"
cos = int(input("How much have you purchased of items?\n>"))
age = int(input("How old are you?\n>"))
con = input("Do you have consent? (yes/no)\n>").lower() == "yes"

# Call the function and print the result
print(free_shipping(p, cos, age, con))