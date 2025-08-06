![GitHub](https://img.shields.io/github/license/ziguifrido/docker-stats-py)
![GitHub top language](https://img.shields.io/github/languages/top/ziguifrido/docker-stats-py)
![GitHub last commit](https://img.shields.io/github/last-commit/ziguifrido/docker-stats-py)

# Docker Live Stats

A Python tool to monitor CPU, memory, and network I/O metrics of your Docker containers in real-time. The script uses the `prettytable` library to display the data in a formatted and readable table right in your terminal.

## Features

  * **Real-Time Monitoring:** Displays a continuous, updating stream of metrics for your containers.
  * **Enhanced Formatting:** Leverages the **PrettyTable** library to present data in a clean, easy-to-read table format.
  * **Detailed Metrics:** Shows CPU, memory consumption, and network I/O rates, including both percentage usage and absolute values.
  * **Network I/O Monitoring:** Real-time network traffic monitoring with download/upload rates per container.
  * **Automatic Screen Clearing:** Clears the terminal with each update, providing a clean and organized display.
  * **Error Handling:** Gracefully handles containers that might be removed during script execution, preventing the script from crashing.


## Prerequisites

* Python 3.7+
* pip (Python package manager)
* A virtual environment (venv)
* Docker

## How to Use

1.  Clone the repository:
```bash

git clone https://github.com/ziguifrido/docker-stats-py.git
cd docker-stats-py

```
    
2. Create a virtual environment
```bash

  python3 -m venv venv
  source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

```

3. Install the denpendencies
```bash

  pip install -r requirements.txt

```

4. Run the script
```bash

  python3 main.py
  
```

The script will begin monitoring and displaying the metrics table in your terminal. It will continue to update the table every few seconds until you stop it (usually with `Ctrl + C`).


## Output Sample

Your terminal output will look like this, with the table updating automatically:

```
+--------------+----------------+-------+----------------------------+-----------------+
|      ID      |      Name      |  CPU  |           Memory           |   Network I/O   |
+--------------+----------------+-------+----------------------------+-----------------+
| 5928f2a4c1f5 | my-app-service | 1.50% |  20.25% - 256.00mb/1.26gb  | ↓2.34mb ↑1.12mb |
| a0c3b8e7d2f9 |  db-container  | 0.89% |  45.70% - 512.00mb/2.00gb  | ↓0.85mb ↑0.43mb |
| d1e5f3c9a0b2 |  redis-cache   | 0.05% |  5.15% - 12.00mb/256.00mb  | ↓0.12mb ↑0.08mb |
| c2f8e1a7b3d6 |  web-frontend  | 2.15% | 32.80% - 128.00mb/512.00mb | ↓5.67mb ↑2.34mb |
+--------------+----------------+-------+----------------------------+-----------------+
```

### Column Explanation:
- **ID:** Container ID (short format)
- **Name:** Container name
- **CPU:** CPU usage percentage
- **Memory:** Memory usage percentage and absolute values (used/limit)
- **Network I/O:** Network traffic rates (↓ = download/received, ↑ = upload/transmitted)

## Contributing

Contributions are always welcome! If you find a bug or have an idea for a new feature, feel free to open an *issue* or submit a *pull request*.

## Technologies Used

* Python 3.7+
* Docker
* PrettyTable

## Licence
This projet uses the [MIT license](https://github.com/ziguifrido/docker-stats-py/blob/main/LICENSE).

## Author

Marcos Oliveira
