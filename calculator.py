# import arithmetic.py
import arithmetic

def main():
    # begin program
    print "This math calculator uses prefix notation. For example in prefix notation,"
    print "the same statement would be written '+ 3 2' or '* 4 4'."
    print "You can use +, -, *, /, square, cube, pow, or mod for calculation."
    print "To exit the calculator, press CTRL + D."
    
    # using while loop for calculation
    while True:
        # using try & except to catch errors
        try:
            # get input from user
            math_input = raw_input("> ")
            # creates an empty array
            array = []
            # separating the values given from user and inserting them to the array
            array = math_input.split(" ")
            # assigning array[0] to character
            character = str(array[0])
            # assigning array[1] to num1
            num1 = int(array[1])
            # checking for a third value
            if len(array) == 3:
                # assigning array[2] to num2
                num2 = int(array[2])
            # using try & except to catch any errors from user's inputs
            if character == "+" or "-" or "*" or "/" or "square" or "cube" or "pow" or "mod" and len(array) == 2 or 3:
                try:
                    # if statements for all kinds of calculation
                    if character == "+":
                        print arithmetic.add(num1,num2)
                        #break
                    elif character == "-":
                        print arithmetic.subtract(num1,num2)
                        #break
                    elif character == "*":
                        print arithmetic.multiply(num1,num2)
                        #break
                    elif character == "/":
                        print arithmetic.divide(num1,num2)
                        #break
                    elif character == "square":
                        # check for only one value needed for square
                        if len(array) > 2:
                            print "Sorry, square can only accept one number."
                            #break
                        else:
                            print arithmetic.square(num1)
                            #break
                    elif character == "cube":
                        # check for only one value needed for cube
                        if len(array) > 2:
                            print "Sorry, cube can only accept one number."
                            #break
                        else:
                            print arithmetic.cube(num1)
                            #break
                    elif character == "pow":
                        print arithmetic.power(num1,num2)
                        #break
                    elif character == "mod":
                        print arithmetic.mod(num1,num2)
                        #break
                    else:
                        print "Sorry, I do not understand. Please give me a mathematical character for calculation."
                        #break
                except UnboundLocalError:
                    print "Sorry, please enter the correct format for prefix notation calulation."
                    print "Or enter only two numbers after the prefix."
                    #break
        except IndexError:
            print "Sorry, please enter only up to one character and two numbers."

if __name__ == '__main__':
    main()