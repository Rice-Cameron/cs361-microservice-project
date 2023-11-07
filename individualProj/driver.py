# Cameron Rice
# ricecam@oregonstate.edu

import sys


# Send request for auth to microservice
def send_to_microservice(command):
    # send command to microservice via dumb pipe
    # for now, just show that the command is making it to this function which will then somehow
    # send it to the microservice in which will figure out what file to open and what function to call
    print(f"== Sending {command} to microservice")


# Get response from microservice
def get_from_microservice():
    # get response from microservice via dumb pipe
    # for now, just show that the command is making it to this function which will then somehow
    # send it to the microservice in which will figure out what file to open and what function to call
    print(f"== Getting response from microservice")


# If auth is verified, then continue with program
def auth_verified():
    print("== Auth verified")
    print("== Starting program")
    print("== Sending command to microservice")
    send_to_microservice("main_menu")
    print("== Getting response from microservice")
    get_from_microservice()


# If auth is denied, then exit program
def auth_denied():
    print("== Auth denied")
    print("== Exiting program")
    sys.exit(0)
