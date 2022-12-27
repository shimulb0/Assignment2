import openai
import os
from wp_guten_post import *
import requests
import base64

def oai_write(prompt):
    from dotenv import load_dotenv
    load_dotenv()
    openai.api_key = os.getenv('API_KEY')
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    output = response.get('choices')[0].get('text')
    return output


keywords = open("keywords.txt").read().splitlines()
for keyword in keywords:
    keyword = keyword.strip('Best ')
    title = f'Best {keyword} reviews with buying guide'
    intro = oai_write(f'Write 150 words about {keyword}')
    first_h2 = f'Why {keyword} is important'
    paragraph2 = oai_write(f'Write three paragraphs about Why {keyword} is important')
    second_h2 = f'{keyword.title()} Buying Guide'
    paragraph3 = oai_write(f'Write 50 words about How to choose best {keywords} in two paragraphs')
    third_h2 = f'Features of best {keyword}'
    paragraph4 = oai_write(f'Features of best {keyword}, Write 200 words in four paragraphs')
    first_h3 = f'How to use a {keyword}'
    paragraph5 = oai_write(f'Write 50 words about how to use a {keyword} in two paragraphs')
    fourth_h2 = 'Wrap Up'
    conclu = oai_write(f'Write a short paragraph about best {keyword}')
    image_url = 'https://thumbs.dreamstime.com/b/product-review-text-written-over-colorful-background-product-review-colorful-stripes-group-136074718.jpg'

    para1 = paragraph(intro)
    para2 = paragraph(paragraph2)
    para3 = paragraph(paragraph3)
    para4 = paragraph(paragraph4)
    para5 = paragraph(paragraph5)
    conclud = paragraph(conclu)
    h2_1 = h2(first_h2)
    h2_2 = h2(second_h2)
    h2_3 = h2(third_h2)
    h3_1 = h3(first_h3)
    h3_2 = h3(fourth_h2)
    image = media(image_url, keyword)

    from dotenv import load_dotenv
    load_dotenv()
    user = os.getenv('WP_user')
    password = os.getenv('WP_password')

    credential = f'{user}:{password}'
    token = base64.b64encode(credential.encode())
    headers = {'Authorization':f'Basic {token.decode("utf-8")}'}

    content_data = {
        'title': title,
        'content': para1 + image + h2_1 + para2 + h2_2 + para3 + h2_3 + para4 + h3_1 + para5 + h3_2 + conclud,
        'categories': '67'
    }
    api_end_point = 'https://localhost/wp/wp-json/wp/v2/posts'
    r = requests.post(api_end_point, data=content_data, headers=headers, verify=False)
    print(title, 'posted')

