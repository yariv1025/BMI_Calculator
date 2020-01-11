def IsNumber(value):
    try:
        float(value)
        return True
    except ValueError and TypeError:
        return False
