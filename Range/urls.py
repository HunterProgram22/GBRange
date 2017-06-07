from django.conf.urls import url
from .views import Main, Woods, Hybrids, Irons, Wedges, Chipping, Putting

urlpatterns = [
            url(r'^$', Main.as_view(), name='RangeMain'),
            url(r'^Woods/$', Woods.as_view(), name='RangeWoods'),
            url(r'^Hybrids/$', Hybrids.as_view(), name='RangeHybrids'),
            url(r'^Irons/$', Irons.as_view(), name='RangeIrons'),
            url(r'^Wedges/$', Wedges.as_view(), name='RangeWedges'),
            url(r'^Chipping/$', Chipping.as_view(), name='RangeChipping'),
            url(r'^Putting/$', Putting.as_view(), name='RangePutting'),
]
