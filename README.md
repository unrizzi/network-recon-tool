# Network Reconnaissance Tool

Utility for network discovery, port scanning, and service identification. The tool uses multithreading to perform concurrent scans and exports findings to structured JSON files.

## Features

* DNS host resolution.
* Concurrent TCP port scanning.
* Passive service banner grabbing.
* JSON data persistence.

## Installation

```
git clone https://github.com/unrizzi/network-recon-tool.git
cd network-recon-tool
```

## Usage

The tool is implemented as a class and can be integrated into Python scripts.

### Basic Implementation

```
from recon import NetworkRecon

# Initialize scanner
scanner = NetworkRecon("scanme.nmap.org")

# Define ports to scan
ports = [21, 22, 80, 443]

# Execute multithreaded scan
scanner.scan_port_range(ports)

# Export results
scanner.save_results()
```

## Disclaimer

Unauthorized scanning is prohibited. Use this tool only with explicit permission.