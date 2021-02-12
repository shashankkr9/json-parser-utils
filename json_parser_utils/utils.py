def safe_int(value):
    try:
        return int(float(value))
    except:
        return None
