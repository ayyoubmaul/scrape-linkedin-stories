from bs4 import BeautifulSoup as bs 
import re
import json
import requests

def execute(url)
  web_page = requests.get(url)

  page_source = web_page.text

  compiled_html = bs(page_source, 'html')

  str_json = re.findall(r'(?<=window.__APOLLO_STATE__ = ).*', compiled_html.find_all('script')[4].contents[0])[0]

  content_json = json.loads(str_json)

  post_keys = filter(lambda x: x, [key if 'Post:' in key else None for key in content_json])

  post_list = []

  for post in list(post_keys):
      post_dict = {}

      post_dict['url'] = content_json[post]['mediumUrl']
      post_dict['title'] = content_json[post]['title']
      post_dict['posted_at_ts'] = content_json[post]['firstPublishedAt']
      post_dict['featured_image_url'] = re.sub(r'ImageMetadata:', 'https://miro.medium.com/v2/resize:fill:224:224/', content_json[post]['previewImage']['__ref'])

      post_list.append(post_dict)

  return post_list
