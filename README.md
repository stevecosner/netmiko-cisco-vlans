# netmiko-cisco-vlans
Create vlans on a Cisco IOS L2 device using a Netmiko python script.

You need to setup SSH access on the Cisco device.

I used the login local command in the VTY lines and the username command in global config top setup username, password and privilege.
username steve privilege 15 password admin

You can set this up from a Docker container inside GNS3, a PC outside of GNS3 connecting to the Cisco device using a cloud or you can run this on physical hardware if you have it.
