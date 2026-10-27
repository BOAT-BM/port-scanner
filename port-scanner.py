import socket
from concurrent.futures import ThreadPoolExecutor
import argparse

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            if s.connect_ex((host, port)) == 0:
                return port
    except Exception:
        pass
    return None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--end", type=int, default=100)
    args = parser.parse_args()

    open_ports = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(lambda p: scan_port(args.host, p),
                               range(args.start, args.end + 1))
        for r in results:
            if r:
                open_ports.append(r)

    print(f"开放端口: {open_ports}")

if __name__ == "__main__":
    main()