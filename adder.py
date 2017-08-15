def adder():
	s=4
	y=3
	x = s + y
	return x 

#The function below stips information from Strings
def stripper():
    turtles="evryonelovesturtles"
    turtles.strip("s")
    r= turtles.strip("s")
    return r

print stripper()
        
#Function passes parameters to function. Appends data to list

def appendnumbertolist(number):
    eclipse = ["TN", "OK",]
    eclipse.append(number)
    return eclipse

print appendnumbertolist("Next Monday")


print adder()
