def isNum(data):
    try:
        int(data)
        return True
    except ValueError:
        return False