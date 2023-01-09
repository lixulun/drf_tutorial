from django.urls import path, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("snippets", views.SnippetViewSet, basename="snippet")
router.register("users", views.UserViewSet, basename="user")


urlpatterns = [path("", include(router.urls))]
