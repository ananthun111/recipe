from recipe.models import Post, PostType
from itertools import count
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'generate post'

    def add_arguments(self, parser):
        parser.add_argument('count',type=int, help='nuber of post to generate')

    def handle(self, *args, **kwargs):
        count = kwargs['count']


        user = User.objects.get(id=1)
        post_type = PostType.objects.get(id=1)
        for i in range(count) :
            title = 'title'+str(i)
            slug = 'slug'+str(i)
            Post.objects.create(title=title,slug=slug,type=post_type,body={"time": 1650208279659, "blocks": [{"id": "kh-44CtFbD", "type": "Header", "data": {"text": "Ingrediants", "level": 2}},], "version": "2.22.2"},thumbnail='thumbnail/uploads/Frame_1.png', meta_description= 'kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju kunju', author= user,status= 3)
            self.stdout.write("post created "+title)