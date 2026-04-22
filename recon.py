import socket, json, threading
from datetime import datetime
from queue import Queue

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
        
    def scan_port_range(self,port_list,thread_count=50):
        ip = self.resolve_target()
        if not ip:
            print("Target IP could not be resolved.")
            return
        threads = []
        def worker(port):
            try:
                if self.check_port(ip, port):
                    banner = self.get_banner(ip, port)
                    print(f"Found open port: {port} | Service: {banner}")
                    self.results["open_ports"].append({"port": port, "service": banner})
            except Exception as e:
                print(f"Error scanning port {port}: {e}")
        for port in port_list:
            t = threading.Thread(target=worker,args=(port,))
            threads.append(t)
            t.start()
            if len(threads) >= thread_count:
                for t in threads:
                    t.join()
                threads = []
        for t in threads:
            t.join()
        print(f"Scan finished. Found {len(self.results['open_ports'])} open ports.")