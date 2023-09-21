gradus = float(input())

if gradus >= 26.00 and gradus <= 35.00:
    print ("Hot")
elif gradus >= 20.1 and gradus <= 25.9:
    print ("Warm")
elif gradus >= 15.00 and gradus <= 20.00:
    print ("Mild")
elif gradus >= 12.00 and gradus <= 14.9:
    print ("Cool")
elif gradus >= 5.00 and gradus <= 11.9:
    print ("Cold")
else:
    print("unknown")
