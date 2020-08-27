from apiclient.discovery import build

phrase = input('Pass a phrase that you would like to search for: ')

resource = build('customsearch', 'v1', developer_key=api_key).cse()

cx = '65d9bd572fc30c8c1'

resource.list(q=phrase, cx=cx).execute()
