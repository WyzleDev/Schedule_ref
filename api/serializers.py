from importlib.resources import read_binary
from tabnanny import verbose
from rest_framework.validators import UniqueValidator
from rest_framework import serializers

from schedule.models import Lesson, Professor


class LessonSerializer(serializers.ModelSerializer):
    name = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )
    group = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
    )
    auditory = serializers.SlugRelatedField(
        slug_field='number',
        read_only=True,
    )
    professor = serializers.StringRelatedField(
        read_only=True,
    )
    from_until = serializers.CharField(
        source='time_table',
        read_only=True,
    )
    lesson_type = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
    )
    day = serializers.CharField(
        source='get_day_display',
        read_only=True,
    )

    class Meta:
        model = Lesson
        exclude = ['id', 'even_week']


class ProfessorSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField(
        read_only=True
    )
    surname = serializers.StringRelatedField(
        read_only=True,
    )
    patronymic = serializers.StringRelatedField(
        read_only=True,
    )
    position = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
    )
    email = serializers.EmailField(
        read_only=True,
    )
    phone = serializers.CharField(
        read_only=True,
    )
    building = serializers.StringRelatedField(
        read_only=True,
    )
    auditory = serializers.SlugRelatedField(
        slug_field='number',
        read_only=True,
    )

    class Meta:
        model = Professor
        exclude = ['id']
