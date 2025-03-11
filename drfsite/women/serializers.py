from rest_framework import serializers

from .models import Women


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = "__all__"

# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

# # Кодирование JSON информации
# def encode():
#     model = WomenModel("Angelina Jolie", "Content: Angelina Jolie")
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep="\n")
#     json = JSONRenderer().render(model_sr.data)
#     print(json)


# # Декодирование JSON инфомации
# def decode():
#     stream = io.BytesIO(
#         b'{"title":"Angelina Jolie", "content":"Content: Angelina Jolie"}'
#     )
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
