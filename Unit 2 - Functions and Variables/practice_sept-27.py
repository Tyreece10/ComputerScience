def add(x, y):      #function
    print(x + y)

add(4, 2)
add(16, 10)     #replaces x to 16 and y to 10)

num_1 = int(input("Whats the first number\n>"))
num_2 = int(input("Whats the second number?\n>"))

add(num_1, num_2)

def top_five_movies(movie_1, movie_2, movie_3, movie_4, movie_5):
    print("1. "+movie_1)
    print("2. "+movie_2)        #Local variable
    print("3. "+movie_3)
    print("4. "+movie_4)
    print("5. "+movie_5)

top_five_movies("Spider 1", "Spiderman2", "Spider3", "Spdier4", "SpiderMan5")

movie_1 = input("Whats your 1st favorite movie?\n>")        #Global Variable
movie_2 = input("Whast you 2nd favorite movie?\n>")     #Not the same as local
movie_3 = input("Whats your 3rd favorite movie?\n>")
movie_4 = input("whats your 4th favorite movie?\n>")
movie_5 = input("What your 5th favorite movie?\n>")

top_five_movies()


x = 4
def my_function():
    global x #Global x not local x
    x = 5   #Changes the Global x to 5
    print(x)


    my_function()   #prints 5
    print(x)        #prints 4