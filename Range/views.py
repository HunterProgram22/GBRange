from django.shortcuts import render
from django.views import View
from django.apps import apps
from .models import Drill_Base_Model
from .dictionaries import form_names_dict


class Main(View):
    def get(self, request):
        return render(request, 'Range/MainMenu.html', {})


class Base_Drill_View(View):
    def get(self, request):
        path = request.path.split('/')
        form_name = path[1] + '_' + path[2] + '_Form'
        model_name = path[1] + '_' + path[2]
        form = form_names_dict[form_name]
        shots = Drill_Base_Model.objects.all().order_by('-date', '-pk')
        url = 'Range/'+ path[1] + '/' + path[1] + path[2] + '.html'
        return render(request, url, {'form': form, 'shots': shots})

    def post(self, request):
        path = request.path.split('/')
        form_name = path[1] + '_' + path[2] + '_Form'
        model_name = path[1] + '_' + path[2]
        form = form_names_dict[form_name]
        dataform = form(request.POST)
        if dataform.is_valid():
            dataform.save()
        shots = Drill_Base_Model.objects.all().order_by('-date', '-pk')
        url = 'Range/'+ path[1] + '/' + path[1] + path[2] + '.html'
        return render(request, url, {'form': form, 'shots': shots})

    def shots_call(self, model_name):
        return model_name.objects.all().order_by('-date', '-pk')


class MenuView(View):
    def get(self, request):
        path = request.path.split('/')
        url = 'Range/'+ path[1] + '/' + path[1] + 'Menu' + '.html'
        return render(request, url, {})
