from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def me(request):
    user = request.user
    if not user.is_authenticated:
        return Response({'authenticated': False, 'role': 'LIBRE'})
    role = 'ADMIN' if user.is_superuser else 'EDITOR' if user.is_staff else 'REGISTRADO'
    return Response({'authenticated': True, 'username': user.username, 'role': role})
