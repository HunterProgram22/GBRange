from django.shortcuts import render
from django.views import View
from django.apps import apps
from .dictionaries import form_names_dict, model_names_dict

class Main(View):
    def get(self, request):
        return render(request, 'Range/MainMenu.html', {})

class Base_Drill_View(View):

    def get(self, request):
        path = request.path.split('/')
        form_name = path[1] + '_' + path[2] + '_Form'
        model_name = path[1] + '_' + path[2]
        form = form_names_dict[form_name]
        shots = self.shots_call(model_names_dict[model_name])
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
        shots = self.shots_call(model_names_dict[model_name])
        url = 'Range/'+ path[1] + '/' + path[1] + path[2] + '.html'
        return render(request, url, {'form': form, 'shots': shots})

    def shots_call(self, model_name):
        return model_name.objects.all().order_by('-date', '-pk')

class Woods(View):
    def get(self, request):
        return render(request, 'Range/Woods/WoodsMenu.html', {})

class WoodsCalibration(View):
    pass

class WoodsPerformance(View):
    pass

class WoodsGames(View):
    pass

class WoodsExperimental(Base_Drill_View):
    def __str__ (self):
        return None

class WoodsTest(View):
    pass

class WoodsTechnical(Base_Drill_View):
    def __str__ (self):
        return None


class Hybrids(View):
    def get(self, request):
        return render(request, 'Range/Hybrids/HybridsMenu.html', {})

class HybridsTest(View):
    pass

class HybridsExperimental(Base_Drill_View):
    def __str__ (self):
        return None

class HybridsCalibration(View):
    pass

class HybridsPerformance(View):
    pass

class HybridsGames(View):
    pass

class HybridsTechnical(Base_Drill_View):
    def __str__ (self):
        return None

class Irons(View):
    def get(self, request):
        return render(request, 'Range/Irons/IronsMenu.html', {})

class IronsTest(View):
    pass

class IronsTechnical(Base_Drill_View):
    def __str__ (self):
        return None

class IronsExperimental(Base_Drill_View):
    def __str__ (self):
        return None

class IronsCalibration(View):
    pass

class IronsPerformance(View):
    pass

class IronsGames(View):
    pass

class Wedges(View):
    def get(self, request):
        return render(request, 'Range/Wedges/WedgesMenu.html', {})

class WedgesTest(View):
    pass

class WedgesCalibration(View):
    pass

class WedgesPerformance(View):
    pass

class WedgesGames(View):
    pass

class WedgesTechnical(Base_Drill_View):
    def __str__ (self):
        return None

class WedgesExperimental(Base_Drill_View):
    def __str__ (self):
        return None

class Chipping(View):
    def get(self, request):
        return render(request, 'Range/Chipping/ChippingMenu.html', {})

class ChippingTest(View):
    pass

class ChippingExperimental(Base_Drill_View):
    def __str__ (self):
        return None

class ChippingCalibration(View):
    pass

class ChippingPerformance(View):
    pass

class ChippingGames(View):
    pass

class ChippingTechnical(Base_Drill_View):
    def __str__ (self):
        return None

class Putting(View):
    def get(self, request):
        return render(request, 'Range/Putting/PuttingMenu.html', {})

class PuttingTest(View):
    pass

class PuttingCalibration(View):
    pass

class PuttingPerformance(View):
    pass

class PuttingGames(View):
    pass

class PuttingTechnical(Base_Drill_View):
    def __str__ (self):
        return None

class PuttingExperimental(Base_Drill_View):
    def __str__ (self):
        return None
