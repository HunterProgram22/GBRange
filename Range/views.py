from django.shortcuts import render
from django.views import View



class Main(View):
    def get(self, request):
        return render(request, 'Range/main.html', {})

class Woods(View):
    def get(self, request):
        return render(request, 'Range/Woods.html', {})

class WoodsTest(View):
    def get(self, request):
        return render(request, 'Range/WoodsTest.html', {})

class Hybrids(View):
    def get(self, request):
        return render(request, 'Range/Hybrids.html', {})

class Irons(View):
    def get(self, request):
        return render(request, 'Range/Irons.html', {})

class Wedges(View):
    def get(self, request):
        return render(request, 'Range/Wedges.html', {})

class Chipping(View):
    def get(self, request):
        return render(request, 'Range/Chipping.html', {})

class Putting(View):
    def get(self, request):
        return render(request, 'Range/Putting.html', {})
