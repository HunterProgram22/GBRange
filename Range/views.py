from django.shortcuts import render, HttpResponse
from django.views import View
from django.apps import apps
from .models import Drill_Base_Model
from .forms import Base_Drill_Form_GET, Base_Drill_Form_POST


class Main(View):
    def get(self, request):
        return render(request, 'Range/MainMenu.html', {})


class Base_Drill_View(View):
    def get(self, request):
        path = request.path.split('/')
        form_name = path[1] + '_' + path[2] + '_Form'
        model_name = path[1] + '_' + path[2]
        club = path[1]
        phase = path[2]
        form = Base_Drill_Form_GET(path[1], path[2])
        shots = Drill_Base_Model.objects.all().order_by('-date', '-pk')
        url = 'Range/'+ path[1] + '/' + path[1] + path[2] + '.html'
        return render(request, url, {'form': form, 'shots': shots,
                                    'club': club, 'phase': phase})

    def post(self, request):
        path = request.path.split('/')
        form_name = path[1] + '_' + path[2] + '_Form'
        model_name = path[1] + '_' + path[2]
        club = path[1]
        phase = path[2]
        dataform = Base_Drill_Form_POST(request.POST)
        if dataform.is_valid():
            dataform.save()
        form = Base_Drill_Form_GET(path[1], path[2])
        shots = Drill_Base_Model.objects.all().order_by('-date', '-pk')
        url = 'Range/'+ path[1] + '/' + path[1] + path[2] + '.html'
        return render(request, url, {'form': form, 'shots': shots,
                                     'club': club, 'phase': phase})


class MenuView(View):
    def get(self, request):
        path = request.path.split('/')
        url = 'Range/'+ path[1] + '/' + path[1] + 'Menu' + '.html'
        return render(request, url, {})
