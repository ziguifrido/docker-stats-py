import docker
import time
from util import cli
from util import convert
from prettytable import PrettyTable

client = docker.from_env()
table = PrettyTable()
previous_stats = {}

while True:
    containers = client.containers.list()
    table.field_names = ["ID", "Name", "CPU", "Memory"]

    if not containers:
        cli.clear_screen()
        print("No running containers found! Waiting...")
        time.sleep(5)
        continue

    current_stats = {}
    for container in containers:
        try:
            stat = container.stats(stream=False)
            container_id = stat['id'][:12]
            container_name = stat['name'].replace("/","")
            current_stats[container.id] = stat

            if container.id in previous_stats:
                memory_usage = stat['memory_stats']['usage']
                memory_limit = stat['memory_stats']['limit']
                memory_usage_str = convert.bytes_to_string(memory_usage)
                memory_limit_str = convert.bytes_to_string(memory_limit)
                memory_percentage_str = convert.values_to_percentage(memory_usage, memory_limit)

                precpu_stats = previous_stats[container.id]['cpu_stats']
                cpu_stats = stat['cpu_stats']

                cpu_delta = cpu_stats['cpu_usage']['total_usage'] - precpu_stats['cpu_usage']['total_usage']
                system_cpu_delta = cpu_stats['system_cpu_usage'] - precpu_stats['system_cpu_usage']
                number_cpus = cpu_stats['online_cpus']
                cpu_percentage = (cpu_delta / system_cpu_delta) * number_cpus * 100.0 if system_cpu_delta > 0 else 0.0

                memory_str = f"{memory_percentage_str} - {memory_usage_str}/{memory_limit_str}"
                cpu_str = f"{cpu_percentage:.2f}%"

                table.add_row([container_id, container_name, cpu_str, memory_str])

        except docker.errors.APIError as e:
            print(f"Error getting stats for container {container.id}: {e}")
            break

    previous_stats = current_stats
    cli.clear_screen()
    print(table)
    table.clear()

    # time.sleep(5)
