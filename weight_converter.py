# exercise from Youtube tutorial

weight = float(input("Weight: "))
unit = str(input("(K)g or (L)bs: "))
if unit.upper() == "K":  # previously had 'or k', but changed to use .upper
    print("Weight in (L)bs:", (round(float(weight * 2.2), 2)))
elif unit.upper() == "L":
    print("Weight in (K)g:", (round(float(weight * 0.45), 2)))  # added float and round to add decimal number
