def bytes_to_mb(bytes_value):
    return bytes_value / (1024 * 1024)

def bytes_to_gb(bytes_value):
    return bytes_value / (1024 * 1024 * 1024)

def bytes_to_string(bytes_value):
    mb_value = bytes_to_mb(bytes_value)
    return f"{mb_value:.2f}mb" if mb_value < 1024 else f"{bytes_to_gb(bytes_value):.2f}gb"

def values_to_percentage(value, max_value):
    percentage = (value * 100) / max_value
    return f"{percentage:.2f}%"
