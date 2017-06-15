from django.shortcuts import render
from django.views import View
from .models import Woods_Technical, Hybrids_Technical, Irons_Technical, \
    Wedges_Technical, Chipping_Technical, Putting_Technical, Woods_Experimental, \
    Wedges_Experimental, Putting_Experimental
from .forms import Woods_Test_Form, Woods_Technical_Form, Hybrids_Technical_Form, \
    Irons_Technical_Form, Wedges_Technical_Form, Chipping_Technical_Form, \
    Putting_Technical_Form, Woods_Experimental_Form, Wedges_Experimental_Form, \
    Putting_Experimental_Form



class Main(View):
    def get(self, request):
        return render(request, 'Range/MainMenu.html', {})

class Woods(View):
    def get(self, request):
        return render(request, 'Range/Woods/WoodsMenu.html', {})

class WoodsCalibration(View):
    pass

class WoodsPerformance(View):
    pass

class WoodsGames(View):
    pass

class WoodsExperimental(View):
    def get(self, request):
        form = Woods_Experimental_Form()
        shots = Woods_Experimental.objects.all().order_by('-date', '-pk')
        return render(request, 'Range/Woods/WoodsExperimental.html', {'form': form,
                                                                'shots': shots})

    def post(self, request):
        dataform = Woods_Experimental_Form(request.POST)
        if dataform.is_valid():
            dataform.save()
        form = Woods_Experimental_Form()
        shots = Woods_Experimental.objects.all().order_by('-date', '-pk')
        return render(request, 'Range/Woods/WoodsExperimental.html', {'form': form,
                                                                'shots': shots})

class WoodsTest(View):
    def get(self, request):
        form = Woods_Test_Form()
        return render(request, 'Range/Woods/WoodsTest.html', {'form':form,
                                                        'range':range(3)
                                                        })

class WoodsTechnical(View):
    def get(self, request):
        form = Woods_Technical_Form()
        shots = Woods_Technical.objects.all().order_by('-date', '-pk')
        return render(request, 'Range/Woods/WoodsTechnical.html', {'form': form,
                                                             'shots': shots})

    def post(self, request):
        dataform = Woods_Technical_Form(request.POST)
        if dataform.is_valid():
            dataform.save()
        form = Woods_Technical_Form()
        shots = Woods_Technical.objects.all().order_by('-date', '-pk')
        return render(request, 'Range/Woods/WoodsTechnical.html', {'form': form,
                                                             'shots': shots})


class Hybrids(View):
    def get(self, request):
        return render(request, 'Range/Hybrids/HybridsMenu.html', {})

class HybridsTest(View):
    pass

class HybridsExperimental(View):
    pass

class HybridsCalibration(View):
    pass

class HybridsPerformance(View):
    pass

class HybridsGames(View):
    pass

class HybridsTechnical(View):
    def get(self, request):
        form = Hybrids_Technical_Form()
        shots = Hybrids_Technical.objects.all().order_by('-date', '-pk')
        return render(request, 'Range/Hybrids/HybridsTechnical.html', {'form': form,
                                                               'shots': shots})

    def post(self, request):
        dataform = Hybrids_Technical_Form(request.POST)
        if dataform.is_valid():
            dataform.save()
        form = Hybrids_Technical_Form()
        shots = Hybrids_Technical.objects.all().order_by('-date', '-pk')
        return render(request, 'Range/Hybrids/HybridsTechnical.html', {'form': form,
                                                               'shots': shots})

class Irons(View):
    def get(self, request):
        return render(request, 'Range/Irons/IronsMenu.html', {})

class IronsTest(View):
    pass

class IronsExperimental(View):
    pass

class IronsCalibration(View):
    pass

class IronsPerformance(View):
    pass

class IronsGames(View):
    pass

