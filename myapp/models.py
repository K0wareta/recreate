from django.db import models
from django.contrib.auth.models import AbstractUser

TYPES = (
    ('Парк', 'Парк'),
    ('Кафе', 'Кафе'),
    ('Ресторан', 'Ресторан'),
    ('Бар', 'Бар'),
    ('Выставка', 'Выставка'),
    ('Музей', 'Музей'),
    ('Кофейня', 'Кофейня'),
    ('Спа', 'Спа'),
    ('Спорт', 'Спорт'),
    ('Культурное пространство', 'Культурное пространство'),
    ('Антикафе', 'Антикафе'),
    ('Клуб', 'Клуб'),
    ('Театр', 'Театр'),
    ('Концерт', 'Концерт'),
)

GOALS = (
    ('Свидание', 'Свидание'),
    ('Спокойный отдых', 'Спокойный отдых'),
    ('Активный отдых', 'Активный отдых'),
    ('Развлечения', 'Развлечения'),
    ('Обучение', 'Обучение'),
    ('Для детей', 'Для детей'),
    ('Еда', 'Еда'),
)


class Place(models.Model):
    place_name = models.CharField(max_length=200)
    place_type = models.CharField(max_length=200, choices=TYPES, null=True, blank=True)
    place_cost = models.IntegerField(null=True, blank=True)
    place_link = models.CharField(max_length=200, null=True, blank=True)  # Встроенный виджет Яндекс карт
    place_address = models.CharField(max_length=200, null=True, blank=True)
    place_image = models.URLField(blank=True)  # Допилить, изображения будут храниться в файловой системе, а не в БД
    place_working_hours_start = models.TimeField(null=True, blank=True)
    place_working_hours_finish = models.TimeField(null=True, blank=True)
    place_goal1 = models.CharField(max_length=200, choices=GOALS, null=True, blank=True)
    place_goal2 = models.CharField(max_length=200, choices=GOALS, null=True, blank=True)
    place_goal3 = models.CharField(max_length=200, choices=GOALS, null=True, blank=True)
    place_rating = models.FloatField(max_length=3, null=True, blank=True)  # Допилить
    place_date = models.DateField(null=True, blank=True)  # Для ивентов, нужно будет допилить с какого по какое

    def __str__(self):
        return self.place_name


class CustomUser(AbstractUser):
    pass

    # add additional fields in here

    def __str__(self):
        return self.username
