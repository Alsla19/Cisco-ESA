from paramiko import SSHClient, AutoAddPolicy
ESAClient=SSHClient()
ESAClient.load_system_host_keys()
ESAClient.set_missing_host_key_policy(AutoAddPolicy())
ESAClient.connect('10.106.36.220',username='ahsanabbas',password='TheNetworkViking', port='22')



def cli_access():
    '''
    command = ['status detail', 'version', 'ipcheck', 'workqueue status', 'antispamstatus', 'enginestatus all']

    for com in command:
    '''
    command = " "

    while command!= 'exit':
        command = input ("ESA > ")
        stdin, stdout, stderr = ESAClient.exec_command(command)
        output = stdout.readlines()
        print (''.join(output))
        file = open('ESA-show-tech-ALL.txt', 'a')
        file.write(''.join(output))
        file.close()

cli_access()

'''
    for line in stdout:
            print(line)
            print(type(line))
            break
'''
