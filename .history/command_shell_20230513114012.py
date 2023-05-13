
# (venv) PS D:\Учеба\D2.NEWSPAPER\NewsPapper> 
# py manage.py makemigrations
# py manage.py migrate
# py manage.py shell 
# from news.models import *
# user1 = User.objects.create(username='Veralt', first_name='Igor')
# Author.objects.create(authorUser=user1)
# user2 = User.objects.create(username='Colobok', first_name='Ivan')
# Author.objects.create(authorUser=user2)
# Category.objects.create(name='IT')
# Category.objects.create(name='Education')
# Category.objects.create(name='Different')
# Category.objects.create(name='New')
# Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Veralt')), categoryType='NW', title='tratata title', text='tratata text')
