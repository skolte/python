# Accept inputs on command line and perform a simple multiplication,
# if number of hours are greater than 40, then pay 1.5 times the rate for the additional hours,
# print the result to the screen.
# Refactored the operation into a separate method.
# Uses Python 2.7.
def computepay(h,r):
    if h > 40:
    	pay = 40 * r + (h - 40) * r * 1.5
    else:
    	pay = h * r
    return pay

hrs = float(raw_input("Enter Hours:"))
rate = float(raw_input("Enter Rate:"))
p = computepay(hrs,rate)
print p