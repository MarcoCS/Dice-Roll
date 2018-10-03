import string
def bizzBang(limit):
    for x in range(limit):
        if (x % 3 == 0) and (x % 5 != 0):  # Check if an even factor of 3 and not 5
            if str.lower(input("{} Bizz or bang?:".format(x))) == "bizz":
                print("good!")
            else:
                return("Wrong! game over")
        if (x % 5 == 0) and (x % 3 != 0): # check if an even factor of 5 and not 3
            if str.lower(input("{} Bizz or bang?:".format(x))) == "bang":
                print("good!")
            else:
                return("Wrong! game over")
                
        if (x % 3 == 0) and (x % 5 == 0): # Bizzbang condition check if both conditions are true
            if str.lower(input("{} Bizz or bang?:".format(x))) == "bizzbang":
                print("good!")
            else:
                return("Wrong! game over")
        print(x)
        
