from django.urls import path, include
from .views import Humanlist, Humandetail, Humancreate, HumanUpdate, HumanDelete

urlpatterns = [
    path('list/', Humanlist.as_view(), name='list'),
    path('detail/<int:pk>', Humandetail.as_view(), name='detail'),
    path('create/', Humancreate.as_view(), name='create'),
    path('update/<int:pk>', HumanUpdate.as_view(), name = 'update'),
    path('delete/<int:pk>', HumanDelete.as_view(), name = 'delete'),
]
