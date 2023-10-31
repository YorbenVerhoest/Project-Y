from django.contrib import admin
from core import models as core

# Register your models here.
# @admin.register(core.TimeRegistration)
# class TimeRegistrationAdmin(admin.ModelAdmin):
#     list_display = ["registration_type", "start_time", "end_time", "user"]
#     raw_id_fields = ["user"]

#     fieldsets = (
#         (None, {
#             'fields': ( 'registration_type', 'user')
#         }),
#         ('Basic info', {
#             'fields': (('start_time', 'end_time'))
#         }),
#         ('Breastfeed info', {
#             'fields': ('breast_side',)
#         }),
       
#     )
    
admin.site.register(core.Baby)
admin.site.register(core.BreastfeedRegistration)
admin.site.register(core.FoodRegistration)
admin.site.register(core.ContractionRegistration)
admin.site.register(core.DiaperRegistration)
admin.site.register(core.Measurement)