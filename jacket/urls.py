from django.urls import path
from . import views

app_name = 'jacket'

urlpatterns = [
    path('', views.JacketIndex.as_view(), name='index'),
    path('<int:pk>/', views.JacketDetails.as_view(), name='details'),
    path('create/', views.JacketCreate.as_view(), name='create'),
    path('search/', views.search_results, name='search'),
    path('return/<int:jacket_id>/', views.mark_returned, name='return'),
    path('claim/<int:jacket_id>/', views.claim_jacket, name='claim'),
]
