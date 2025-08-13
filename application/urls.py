from django.urls import path
from .views import *

from .views import *

urlpatterns = [
    path('', FrontendAppView.as_view(), name='home'),
]