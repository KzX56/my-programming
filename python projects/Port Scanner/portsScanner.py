import socket

def scan_port(ip, port):
    try:
        check = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Specify AF_INET for IPv4, SOCK_STREAM for TCP
        check.settimeout(1)  # Set a timeout of 1 second
        check.connect((ip, port))
        print("|+| this is open port : " + str(port))
        check.close()
    except socket.timeout:
        print(str(port) + " not open (timeout)")
    except ConnectionRefusedError:
        print(str(port) + " not open (connection refused)")
    except Exception as e: 
        print(f"{port} not open (error: {e})")
    finally: 
        if 'check' in locals() and check:
            check.close()

def scan(target, ports):
    print('\n' + ' Starting Scan IP\'s Ports ' + str(target))
    for port in range(1, ports + 1): # Scan up to and including the 'ports' number
        scan_port(target, port)

targets = input(" Enter Target: ")
ports = int(input(" How Many Ports : "))

if ',' in targets:
    print("[*] Scanning Multiple Targets")
    for ip_ad in targets.split(','):
        scan(ip_ad.strip(), ports) # .strip() removes leading/trailing whitespace
else:
    scan(targets, ports)

print("Done")
