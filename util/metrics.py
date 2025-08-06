from util import convert

def calculate_cpu_usage(current_stats: dict, previous_stats: dict) -> str:
    """Calculate CPU usage percentage between two stats snapshots"""
    cpu_stats = current_stats.get('cpu_stats', {})
    precpu_stats = previous_stats.get('cpu_stats', {})

    cpu_delta = cpu_stats.get('cpu_usage', {}).get('total_usage', 0) - precpu_stats.get('cpu_usage', {}).get('total_usage', 0)
    system_cpu_delta = cpu_stats.get('system_cpu_usage', 0) - precpu_stats.get('system_cpu_usage', 0)
    number_cpus = cpu_stats.get('online_cpus', 0)

    # Calculate CPU usage percentage
    cpu_usage = (cpu_delta / system_cpu_delta) * number_cpus * 100.0 if system_cpu_delta > 0 else 0.0

    return f"{cpu_usage:.2f}%"

def calculate_memory_usage(stat: dict) -> str:
    """Calculate memory usage percentage."""
    memory_usage = stat.get('memory_stats', {}).get('usage', 0)
    memory_limit = stat.get('memory_stats', {}).get('limit', 0)

    memory_usage_str = convert.bytes_to_string(memory_usage)
    memory_limit_str = convert.bytes_to_string(memory_limit)
    memory_percentage_str = convert.values_to_percentage(memory_usage, memory_limit)

    return f"{memory_percentage_str} - {memory_usage_str}/{memory_limit_str}"

def calculate_network_io(current_stats: dict, previous_stats: dict) -> str:
    """Calculate network I/O rates between two stats snapshots"""
    current_networks = current_stats.get('networks', {})
    previous_networks = previous_stats.get('networks', {})

    total_rx = 0
    total_tx = 0
    total_previous_rx = 0
    total_previous_tx = 0

    # Sum up all network interfaces
    for interface, stats in current_networks.items():
        total_rx += stats.get('rx_bytes', 0)
        total_tx += stats.get('tx_bytes', 0)

    for interface, stats in previous_networks.items():
        total_previous_rx += stats.get('rx_bytes', 0)
        total_previous_tx += stats.get('tx_bytes', 0)

    # Calculate deltas (bytes transferred since last measurement)
    rx_delta = max(0, total_rx - total_previous_rx)
    tx_delta = max(0, total_tx - total_previous_tx)

    # Format network I/O deltas as human readable string
    rx_str = convert.bytes_to_string(rx_delta)
    tx_str = convert.bytes_to_string(tx_delta)

    return f"↓{rx_str} ↑{tx_str}"
