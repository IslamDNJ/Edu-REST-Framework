# from rest_framework import generics
from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Women
from .serializers import WomenSerializer

# Без сериализатора
class WomenAPIView(APIView):
    def get(self, request):
        lst = Women.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self, request):
        post_new = Women.objects.create(
            title=request.data['title'],            # request.data используется для получения данных
            content=request.data['content'],        # которые были отправлены в запросе 
            cat_id=request.data['cat_id']           # POST, PUT или PATCH
        )
        return Response({'post': model_to_dict(post_new)})

# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
