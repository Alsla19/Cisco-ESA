import requests

import json

import pprint

import base64

import getpass



def convert_user_pass(username,password):

    """Converts username and password to base64 string."""

    user = username+":"+password

    user_bytes = user.encode("ascii")

    base64_bytes = base64.b64encode(user_bytes)

    base64_string = base64_bytes.decode("ascii")

    return (base64_string)



def fetch_user_pass():

    """Fetches username and password from user input."""

    user = input("Username : ")

    pwd = getpass.getpass()

    return user,pwd



def fetch_ip():

    """Fetches IP address and port number from user input."""

    ip = input("Enter the IP Address of the ESA : \n")

    port_no = input("Enter the port number : \n")

    return ip,port_no



def setting_base_uRL(ip,port_no):

    """Sets the base URL."""

    global url

    url = "http://"+ip+":"+port_no+"/esa/api/v2.0"



def fetch_headers(cred):

    """Fetches the headers for the request."""

    headers = {

    'Authorization': 'Basic '+ cred,

    'Cookie': 'sid'

    }

    return headers



def fetch_choice():

    """Fetches the user's choice of action."""

    choice = input("""\n\nEnter your choice:

        1 - Date and Time

        2 - Managed Device Information

        3 - Health of the Device

        4 - List the Accessible APIs

        q - quit

        : """)

    return choice



def managed_device_info(headers):

    """Fetches and prints the managed device information."""

    response = requests.request("GET", url+"/config/appliances?device_type=esa", headers=headers, verify="False")

    print_output(response)



def fetch_date_time(headers):

    """Fetches and prints the date and time."""

    response = requests.request("GET", url+"/config/system_time?device_type=esa", headers=headers, verify="False")

    print_output(response)



def fetch_health(headers):

    """Fetches and prints the health of the device."""

    response = requests.request("GET", url+"/health", headers=headers, verify="False")

    print_output(response)



def accessible_apis(headers):

    """Fetches and prints the accessible APIs."""

    response = requests.request("GET", url+"/login/privileges", headers=headers, verify="False")

    print_output(response)



def print_output(response):

    """Prints the output from the request."""

    json_string = json.loads(response.content)

    print("\n********************************************************\n\n")

    pprint.pprint(json_string)

    print("\n********************************************************")



if __name__=='__main__':

    """Main function."""

    ip,port_no = fetch_ip()

    setting_base_uRL(ip,port_no)

    username,password = fetch_user_pass()

    cred = convert_user_pass(username,password)

    headers = fetch_headers(cred)   

    while True:

        choice = fetch_choice()

        if choice == '1':

            fetch_date_time(headers)

        elif choice == '2':

            managed_device_info(headers)

        elif choice == '3':

            fetch_health(headers)

        elif choice == '4':

            accessible_apis(headers)

        elif choice.lower() == "q":

            break


#Video demonstration of this Python Code:
#https://www.youtube.com/watch?v=8Fc1OOuCk1E