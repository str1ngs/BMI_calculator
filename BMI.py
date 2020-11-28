# A simple BMI calculator in imperial and metric system v.01
# @str1ngs

'''Less than 15 is Very severely underweight
#Between 15 and 16 Severely underweight
#Between 16 and 18.5 Underweight
#Between 18.5 and 25 Normal (healthy weight)
#Between 25 and 30 Overweight
#Between 30 and 35 Moderately obese
#Between 35 and 40 Severely obese
#Over 40 Very severely obese'''

measurement_system = str(input('Use Imperial or Metric measurement system: '))

if measurement_system == 'Imperial':
    weight_lbs = float(input('Enter weight in lbs: '))
    height_in = float(input('Enter height in in: '))

    def bmi_imperial(weight_lbs, height_in):
        bmi_imperial_value = 703 * weight_lbs / (height_in ** 2)
        print('Your BMI is: ', int(bmi_imperial_value))
    bmi_imperial(weight_lbs, height_in)

elif measurement_system == 'Metric':
    weight_kg = float(input('Enter weight in kg: '))
    height_m = float(input('Enter height in m: '))

    def bmi_metric(weight_kg, height_m):
        bmi_metric_value = weight_kg / (height_m ** 2)
        print('Your BMI is: ', int(bmi_metric_value))
    bmi_metric(weight_kg, height_m)

else:
    print('You need to type either Imperial or Metric')
