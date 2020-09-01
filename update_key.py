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

def check_for_one_correct_argument():

    if(len(sys.argv) == 1 or len(sys.argv) > 3):
        raise Exception(
            '''You have passed a wrong number of arguments,
            pass an api_key after calling the script''')

    pattern = "^[\w:-]+$"
    argument = sys.argv[1]
    if(re.search(pattern, argument)):
        if(len(sys.argv)==2):
            return 'There is one correct argument'
        else:
            second_pattern = "^([\d]+)$"
            second_argument = sys.argv[2]
            if(re.search(second_pattern,second_argument) and int(second_argument)%10==0):
                return 'There are two correct arguments'
            else:
                raise Exception('Second argument must be a divisible by 10 number!')
    else:
        raise Exception(
            '''The key you have passed doesn't comply with the standards,
            try a different one''')


if __name__ == "__main__":
    config_key = check_for_one_correct_argument(sys.argv)
    update_config(config_key)