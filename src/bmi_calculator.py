def bmi_calc(body_mass, body_height):
    return body_mass / body_height ** 2


def category_by_bmi(bmi_value):
    if bmi_value <= 0:
        return "Error"
    if bmi_value < 15:
        return "Very severely underweight"
    if 16 > bmi_value >= 15:
        return "Severely underweight"
    if 18.5 > bmi_value >= 16:
        return "Underweight"
    if 25 > bmi_value >= 18.5:
        return "Normal"
    if 35 > bmi_value >= 30:
        return "Moderately obese"
    if 40 > bmi_value >= 35:
        return "Severely obese"
    if 45 > bmi_value >= 40:
        return "Very severely obese"
    if 50 > bmi_value >= 45:
        return "Morbidly obese"
    if 60 > bmi_value >= 50:
        return "Super obese"
    if bmi_value >= 60:
        return "Hyper obese"
