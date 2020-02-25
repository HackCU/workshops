import subprocess

def check_connectivity(ip):

    test_ip=ip
    proc = subprocess.Popen( ['ping', '-c', '2', test_ip], stdout=subprocess.PIPE)
    x=proc.communicate()
    if proc.returncode == 0:
        print("{} is reachable.".format(test_ip))
    else:
        print("{} is not reachable.".format(test_ip))
        raise Exception("Given Web page or Internet is down")
    
ip = "192.168.10.200"
check_connectivity(ip)
print("New")