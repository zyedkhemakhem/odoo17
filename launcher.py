
import os

container_name = 'odoo_zyed'
command = f'docker ps -a --filter "name={container_name}" --format "{{{{.Names}}}}" | grep -w {container_name}'
output = os.popen(command).read()
if len(output) == 0:
    os.system(f'docker build -t {container_name} .')
    os.system('docker-compose up')
    
else:
    print('oh my god it is already running my friend')


