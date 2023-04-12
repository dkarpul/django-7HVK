from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'streamlit-home'),
    # path('<path:resource>', views.streamlitproxy, name = 'streamlit-proxy'),
    # path('lt/(?P<path>.*)', views.djproxy, name='streamlit'),
]
    
