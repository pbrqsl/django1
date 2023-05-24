from django.urls import path

from .views import HomePageView, AboutPageView, Something

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("something/", Something.as_view(), name="something"),
    path("", HomePageView.as_view(), name="home"),
]
