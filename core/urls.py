from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core import api

app_name = 'core'

router = DefaultRouter()
router.register(r'registrations', api.BreastfeedRegistrationViewSet, basename="BreastfeedRegistrationViewSet")

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/login/', api.UserLoginView.as_view(), name='user-login'),
    path('api/token/refresh/', api.RefreshTokenView.as_view(), name='token_refresh'),

]
