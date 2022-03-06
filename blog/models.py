from django.db import models
from django.utils import timezone # позволяет устонавливать время на данный момент
from django.contrib.auth.models import User
from django.urls import reverse

class News(models.Model):
    title = models.CharField('Название статьи', max_length=100, unique=True) #CharField - позволяет устонавливать в текстовое полепозволяет устонавливать в текстовое поле макс. количество симвоов 250
    text = models.TextField('Основной текст статьи') #TextField - позволяет устонавливать в текстовое поле макс. количество симвоов неограниченно
    date = models.DateTimeField('Дата', default=timezone.now) #DateTimeField - позволяет устонавливать в текстовое поле дату и время
    avtor = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE) #ForeignKey - связывает поле с какой либо другой таблцей

    views = models.IntegerField('Просмотры', default=1) #IntegerField - количество просмотов
    # sizes = (
    #     ('S', 'Small'),
    #     ('M', 'Medium'),
    #     ('L', 'Large'),
    #     ('XL', 'X large')
    # )
    #
    # shop_sizes = models.CharField(max_length=2, choices=sizes, default='S')

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Новость' #Название таблицы в одиночном числе
        verbose_name_plural = 'Новости' #Название таблицы во множественном числе
