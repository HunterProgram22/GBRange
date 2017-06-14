from django.conf.urls import url
from .views import Main, Woods, Hybrids, Irons, Wedges, Chipping, Putting, \
    WoodsTest, HybridsTest, IronsTest, WedgesTest, ChippingTest, PuttingTest, \
    WoodsTechnical, HybridsTechnical, IronsTechnical, WedgesTechnical, \
    ChippingTechnical, PuttingTechnical, \
    WoodsExperimental, WedgesExperimental, PuttingExperimental, HybridsExperimental, \
    IronsExperimental, ChippingExperimental, \
    WoodsCalibration, WedgesCalibration, PuttingCalibration, HybridsCalibration, \
    IronsCalibration, ChippingCalibration, \
    WoodsPerformance, WedgesPerformance, PuttingPerformance, HybridsPerformance, \
    IronsPerformance, ChippingPerformance, \
    WoodsGames, WedgesGames, PuttingGames, HybridsGames, IronsGames, ChippingGames


urlpatterns = [
            url(r'^$', Main.as_view(), name='RangeMain'),
            url(r'^Woods/$', Woods.as_view(), name='RangeWoods'),
            url(r'^Woods/Test/$', WoodsTest.as_view(), name='WoodsTest'),
            url(r'^Woods/Technical/$', WoodsTechnical.as_view(), name='WoodsTechnical'),
            url(r'^Woods/Experimental/$', WoodsExperimental.as_view(), name='WoodsExperimental'),
            url(r'^Woods/Calibration/$', WoodsCalibration.as_view(), name='WoodsCalibration'),
            url(r'^Woods/Performance/$', WoodsPerformance.as_view(), name='WoodsPerformance'),
            url(r'^Woods/Games/$', WoodsGames.as_view(), name='WoodsGames'),
            url(r'^Hybrids/$', Hybrids.as_view(), name='RangeHybrids'),
            url(r'^Hybrids/Test/$', HybridsTest.as_view(), name='HybridsTest'),
            url(r'^Hybrids/Technical/$', HybridsTechnical.as_view(), name='HybridsTechnical'),
            url(r'^Hybrids/Experimental/$', HybridsExperimental.as_view(), name='HybridsExperimental'),
            url(r'^Hybrids/Calibration/$', HybridsCalibration.as_view(), name='HybridsCalibration'),
            url(r'^Hybrids/Performance/$', HybridsPerformance.as_view(), name='HybridsPerformance'),
            url(r'^Hybrids/Games/$', HybridsGames.as_view(), name='HybridsGames'),
            url(r'^Irons/$', Irons.as_view(), name='RangeIrons'),
            url(r'^Irons/Test/$', IronsTest.as_view(), name='IronsTest'),
            url(r'^Irons/Technical/$', IronsTechnical.as_view(), name='IronsTechnical'),
            url(r'^Irons/Experimental/$', IronsExperimental.as_view(), name='IronsExperimental'),
            url(r'^Irons/Calibration/$', IronsCalibration.as_view(), name='IronsCalibration'),
            url(r'^Irons/Performance/$', IronsPerformance.as_view(), name='IronsPerformance'),
            url(r'^Irons/Games/$', IronsGames.as_view(), name='IronsGames'),
            url(r'^Wedges/$', Wedges.as_view(), name='RangeWedges'),
            url(r'^Wedges/Test/$', WedgesTest.as_view(), name='WedgesTest'),
            url(r'^Wedges/Technical/$', WedgesTechnical.as_view(), name='WedgesTechnical'),
            url(r'^Wedges/Experimental/$', WedgesExperimental.as_view(), name='WedgesExperimental'),
            url(r'^Wedges/Calibration/$', WedgesCalibration.as_view(), name='WedgesCalibration'),
            url(r'^Wedges/Performance/$', WedgesPerformance.as_view(), name='WedgesPerformance'),
            url(r'^Wedges/Games/$', WedgesGames.as_view(), name='WedgesGames'),
            url(r'^Chipping/$', Chipping.as_view(), name='RangeChipping'),
            url(r'^Chipping/Test/$', ChippingTest.as_view(), name='ChippingTest'),
            url(r'^Chipping/Technical/$', ChippingTechnical.as_view(), name='ChippingTechnical'),
            url(r'^Chipping/Experimental/$', ChippingExperimental.as_view(), name='ChippingExperimental'),
            url(r'^Chipping/Calibration/$', ChippingCalibration.as_view(), name='ChippingCalibration'),
            url(r'^Chipping/Performance/$', ChippingPerformance.as_view(), name='ChippingPerformance'),
            url(r'^Chipping/Games/$', ChippingGames.as_view(), name='ChippingGames'),
            url(r'^Putting/$', Putting.as_view(), name='RangePutting'),
            url(r'^Putting/Test/$', PuttingTest.as_view(), name='PuttingTest'),
            url(r'^Putting/Technical/$', PuttingTechnical.as_view(), name='PuttingTechnical'),
            url(r'^Putting/Experimental/$', PuttingExperimental.as_view(), name='PuttingExperimental'),
            url(r'^Putting/Calibration/$', PuttingCalibration.as_view(), name='PuttingCalibration'),
            url(r'^Putting/Performance/$', PuttingPerformance.as_view(), name='PuttingPerformance'),
            url(r'^Putting/Games/$', PuttingGames.as_view(), name='PuttingGames'),
]
