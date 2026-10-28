from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    dashboard,
    login_view,
    CategoryViewSet,
    TicketViewSet,
)

router = DefaultRouter()
router.register(
    "categories",
    CategoryViewSet,
    basename="categories"
)
router.register(
    "tickets",
    TicketViewSet,
    basename="tickets"
)

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("login/", login_view, name="login"),
    path("api/", include(router.urls)),
]
