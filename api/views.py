from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

from .serializers import LessonSerializer, ProfessorSerializer, NewsSerializer

from schedule.models import Lesson, Professor
from news.models import Post


@permission_classes([AllowAny])
class LessonViewSet(APIView):
    def get(self, request, even_week: str, group_name: str):
        lessons = Lesson.objects.filter(
            time_table__lesson__even_week=even_week, time_table__lesson__group__name=group_name)
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)


@permission_classes([AllowAny])
class exactProfessorViewSet(APIView):
    def get(self, request, id: int):
        professor = Professor.objects.filter(lesson__professor__id=id)
        serializer = ProfessorSerializer(professor, many=True)
        return Response(serializer.data)


@permission_classes([AllowAny])
class ProfessorsViewSet(APIView):
    def get(self, request):
        professors = Professor.objects.all()
        serializer = ProfessorSerializer(professors, many=True)
        return Response(serializer.data)


@permission_classes([AllowAny])
class NewsViewSet(APIView):
    def get(self, request):
        news = Post.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)
