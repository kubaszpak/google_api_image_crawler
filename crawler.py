from googleapiclient.discovery import build
from update_key import check_for_correct_arguments, read_config
import sys
import requests
import os

def main(searched_phrase):

    api_key = read_config()

    service = build(serviceName='customsearch', version='v1', developerKey=api_key).cse()

    cx = '65d9bd572fc30c8c1'

    result = service.list(q=searched_phrase.replace('_',' '), cx=cx, searchType='image').execute()

    save_images_to_file(searched_phrase, result['items'])

def save_images_to_file(searched_phrase, list_of_images):

    image_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'images',searched_phrase)
    
    try:
        os.makedirs(image_dir)
    except:
        raise Exception('''There already exists a directory with this name, 
    look into the images folder''')

    for index,item in enumerate(list_of_images):
        response = requests.get(item['link'])
        if response.ok:
            with open(os.path.join(image_dir,f'{searched_phrase}{index}.jpg'),'wb') as f:
                f.write(response.content)


if __name__ == "__main__":
    searched_phrase = check_for_correct_arguments(sys.argv)
    main(searched_phrase)