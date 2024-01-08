from rest_framework.response import Response
from rest_framework.views import APIView
from SimpleAPI.settings import BASE_DIR


# Create your views here.
class SimpleRequest(APIView):
    def get(self, request):
        return Response({"message": f"{BASE_DIR}"})