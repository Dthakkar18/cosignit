from django.urls import path, include
from .views import home_page_user, reactpy_sample

urlpatterns = [
    path("", home_page_user, name="home_page_view"),
    path("sample", reactpy_sample, name="reactpy_sample_view")



]