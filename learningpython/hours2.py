# Accept inputs on command line and perform a simple multiplication,
# if number of hours are greater than 40, then pay 1.5 times the rate for the additional hours,
# print the result to the screen.
# Uses Python 2.7.
hrs = float(raw_input("Enter Hours:"))
rate = float(raw_input("Enter Rate:"))
pay = 0.0
if hrs <= 40:
    pay = hrs * rate

if hrs > 40:
    pay = rate * 40 + (rate * 1.5 * (hrs - 40))
    
print pay