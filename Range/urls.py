from django.conf.urls import url
from .views import Main, Base_Drill_View, MenuView


urlpatterns = [
            url(r'^$', Main.as_view(), name='RangeMain'),
            url(r'^Woods/$', MenuView.as_view(), name='RangeWoods'),
            url(r'^Woods/Test/$', Base_Drill_View.as_view(), name='WoodsTest'),
            url(r'^Woods/Technical/$', Base_Drill_View.as_view(), name='WoodsTechnical'),
            url(r'^Woods/Experimental/$', Base_Drill_View.as_view(), name='WoodsExperimental'),
            url(r'^Woods/Calibration/$', Base_Drill_View.as_view(), name='WoodsCalibration'),
            url(r'^Woods/Performance/$', Base_Drill_View.as_view(), name='WoodsPerformance'),
            url(r'^Woods/Games/$', Base_Drill_View.as_view(), name='WoodsGames'),
            url(r'^Hybrids/$', MenuView.as_view(), name='RangeHybrids'),
            url(r'^Hybrids/Test/$', Base_Drill_View.as_view(), name='HybridsTest'),
            url(r'^Hybrids/Technical/$', Base_Drill_View.as_view(), name='HybridsTechnical'),
            url(r'^Hybrids/Experimental/$', Base_Drill_View.as_view(), name='HybridsExperimental'),
            url(r'^Hybrids/Calibration/$', Base_Drill_View.as_view(), name='HybridsCalibration'),
            url(r'^Hybrids/Performance/$', Base_Drill_View.as_view(), name='HybridsPerformance'),
            url(r'^Hybrids/Games/$', Base_Drill_View.as_view(), name='HybridsGames'),
            url(r'^Irons/$', MenuView.as_view(), name='RangeIrons'),
            url(r'^Irons/Test/$', Base_Drill_View.as_view(), name='IronsTest'),
            url(r'^Irons/Technical/$', Base_Drill_View.as_view(), name='IronsTechnical'),
            url(r'^Irons/Experimental/$', Base_Drill_View.as_view(), name='IronsExperimental'),
            url(r'^Irons/Calibration/$', Base_Drill_View.as_view(), name='IronsCalibration'),
            url(r'^Irons/Performance/$', Base_Drill_View.as_view(), name='IronsPerformance'),
            url(r'^Irons/Games/$', Base_Drill_View.as_view(), name='IronsGames'),
            url(r'^Wedges/$', MenuView.as_view(), name='RangeWedges'),
            url(r'^Wedges/Test/$', Base_Drill_View.as_view(), name='WedgesTest'),
            url(r'^Wedges/Technical/$', Base_Drill_View.as_view(), name='WedgesTechnical'),
            url(r'^Wedges/Experimental/$', Base_Drill_View.as_view(), name='WedgesExperimental'),
            url(r'^Wedges/Calibration/$', Base_Drill_View.as_view(), name='WedgesCalibration'),
            url(r'^Wedges/Performance/$', Base_Drill_View.as_view(), name='WedgesPerformance'),
            url(r'^Wedges/Games/$', Base_Drill_View.as_view(), name='WedgesGames'),
            url(r'^Chipping/$', MenuView.as_view(), name='RangeChipping'),
            url(r'^Chipping/Test/$', Base_Drill_View.as_view(), name='ChippingTest'),
            url(r'^Chipping/Technical/$', Base_Drill_View.as_view(), name='ChippingTechnical'),
            url(r'^Chipping/Experimental/$', Base_Drill_View.as_view(), name='ChippingExperimental'),
            url(r'^Chipping/Calibration/$', Base_Drill_View.as_view(), name='ChippingCalibration'),
            url(r'^Chipping/Performance/$', Base_Drill_View.as_view(), name='ChippingPerformance'),
            url(r'^Chipping/Games/$', Base_Drill_View.as_view(), name='ChippingGames'),
            url(r'^Putting/$', MenuView.as_view(), name='RangePutting'),
            url(r'^Putting/Test/$', Base_Drill_View.as_view(), name='PuttingTest'),
            url(r'^Putting/Technical/$', Base_Drill_View.as_view(), name='PuttingTechnical'),
            url(r'^Putting/Experimental/$', Base_Drill_View.as_view(), name='PuttingExperimental'),
            url(r'^Putting/Calibration/$', Base_Drill_View.as_view(), name='PuttingCalibration'),
            url(r'^Putting/Performance/$', Base_Drill_View.as_view(), name='PuttingPerformance'),
            url(r'^Putting/Games/$', Base_Drill_View.as_view(), name='PuttingGames'),
]
