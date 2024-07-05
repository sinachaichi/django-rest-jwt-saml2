from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import logging

User = get_user_model()

logger = logging.getLogger(__name__)


class SAMLRedirectAPIView(APIView):
    def get(self, request):
        session_data = dict(request.session.items())
        user_id = session_data.get('_auth_user_id')
        if user_id:
            try:
                user = User.objects.get(id=int(session_data['_auth_user_id']))
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
            except:
                return Response({'detail': 'Authentication failed'}, status=401)
        else:
            return Response({'detail': 'No user credentials in response received'}, status=400)
            
