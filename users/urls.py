from django.urls import path
from users.views import SAMLRedirectAPIView

urlpatterns = [
    path('callback/', SAMLRedirectAPIView.as_view(), name='callback')
]
