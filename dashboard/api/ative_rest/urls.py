from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("history/", views.getTradeList, name="trade-list"),
    path("actual/", views.getTradeActual, name="trade-actual"),
    path("count/", views.getnumber_of_trades, name="trade-count"),
    path("balance/", views.getbalance, name="trade-balance"),
    path("tokens/", views.getTokenNumber, name="token-number"),
]