from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import User
from .serializers import *

@api_view(['GET'])
def api_list(request):
    if request.method == 'GET':
        data = User.objects.all()

		# will convert before we return it as a response
        serializer = UserSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)
