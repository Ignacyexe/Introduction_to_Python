from netmiko import ConnectHandler

try:
    device_connection = ConnectHandler(
        device_type='cisco_ios',
        host='10.10.20.48',
        username='developer',
        password='C1sco12345',
    )
    print("Połączono się z urządzeniem Cisco!")

    ssh_output = device_connection.send_command("show ip int br")
    print(ssh_output)

    hostname_output = device_connection.send_command("hostname")
    print(hostname_output)

except:
    print("Porażka...")
