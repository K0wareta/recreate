from django.shortcuts import render
from myapp.models import Place
from rest_framework import generics
from myapp.serializers import PlaceSerializer
from rest_framework.views import APIView #Новенькое
from rest_framework.response import Response #Новенькое
from django.forms import model_to_dict
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm




def myapp(request):

    all_places = Place.objects.all()
    for i in all_places:
        x = (i.place_name, i.place_type, i.place_cost, i.place_link, i.place_address, i.place_image,
             i.place_working_hours_start, i.place_working_hours_finish, i.place_goal1, i.place_goal2, i.place_goal3,
             i.place_rating, i.place_date)
        return render(request, 'myapp.html', context={'data': all_places})


def index(request):
    return render(request, 'main.html')



class PlacesAPIView(APIView):
    def get(self, request):
        p = Place.objects.all()
        return Response({'posts': PlaceSerializer(p, many=True).data})

    def post(self, request):
        serializer = PlaceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post_new = Place.objects.create(
            place_name=request.data['place_name'],
            place_type=request.data['place_type'],
            place_cost=request.data['place_cost'],
            place_link=request.data['place_link'],
            place_address=request.data['place_address'],
            place_image=request.data['place_image'],
            place_working_hours_start=request.data['place_working_hours_start'],
            place_working_hours_finish=request.data['place_working_hours_finish'],
            place_goal1=request.data['place_goal1'],
            place_goal2=request.data['place_goal2'],
            place_goal3=request.data['place_goal3'],
            place_rating=request.data['place_rating'],
            place_date=request.data['place_date'],
        )
        return Response({'post': model_to_dict(post_new).data()})


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
