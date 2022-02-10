hours = float(input("enter hours here"))
rate = float(input("enter hourly pay here"))
overtime = hours-40 
if hours <= 40:
    print (hours*rate)
else:
    print (float(40*rate)+float(overtime*(rate*1.5)))
