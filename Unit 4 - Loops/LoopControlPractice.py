for i in range(1,21):
    if i == 16:
        break
    print(i)

for i in range(1, 31):
    if i % 2 == 0:  # Check if the number is even
        continue    # Skip to the next iteration if it is
    print(i)        # Print the number if it's odd
print("--------------------------------------------------------------------------------------------------------------------")


for i in range(10, 1):
    if i == 5:
        break
    print(i)