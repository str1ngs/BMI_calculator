# This function uses the metric system for the formula

def bmi_metric(weight_kg, height_m):
    bmi_metric_value = weight_kg / (height_m ** 2)
    return bmi_metric_value


# This function uses the imperial system for the formula

def bmi_imperial(weight_lbs, height_in):
    bmi_imperial_value = 703 * weight_lbs / (height_in ** 2)
    return bmi_imperial_value


print("Select operation.")
print("1.Metric")
print("2.Imperial")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/: ")

    # Check if choice is one of the two options
    if choice in ('1', '2'):
        weight_kg = float(input("Enter kg : "))
        height_m = float(input("Enter m : "))

        if choice == '1':
            print(bmi_metric)
