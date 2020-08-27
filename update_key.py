from configparser import ConfigParser
import sys
import re


def update_config(config_key):

    # Read config.ini file
    config_object = ConfigParser()
    config_object.read('api_key.ini')

    # Get the USERINFO section
    userinfo = config_object['USER_INFO']

    # Update the password
    userinfo['api_key'] = config_key

    # Write changes back to file
    with open('api_key.ini', 'w') as conf:
        config_object.write(conf)

def read_config():
    config_object = ConfigParser()
    config_object.read('api_key.ini')

    # Get the USERINFO section
    userinfo = config_object['USER_INFO']

    return userinfo['api_key']

def check_for_correct_arguments(args):

    if(len(args) == 1 or len(args) > 2):
        raise Exception(
            '''You have passed a wrong number of arguments,
            pass an api_key after calling the script''')
    else:
        pattern = "^\w+$"
        config_key = sys.argv[1]
        if(re.search(pattern, config_key)):
            return config_key
        else:
            raise Exception(
                '''The key you have passed doesn't comply with the standards,
                try a different one''')


if __name__ == "__main__":
    config_key = check_for_correct_arguments(sys.argv)
    update_config(config_key)