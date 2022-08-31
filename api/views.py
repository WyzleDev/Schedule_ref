from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from schedule.models import Lesson, TimeTable, Professor
from .serializers import *


@permission_classes([IsAuthenticatedOrReadOnly])
class LessonViewSet(APIView):
    def get(self, request, group):
        lessons = Lesson.objects.filter(group__abbreviation_on_eng=group)
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)
