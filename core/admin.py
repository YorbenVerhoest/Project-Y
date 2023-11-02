from django.contrib import admin
from core import models as core

@admin.register(core.BreastfeedRegistration)
class BreastfeedRegistrationAdmin(admin.ModelAdmin):
    list_display = ["start_time", "end_time", "breast_side", "baby"]
    raw_id_fields = ["baby"]

    fieldsets = (
        (None, {
            'fields': ('baby',)
        }),
        ('Basic info', {
            'fields': (('start_time', 'end_time'))
        }),
        ('Breastfeed info', {
            'fields': ('breast_side',)
        }),
       
    )
    
admin.site.register(core.Baby)
admin.site.register(core.FoodRegistration)
admin.site.register(core.ContractionRegistration)
admin.site.register(core.DiaperRegistration)
admin.site.register(core.Measurement)