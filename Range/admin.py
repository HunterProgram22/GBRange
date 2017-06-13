from django.contrib import admin
from .models import Woods_Test, Woods_Technical, \
    Hybrids_Technical, Irons_Technical, Wedges_Technical, Chipping_Technical, \
    Putting_Technical

admin.site.register(Woods_Test)
admin.site.register(Woods_Technical)
admin.site.register(Hybrids_Technical)
admin.site.register(Irons_Technical)
admin.site.register(Wedges_Technical)
admin.site.register(Chipping_Technical)
admin.site.register(Putting_Technical)
