def get_file_content(file_path):
    try:
        with open(file_path) as tmp:
            content = tmp.readlines()
        return content
    except FileNotFoundError:
        return


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
