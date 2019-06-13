from netmiko import ConnectHandler

S1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.91.132',
    'username': 'steve',
    'password': 'admin',
}

S2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.91.133',
    'username': 'steve',
    'password': 'admin',
}

all_devices = [S1, S2]

for devices in all_devices:


    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(['vlan 10,20,30,40,50,60'])
    output = net_connect.send_command('show vlan brief')
    print output
