from src.is_number import IsNumber


def bmi_calc(body_mass, body_height):
    if (IsNumber(body_mass) and IsNumber(body_height)):
        body_mass=float(body_mass)
        body_height = float(body_height)
        if (body_mass > 0 and body_mass < 150 and body_mass != None):
            if (body_height > 0 and body_height < 2.5 and body_height != None):
                return body_mass / body_height ** 2
    return "Wrong value's: Please insert positive numbers. Weight in kg and Height in meters!"


def category_by_bmi(bmi_value):
    if not isinstance(bmi_value, (int, float)):
        return "bmi_value is not numeric."
    elif bmi_value < 0:
        return "bmi_value must be positive."
    elif bmi_value < 15:
        return "Very severely underweight"
    elif 16 > bmi_value >= 15:
        return "Severely underweight"
    elif 18.5 > bmi_value >= 16:
        return "Underweight"
    elif 25 > bmi_value >= 18.5:
        return "Normal"
    elif 30 > bmi_value >= 25:
        return "Overweight"
    elif 35 > bmi_value >= 30:
        return "Moderately obese"
    elif 40 > bmi_value >= 35:
        return "Severely obese"
    elif 45 > bmi_value >= 40:
        return "Very severely obese"
    elif 50 > bmi_value >= 45:
        return "Morbidly obese"
    elif 60 > bmi_value >= 50:
        return "Super obese"
    elif bmi_value >= 60:
        return "Hyper obese"
