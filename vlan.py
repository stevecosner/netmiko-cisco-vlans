from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.91.134',
    'username': 'steve',
    'password': 'admin',
}


net_connect = ConnectHandler(**iosv_l2)
output = net_connect.send_config_set(['vlan 10,20,30,40,50,60'])
output = net_connect.send_command('show vlan')
print output
