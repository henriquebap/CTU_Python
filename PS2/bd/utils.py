def get_float(value):
    try:
        result = float(value)
        return result
    except ValueError:
        return
    
def get_int(value):
    try:
        result = int(value)
        return result
    except ValueError:
        return
