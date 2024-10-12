from osimport import subprocess
import time

#define the SentinelOne installer path and the device's IP Address
sentineone_installer_path = 'C:\Users\UserName\Downloads\SentinelOneInstaller.exe'
device_ip_address = '192.168.1.100' #change this to the IP Iddress of the agent

#define deployment settings
deployment_settings = {
    'installation_folder': 'C:\\Program Files\\SentinelOne',
    'token_key': 'Insert_Token_Key',
    'console_address': 'https://management.console.address.com',
    'console_port': 443
}
# Define the command to deploy SentinelOne
deployment_command = f'{sentinelone_installer_path} /s /v"/qn INSTALLFOLDER={deployment_settings["installation_folder"]} ACTIVATIONKEY={deployment_settings["activation_key"]} CONSOLEADDRESS={deployment_settings["console_address"]} CONSOLEPORT={deployment_settings["console_port"]}"'

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