import json
from recipe.models import Post, PostType
from itertools import count
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os
from pathlib import Path
import shutil
from urllib import request
import requests
from bs4 import BeautifulSoup as bs
# import csv


import wget

class Command(BaseCommand):
    help = 'generate post'

    def add_arguments(self, parser):
        parser.add_argument('count',type=int, help='nuber of post to generate')

    def handle(self, *args, **kwargs):
        count = kwargs['count']


        user = User.objects.get(id=1)
        # for i in range(count) :
        #     title = 'title'+str(i)
        #     slug = 'slug'+str(i)
            # Post.objects.create(title=title,slug=slug,type=post_type,body={"time": 1650208279659, "blocks": [{"id": "kh-44CtFbD", "type": "Header", "data": {"text": "Ingrediants", "level": 2}},], "version": "2.22.2"},thumbnail='thumbnail/uploads/Frame_1.png', meta_description= 'kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju', author= user,status= 3)
        #     self.stdout.write("post created "+title)



        posts = []
        def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
            """
            Call in a loop to create terminal progress bar
            @params:
                iteration   - Required  : current iteration (Int)
                total       - Required  : total iterations (Int)
                prefix      - Optional  : prefix string (Str)
                suffix      - Optional  : suffix string (Str)
                decimals    - Optional  : positive number of decimals in percent complete (Int)
                length      - Optional  : character length of bar (Int)
                fill        - Optional  : bar fill character (Str)
                printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
            """
            percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
            filledLength = int(length * iteration // total)
            bar = fill * filledLength + '-' * (length - filledLength)
            print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
            # Print New Line on Complete
            if iteration == total: 
                print()

        def sitemapscroll():
            totalurl =0
            tabpost = []
            URL = 'https://ammachiyudeadukkala.net/sitemap_index.xml'
            req = requests.get(URL)
            soup = bs(req.text, 'xml')
            r_sitemaps = soup.select('sitemap')
            for sitmap in r_sitemaps:
                u = sitmap.find("loc").text
                if(u.__contains__('post')):
                    r = requests.get(u)
                    s = bs(r.text, 'xml')
                    posts_urls = s.find_all('loc')
                    for url in posts_urls:
                        arr=url.text.split('/')[3:]
                        post={'catagory':'null','slug':'null','url':'null'}
                        try:
                            post['catagory'] = arr[0]
                            post['slug'] = arr[1]
                            post['url'] = url.text
                            if(post['catagory']!='wp-content'):
                                tabpost.append(post)
                        except:
                            pass
            i=0
            printProgressBar(0, len(tabpost), prefix = 'Progress:', suffix = str(i)+'Complete', length = 50)
            for post in tabpost:
                scrapingpost(post)
                i=i+1
                printProgressBar(i, len(tabpost), prefix = 'Progress:', suffix = str(i)+' post scrolled Complete', length = 50)


        def scrapingpost(post):
            url = post['url']
            r = requests.get(url)
            soup = bs(r.content, 'html.parser')
            i=0
            body = soup.find('article').find_all()
            taglist = '{"time": 1650208279659, "blocks": ['
            for tags in body:                
                if tags.name == 'p':
                    if i != 0:
                        taglist=taglist+','
                    i=i+1
                    data = str(tags).split('p>')[1].replace('<br/>', '').replace('</', '')
                    taglist = taglist +'{"id": "_q'+str(i)+'K_TtVfX", "type": "paragraph", "data": {"text": "'+data+'"}}'            
                elif tags.name == 'div':
                    pass
                else:
                    pass
                    # print(tags)
            taglist = taglist+'], "version": "2.22.2"}'
            # print(taglist)
            # self.stdout.write()
            try:
                post_type = PostType.objects.get(post_type_name=post['catagory'])
                post['body']=json.loads(taglist,strict=False) 
                post['author'] = soup.find('li',class_='meta-author').text
                images = soup.find("meta",  property="og:image")
                post['title'] = soup.find("meta",  property="og:title")["content"].replace('- Ammachiyude Adukkala ™', '')
                post['description']= post['title']
                src=images["content"]
                res = requests.get(src, stream = True)
                arr=src.split('/')
                filename= Path(r'thumbnail\ '+"img\ " + str(next(reversed(arr))))
                post['image']= str(filename)
                os.makedirs(os.path.dirname(filename), exist_ok=True)
                if res.status_code == 200:
                    with open(filename,'wb') as f:
                        shutil.copyfileobj(res.raw, f)
                # posts.append(post)
                Post.objects.create(title=post['title'],slug=post['slug'],type=post_type,body=post['body'],thumbnail=post['image'], meta_description= post['description'], author= user,status= count)
            except:
                posts.append(post)
                pass
            

            # print(post['body'])
            
        # post ={}
        # post['catagory'] = 'recipe'
        # post['slug'] = 'mathi-fry'
        # post['url'] = 'https://ammachiyudeadukkala.net/non-vegetarian/fish-curry-2/'
        # scrapingpost(post)
        sitemapscroll()
        print(posts)
