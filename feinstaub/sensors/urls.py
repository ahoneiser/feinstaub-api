# coding=utf-8
from rest_framework import routers
from django.urls import include, path
from .views import (
    NodeView,
    PostSensorDataView,
    SensorDataView,
    SensorView,
    StatisticsView,
    NowView,
)
from main.views import UsersView


router = routers.DefaultRouter()
router.register(
    r"push-sensor-data", PostSensorDataView, basename="push-sensor-data"
)
router.register(r"node", NodeView)
router.register(r"sensor", SensorView)
router.register(r"data", SensorDataView)
router.register(r"statistics", StatisticsView, basename="statistics")
router.register(r"user", UsersView)
router.register(r"now", NowView)

urlpatterns = [
    path("", view=include(router.urls)),
]
