#Amazon free shipping aliibilty system
#prime customers OR purchases of over $25
#under 18, you need parent consent to purchase

def free_shipping(prime, cost, age, consent):
    #You must be at least 18 year old and have 1 year of experience to be eligible
    if (prime == True or cost >= 25) and (age >= 18 or consent == True):
        print("Free shipping applied!")
    else:
        print("Ineligible for free shipping")


p = False
cos = 40
age = 55
con = False

free_shipping(p, cos, age, con)