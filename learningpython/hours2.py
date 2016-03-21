hrs = float(raw_input("Enter Hours:"))
rate = float(raw_input("Enter Rate:"))
pay = 0.0
if hrs <= 40:
    pay = hrs * rate

if hrs > 40:
    pay = rate * 40 + (rate * 1.5 * (hrs - 40))
    
print pay