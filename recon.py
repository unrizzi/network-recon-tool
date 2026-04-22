import socket, json
from datetime import datetime

class NetworkRecon:

    def __init__(self,target):
        self.target = target
        self.results = {
            "target": target,
            "scan_time": datetime.now().isoformat(),
            "open_ports": []
        }

    def resolve_target(self):
        try:
            return socket.gethostbyname(self.target)
        except socket.gaierror:
            print(f"[ERROR]: Could not resolve host {self.target}")
            return None
    
    def check_port(self,ip,port,timeout=2):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                result = s.connect_ex((ip,port))
                if result == 0:
                    return True
                return False
        except Exception as e:
            print(f"Unexpected error on port {port}: {e}")
            return False
        
    def get_banner(self, ip, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(3)
                s.connect((ip,port))

                banner = s.recv(1024).decode(errors='ignore').strip()
                return banner if banner else "No banner retrieved."
        except Exception:
            return None