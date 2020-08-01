
from django.urls import path, include
from . import views
from .views import HistoryView,ContactsView,PricesView,HoursView,PostView

urlpatterns = [
  #  path('', views.home, name="home"),

    path('history.html/', HistoryView.as_view(), name="history"),
    path('contacts.html/', ContactsView.as_view(), name="contacts"),
    path('prices.html/', PricesView.as_view(), name="prices"),
    path('hours.html/' , HoursView.as_view(), name="hours"),
    path('', PostView.as_view(), name = "home"),
]