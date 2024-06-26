from django.urls import path, include
from .views import home_page, reactpy_sample

urlpatterns = [
    path("", home_page, name="home_page_view"),
    path("sample", reactpy_sample, name="reactpy_sample_view")



]