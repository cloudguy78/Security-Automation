import subprocess
import time

#define the SentinelOne installer path and the device's IP Address
s1_installer_path = input(f"Enter SentinelOne Installation Path: ")
device_ip_address = input(f"Enter IP Address:") #take input for the iP address for the destination endpoint

# Take input for the Token Key
token_key = input("Enter Token Key: ")

# Define deployment settings
deployment_settings = {
    'installation_folder': r'C:\Program Files\SentinelOne',
    'token_key': token_key,  # Insert the user-provided Token Key
    'console_address': 'https://usea1-300-mssp.sentinelone.net/',
    'console_port': 443
}

# Define the command to deploy SentinelOne
deployment_command = f'{s1_installer_path} /s /v"/qn INSTALLFOLDER={deployment_settings["installation_folder"]} ACTIVATIONKEY={deployment_settings["activation_key"]} CONSOLEADDRESS={deployment_settings["console_address"]} CONSOLEPORT={deployment_settings["console_port"]}"'

# Connect to the device using psexec
psexec_command = f'psexec \\\\{device_ip_address} -u username -p password cmd /c "{deployment_command}"'
print(f'Connecting to {device_ip_address} and deploying SentinelOne...')
subprocess.run(psexec_command, shell=True)

# Wait for the deployment to complete
print('Waiting for deployment to complete...')
time.sleep(300)  # Wait for 5 minutes

# Verify the deployment
print('Verifying deployment...')
subprocess.run(f'psexec \\\\{device_ip_address} -u username -p password cmd /c "sc query SentinelOneAgent"', shell=True)

print('Deployment complete!')