# 1.1 Added While True loop for error handling
# 1.2 Added global delay factor 1 for timing handling
# 1.3 Added command_expect for improved output speed
# 1.4 Migrated to JSon formatting for ease of multi config
# 1.5 Added timing mechanism
# python Python_Aruba_Post_Json.py > delta.txt & type delta.txt

from __future__ import absolute_import, division, print_function

import time
import json
import netmiko
import tee

Aruba_Devices = """
192.168.1.1



""".strip().splitlines() 
device_type = 'hp_procurve'
#username = 'admin'
#password = 'admin'
username = 'Username'
password = 'Password'
global_delay_factor = 1

#netmiko_exceptions = (netmiko.ssh_exception.NetMikoTimeoutException,
#                     netmiko.ssh_exception.NetMikoAuthenticationException)


start = time.time()
for device in Aruba_Devices:
   while True:
      try:
         print('')
         print('Please Wait While Connecting to Device', device)
         print('')

         print('=' * 80)
         print('DISABLING PAGING SYSTEM...', device)
         print('=' * 80)
         connection = netmiko.ConnectHandler(ip=device, device_type=device_type,
                                             username=username, password=password)
         print(connection.send_command('no page'))    
         #connection.disconnect()
      except netmiko_exceptions as e:
         print('Failed Connection to Device', device, e)
         continue
      break
   while True:
      try:
         print('')
         print('=' * 80)
         print('SHOW RUN', device)
         print('=' * 80)
         print(connection.send_command('show run'))
         #connection.disconnect()
      except netmiko_exceptions as e:
         print('Failed Connection to Device', device, e)
         continue
      break
   while True:
      try:
         print('')
         print('=' * 80)
         print('SHOW MAC-ADDRESS', device)
         print('=' * 80)
         print(connection.send_command('show mac-address-table'))
         #connection.disconnect()
      except netmiko_exceptions as e:
         print('Failed Connection to Device', device, e)
         continue
      break
   while True:
      try:
         print('')
         print('=' * 80)
         print('SHOW ARP', device)
         print('=' * 80)
         print(connection.send_command('show arp'))
         #connection.disconnect()
      except netmiko_exceptions as e:
         print('Failed Connection to Device', device, e)
         continue
      break
   while True:
      try:
         print('')
         print('=' * 80)
         print('SHOW LLDP', device)
         print('=' * 80)
         print(connection.send_command('show lldp neighbor-info'))
         #connection.disconnect()
      except netmiko_exceptions as e:
         print('Failed Connection to Device', device, e)
         continue
      break
   while True:
      try:
         print('')
         print('=' * 80)
         print('SHOW VERSION', device)
         print('=' * 80)
         print(connection.send_command('show version'))
         #connection.disconnect()
      except netmiko_exceptions as e:
         print('Failed Connection to Device', device, e)
         continue
      break
   while True:
      try:
         print('')
         print('=' * 80)
         print('SHOW CAPACITIES', device)
         print('=' * 80)
         print(connection.send_command('show capacities-status'))
         #connection.disconnect()
      except netmiko_exceptions as e:
         print('Failed Connection to Device', device, e)
         continue
      break
   while True:
      try:
         print('')
         print('=' * 80)
         print('SHOW ENVIRONMENT', device)
         print('=' * 80)
         print(connection.send_command('show environment'))
         #connection.disconnect()
      except netmiko_exceptions as e:
         print('Failed Connection to Device', device, e)
         continue
      break  
   while True:
      try:
         print('')
         print('=' * 80)
         print('SHOW INTERFACES TRANSCEIVER', device)
         print('=' * 80)
         print(connection.send_command('show interface transceiver'))
         connection.disconnect()
      except netmiko_exceptions as e:
         print('Failed Connection to Device', device, e)
         continue
      break
end = time.time()
print('')
print('=' * 80)
print('Total Execution Time =', end - start)
print('=' * 80)