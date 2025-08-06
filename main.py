import docker
from util import cli, metrics
from prettytable import PrettyTable

client = docker.from_env()
table = PrettyTable()
table.field_names = ["ID", "Name", "CPU", "Memory", "Network I/O"]
previous_stats = {}

while True:
    containers = client.containers.list()

    if not containers:
        cli.show_message("No running containers found! Waiting...")
        continue

    current_stats = {}
    for container in containers:
        try:
            stat = container.stats(stream=False)
            container_id = stat['id'][:12]
            container_name = stat['name'].replace("/","")
            current_stats[container.id] = stat

            if container.id in previous_stats:
                cpu_percentage = metrics.calculate_cpu_usage(stat, previous_stats[container.id])
                memory_usage = metrics.calculate_memory_usage(stat)
                network_io = metrics.calculate_network_io(stat, previous_stats[container.id])

                table.add_row([container_id, container_name, cpu_percentage, memory_usage, network_io])

        except KeyError as e:
            cli.show_messages([f"Error getting container stats: KeyError[{e}]", "Trying again..."])
            break

    previous_stats = current_stats
    cli.show_metrics(table)
