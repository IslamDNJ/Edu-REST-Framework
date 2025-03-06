from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Women
from .serializers import WomenSerializer

# Реализация сериализатора
class WomenAPIView(APIView):
    def get(self, request):
        # Формирование списка из объекта классов Women
        w = Women.objects.all()
        # Передача параметров на Сериализатор
        return Response({'posts': WomenSerializer(w, many=True).data}) # many - для списка записей

    def post(self, request):
        # Проверка на корректность в POST запросе title, content, cat_id
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # В случае отсутствия одного из значений, заданных в serializers.py, ошибка не выдается, а возвращается JSON файл:
        # {
        #     "title":[
        #         "Обязательное поле."
        #     ],
        #     "time_create": [
        #         "Обязательное поле."
        #     ],
        #     "time_update": [
        #         "Обязательное поле."
        #     ]
        # }

        post_new = Women.objects.create(
            title=request.data['title'],            # request.data используется для получения данных
            content=request.data['content'],        # которые были отправлены в запросе 
            cat_id=request.data['cat_id']           # POST, PUT или PATCH
        )
        return Response({'post': WomenSerializer(post_new).data})