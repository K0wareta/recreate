import io
from rest_framework import serializers, fields
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from myapp.models import Place



TYPES = (
    ('парк', 'Парк'),
    ('кафе', 'Кафе'),
    ('ресторан', 'Ресторан'),
    ('бар', 'Бар'),
    ('выставка', 'Выставка'),
    ('музей', 'Музей'),
    ('кофейня', 'Кофейня'),
    ('спа', 'Спа'),
    ('спорт', 'Спорт'),
    ('культурное пространство', 'Культурное пространство'),
    ('антикафе', 'Антикафе'),
    ('клуб', 'Клуб'),
    ('театр', 'Театр'),
    ('концерт', 'Концерт'),
)

GOALS = (
    ('свидание', 'Свидание'),
    ('спокойный отдых', 'Спокойный отдых'),
    ('активный отдых', 'Активный отдых'),
    ('развлечения', 'Развлечения'),
    ('обучение', 'Обучение'),
    ('для детей', 'Для детей'),
    ('еда', 'Еда'),
)

class PlaceSerializer(serializers.Serializer):
    place_name = serializers.CharField(max_length=200)
    place_type = serializers.ChoiceField(choices=TYPES, required=False, allow_null=True)
    place_cost = serializers.IntegerField(required=False, allow_null=True)
    place_link = serializers.CharField(required=False, allow_blank=True)  # Встроенный виджет Яндекс карт
    place_address = serializers.CharField(required=False, allow_blank=True)
    place_image = serializers.URLField(required=False, allow_null=True)  # Допилить, изображения будут храниться в файловой системе, а не в БД
    place_working_hours_start = serializers.TimeField(required=False, allow_null=True)
    place_working_hours_finish = serializers.TimeField(required=False, allow_null=True)
    place_goal1 = serializers.ChoiceField(choices=GOALS, required=False, allow_null=True)
    place_goal2 = serializers.ChoiceField(choices=GOALS, required=False, allow_null=True)
    place_goal3 = serializers.ChoiceField(choices=GOALS, required=False, allow_null=True)
    place_rating = serializers.FloatField(required=False, allow_null=True)
    place_date = serializers.DateField(required=False, allow_null=True)  # Для ивентов, нужно будет допилить с какого по какое


