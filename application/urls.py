from django.urls import path
from .views import *

from .views import *

urlpatterns = [
    path('', index),
    path('<path:path>', index),
]