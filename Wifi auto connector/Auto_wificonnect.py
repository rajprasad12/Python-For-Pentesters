import os
import sys
# it will show the saved networks
saved_profiles= os.popen(" netsh wlan show profiles").read()
print(saved_profiles)

#it will show the available networks
available_profiles= os.popen('netsh wlan show networks').read()
print(available_profiles)

# to take wifi name which wants to connect
prefered_ssid= input('enter the wifi name to connect with!!')

# it will disconnect from the current network
response= os.popen('netsh wlan disconnect').read()
print(response)

# it checks for the wifi that is saved or not
if prefered_ssid not in saved_profiles:
    print('Profile for ' + prefered_ssid + 'not saved in the system' )
    print('Can not connect to the network!! ')
    sys.exit()

# it checks the wifi is available or not
elif prefered_ssid in available_profiles:
    print('Connecting to !!! '+ prefered_ssid)
    os.popen('netsh wlan connect name=' +'"'+prefered_ssid+'"') #this command helps to connect with the given wifi
    print('Connected to  '+prefered_ssid)
    