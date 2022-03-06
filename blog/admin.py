from django.contrib import admin
from .models import News

admin.site.register(News) # Регесстрирруем таблицу News, которую мы создавали в файле models.py что бы она отображалась
