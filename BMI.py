# A simple BMI calculator in imperial and metric system v.01
# @str1ngs

measurement_system = str(input('Use Imperial or Metric measurement system: '))

if measurement_system == 'Imperial':
    weight_lbs = float(input('Enter weight in lbs: '))
    height_in = float(input('Enter height in in: '))

    def bmi_imperial(weight_lbs, height_in):
        bmi_imperial_value = int(703 * weight_lbs / (height_in ** 2))
        print('Your BMI score is: {0}' .format(bmi_imperial_value), end='')
        if 15 > bmi_imperial_value:
            print(', which is severely underweight.')
        elif 15 < bmi_imperial_value < 18.5:
            print(', which is underweight.')
        elif 18.5 < bmi_imperial_value < 25:
            print(', which is a healthy weight.')
        elif 25 < bmi_imperial_value < 30:
            print(', which is overweight.')
        elif 30 < bmi_imperial_value < 35:
            print(', which is moderately obese.')
        elif 35 < bmi_imperial_value < 40:
            print(', which is severely obese.')
        elif 40 <= bmi_imperial_value:
            print(', which is very severely obese.')
    bmi_imperial(weight_lbs, height_in)

elif measurement_system == 'Metric':
    weight_kg = float(input('Enter weight in kg: '))
    height_m = float(input('Enter height in m: '))

    def bmi_metric(weight_kg, height_m):
        bmi_metric_value = int(weight_kg / (height_m ** 2))
        print('Your BMI score is: {0} ' .format(bmi_metric_value), end='')
        if 15 > bmi_metric_value:
            print(', which is severely underweight.')
        elif 15 < bmi_metric_value < 18.5:
            print(', which is underweight.')
        elif 18.5 < bmi_metric_value < 25:
            print(', which is a healthy weight.')
        elif 25 < bmi_metric_value < 30:
            print(', which is overweight.')
        elif 30 < bmi_metric_value < 35:
            print(', which is moderately obese.')
        elif 35 < bmi_metric_value < 40:
            print(', which is severely obese.')
        elif 40 <= bmi_metric_value:
            print(', which is very severely obese.')
    bmi_metric(weight_kg, height_m)

else:
    print('You need to type either Imperial or Metric!')
