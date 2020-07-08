# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(no):
    if no % 2 == 0:
        return True
    else:
        return False 

while True:
# Read a number from the keyboard
    num = input("Enter a number: ")
    num = num

    # Print out "Even!" if the number is even. Otherwise print "Odd"
    if num == "bye":
        break
    elif num.isdigit() == False:
        print("Are you playing games? I said enter a number!!!")
    elif is_even(int(num)) == True:
        print("Even!")
    elif is_even(int(num)) == False:
        print("Odd!")
    # else:
    #     print("Are you playing games? I said enter a number!!!")
        continue

# YOUR CODE HERE

