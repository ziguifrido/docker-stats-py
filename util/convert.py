def bytes_to_mb(bytes_value: int) -> float:
    return bytes_value / (1024 * 1024)

def bytes_to_gb(bytes_value: int) -> float:
    return bytes_value / (1024 * 1024 * 1024)

def bytes_to_string(bytes_value: int) -> str:
    mb_value = bytes_to_mb(bytes_value)
    return f"{mb_value:.2f}mb" if mb_value < 1024 else f"{bytes_to_gb(bytes_value):.2f}gb"

def values_to_percentage(value: int, max_value: int) -> str:
    percentage = (value * 100) / max_value
    return f"{percentage:.2f}%"
