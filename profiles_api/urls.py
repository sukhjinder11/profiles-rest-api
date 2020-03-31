from django.urls import path
from profiles_api.views import HelloAPIView


urlpatterns = [
    path('', HelloAPIView.as_view()),

]
