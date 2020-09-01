from googleapiclient.discovery import build
from update_key import check_for_one_correct_argument, read_config
import sys
import requests
import os

def main(searched_phrase, number):

    api_key = read_config()

    service = build(serviceName='customsearch', version='v1', developerKey=api_key).cse()

    cx = '65d9bd572fc30c8c1'

    images = []

    for i in range(1,int(number),10):

        result = service.list(q=searched_phrase.replace('_',' '), cx=cx, searchType='image',start = i).execute()

        images += result['items']

    save_images_to_file(searched_phrase, images)

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
            with open(os.path.join(image_dir,f'{searched_phrase}{index+1}.jpg'),'wb') as f:
                f.write(response.content)


if __name__ == "__main__":
    response = check_for_one_correct_argument()
    print(sys.argv)
    if(response == 'There is one correct argument'):
        main(sys.argv[1],10)
    elif(response == 'There are two correct arguments'):
        main(sys.argv[1],sys.argv[2])
    