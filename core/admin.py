from django.contrib import admin
from core import models as core

admin.site.register(core.Baby)
admin.site.register(core.Measurement)

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
    
@admin.register(core.FoodRegistration)
class FoodRegistrationAdmin(admin.ModelAdmin):
    list_display = ["start_time", "end_time", "baby"]
    raw_id_fields = ["baby"]

    fieldsets = (
        (None, {
            'fields': ('baby',)
        }),
        ('Basic info', {
            'fields': (('start_time', 'end_time'))
        }),
       
    )

@admin.register(core.ContractionRegistration)
class ContractionRegistrationAdmin(admin.ModelAdmin):
    list_display = ["start_time", "end_time", "baby"]
    raw_id_fields = ["baby"]

    fieldsets = (
        (None, {
            'fields': ('baby',)
        }),
        ('Basic info', {
            'fields': (('start_time', 'end_time'))
        }),
       
    )


@admin.register(core.DiaperRegistration)
class DiaperRegistrationAdmin(admin.ModelAdmin):
    list_display = ["start_time", "end_time", "baby"]
    raw_id_fields = ["baby"]

    fieldsets = (
        (None, {
            'fields': ('baby',)
        }),
        ('Basic info', {
            'fields': (('start_time', 'end_time'))
        }),
       
    )

