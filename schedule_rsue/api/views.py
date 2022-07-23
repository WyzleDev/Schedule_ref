from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CreateUserSerializer, LessonSerializer
from schedule import models


class LessonView(APIView):
    def get(self, request, even_week, group_name):
        print(group_name)
        lessons = models.Lesson.objects.filter(timetable__lesson__even_week=even_week, timetable__lesson__group__name=group_name)
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)


class ProfessorView(APIView):
    def get(self, request):
        last_name = request.data.get('last_name')
        lessons = models.Lesson.objects.filter(
            professor__last_name=last_name,
        )
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = CreateUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({'message': 'пользователь успешно зарегистрирован'},
                    status=status.HTTP_201_CREATED)
