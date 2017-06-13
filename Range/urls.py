from django.conf.urls import url
from .views import Main, Woods, Hybrids, Irons, Wedges, Chipping, Putting, \
    WoodsTest, WoodsTechnical, HybridsTechnical, IronsTechnical, WedgesTechnical, \
    ChippingTechnical, PuttingTechnical

urlpatterns = [
            url(r'^$', Main.as_view(), name='RangeMain'),
            url(r'^Woods/$', Woods.as_view(), name='RangeWoods'),
            url(r'^Woods/Test/$', WoodsTest.as_view(), name='WoodsTest'),
            url(r'^Woods/Technical/$', WoodsTechnical.as_view(), name='WoodsTechnical'),
            url(r'^Hybrids/$', Hybrids.as_view(), name='RangeHybrids'),
            url(r'^Hybrids/Technical/$', HybridsTechnical.as_view(), name='HybridsTechnical'),
            url(r'^Irons/$', Irons.as_view(), name='RangeIrons'),
            url(r'^Irons/Technical/$', IronsTechnical.as_view(), name='IronsTechnical'),
            url(r'^Wedges/$', Wedges.as_view(), name='RangeWedges'),
            url(r'^Wedges/Technical/$', WedgesTechnical.as_view(), name='WedgesTechnical'),
            url(r'^Chipping/$', Chipping.as_view(), name='RangeChipping'),
            url(r'^Chipping/Technical/$', ChippingTechnical.as_view(), name='ChippingTechnical'),
            url(r'^Putting/$', Putting.as_view(), name='RangePutting'),
            url(r'^Putting/Technical/$', PuttingTechnical.as_view(), name='PuttingTechnical'),
]