class IronsTechnical(View):
    def get(self, request):
        form = Irons_Technical_Form()
        shots = Irons_Technical.objects.all().order_by('-date', '-pk')
        return render(request, 'Range/Irons/IronsTechnical.html', {'form': form,
                                                             'shots': shots})

    def post(self, request):
        dataform = Irons_Technical_Form(request.POST)
        if dataform.is_valid():
            dataform.save()
        form = Irons_Technical_Form()
        shots = Irons_Technical.objects.all().order_by('-date', '-pk')
        return render(request, 'Range/Irons/IronsTechnical.html', {'form': form,
                                                             'shots': shots})

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

class WedgesTechnical(View):
    def get(self, request):
        form = Wedges_Technical_Form()
        shots = Wedges_Technical.objects.all().order_by('-date', '-pk')
        return render(request, 'Range/Wedges/WedgesTechnical.html', {'form': form,
                                                              'shots': shots})

    def post(self, request):
        dataform = Wedges_Technical_Form(request.POST)
        if dataform.is_valid():
            dataform.save()
        form = Wedges_Technical_Form()
        shots = Wedges_Technical.objects.all().order_by('-date', '-pk')
        return render(request, 'Range/Wedges/WedgesTechnical.html', {'form': form,
                                                              'shots': shots})

class WedgesExperimental(View):
    def get(self, request):
        form = Wedges_Experimental_Form()
        shots = Wedges_Experimental.objects.all().order_by('-date', '-pk')
        return render(request, 'Range/Wedges/WedgesExperimental.html', {'form': form,
                                                                 'shots': shots})

    def post(self, request):
        dataform = Wedges_Experimental_Form(request.POST)
        if dataform.is_valid():
            dataform.save()
        form = Wedges_Experimental_Form()
        shots = Wedges_Experimental.objects.all().order_by('-date', '-pk')
        return render(request, 'Range/Wedges/WedgesExperimental.html', {'form': form,
                                                                 'shots': shots})


class Chipping(View):
    def get(self, request):
        return render(request, 'Range/Chipping/ChippingMenu.html', {})

class ChippingTest(View):
    pass

class ChippingExperimental(View):
    pass

class ChippingCalibration(View):
    pass

class ChippingPerformance(View):
    pass

class ChippingGames(View):
    pass

class ChippingTechnical(View):
    def get(self, request):
        form = Chipping_Technical_Form()
        shots = Chipping_Technical.objects.all().order_by('-date', '-pk')
        return render(request, 'Range/Chipping/ChippingTechnical.html', {'form': form,
                                                                'shots': shots})

    def post(self, request):
        dataform = Chipping_Technical_Form(request.POST)
        if dataform.is_valid():
            dataform.save()
        form = Chipping_Technical_Form()
        shots = Chipping_Technical.objects.all().order_by('-date', '-pk')
        return render(request, 'Range/Chipping/ChippingTechnical.html', {'form': form,
                                                                'shots': shots})

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

class PuttingTechnical(View):
    def get(self, request):
        form = Putting_Technical_Form()
        shots = Putting_Technical.objects.all().order_by('-date', '-pk')
        return render(request, 'Range/Putting/PuttingTechnical.html', {'form': form,
                                                               'shots': shots})

    def post(self, request):
        dataform = Putting_Technical_Form(request.POST)
        if dataform.is_valid():
            dataform.save()
        form = Putting_Technical_Form()
        shots = Putting_Technical.objects.all().order_by('-date', '-pk')
        return render(request, 'Range/Putting/PuttingTechnical.html', {'form': form,
                                                               'shots': shots})

class PuttingExperimental(View):
    def get(self, request):
        form = Putting_Experimental_Form()
        shots = Putting_Experimental.objects.all().order_by('-date', '-pk')
        return render(request, 'Range/Putting/PuttingExperimental.html', {'form': form,
                                                                  'shots': shots})

    def post(self, request):
        dataform = Putting_Experimental_Form(request.POST)
        if dataform.is_valid():
            dataform.save()
        form = Putting_Experimental_Form()
        shots = Putting_Experimental.objects.all().order_by('-date', '-pk')
        return render(request, 'Range/Putting/PuttingExperimental.html', {'form': form,
                                                                  'shots': shots})
