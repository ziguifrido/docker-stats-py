def bytes_to_mb(bytes_value: int) -> float:
    """Convert bytes to megabytes."""
    if bytes_value == 0 or bytes_value is None:
        return 0.0

    return bytes_value / (1024 * 1024)

def bytes_to_gb(bytes_value: int) -> float:
    """Convert bytes to gigabytes."""
    if bytes_value == 0 or bytes_value is None:
        return 0.0

    return bytes_value / (1024 * 1024 * 1024)

def bytes_to_string(bytes_value: int) -> str:
    """Convert bytes to a human-readable string."""
    if bytes_value == 0 or bytes_value is None:
        return "0.00mb"

    mb_value = bytes_to_mb(bytes_value)

    # Returns a human-readable string representation of the bytes value, mb or gb denpending on the value.
    return f"{mb_value:.2f}mb" if mb_value < 1024 else f"{bytes_to_gb(bytes_value):.2f}gb"

def values_to_percentage(used_value: int, max_value: int) -> str:
    """Convert used and max values to a percentage string."""
    if max_value == 0 or max_value is None:
        return "0%"

    percentage = (used_value * 100) / max_value

    return f"{percentage:.2f}%"
