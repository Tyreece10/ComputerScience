def add_three(x, y, a):     #I created a function for adding the future 3 variables
    str(print(x + y + a))

int_1 = int(input("Give me one integer\n>"))     #I asked for the first number
int_1 = int(int_1)        #converted it to string
int_2 = int(input("Give me the second integer\n>"))      #Asked for second number
int_2 = int(int_2)        #converted
int_3 = int(input("Give me the third integer\n>"))           #third
int_3 = int(int_3)    #converted

add_three(int_1, int_2, int_3)     #Then I used he function to add the 3 int together
