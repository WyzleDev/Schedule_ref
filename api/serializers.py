from rest_framework import serializers
from schedule.models import Year, Week, Day, Building, Professor, Group, Lesson, Event, Tag


class YearSerializer(serializers.ModelSerializer):
    date = serializers.CharField(
        read_only=True
    )

    class Meta:
        model = Year
        exclude = ['id']


class WeekSerializer(serializers.ModelSerializer):
    title = serializers.IntegerField(
        read_only=True
    )
    year = YearSerializer(
        read_only=True
    )
    is_even = serializers.CharField(read_only=True)

    class Meta:
        model = Week
        exclude = ['id']


class DaySerializer(serializers.ModelSerializer):
    week_day = serializers.CharField(
        read_only=True
    )

    class Meta:
        model = Day
        exclude = ['id']


class BuildingSerializer(serializers.ModelSerializer):
    address = serializers.CharField(read_only=True)
    corp = serializers.CharField(read_only=True)

    class Meta:
        model = Building
        exclude = ['id']


class ProfessorSerializer(serializers.ModelSerializer):
    surname = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    patronym = serializers.CharField(read_only=True)
    age = serializers.CharField(read_only=True)
    building = BuildingSerializer(read_only=True)

    class Meta:
        model = Professor
        exclude = ['id']


class GroupSerializer(serializers.ModelSerializer):
    abbreviation_on_ru = serializers.CharField(read_only=True)
    abbreviation_on_eng = serializers.CharField(read_only=True)
    tutor = ProfessorSerializer(read_only=True)

    class Meta:
        model = Group
        exclude = ['id']


class LessonSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    room = serializers.CharField(read_only=True)
    position = serializers.CharField(read_only=True)
    starting_time = serializers.CharField(read_only=True)
    week = WeekSerializer(read_only=True)
    day = DaySerializer(read_only=True)
    professor = ProfessorSerializer(read_only=True)
    building = BuildingSerializer(read_only=True)
    group = GroupSerializer(read_only=True)

    class Meta:
        model = Lesson
        exclude = ['id']


class TagSerializer(serializers.ModelSerializer):
    title = serializers.CharField(read_only=True)

    class Meta:
        model = Tag
        fields = ['title']


class EventSerializer(serializers.ModelSerializer):
    title = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    tags = TagSerializer(read_only=True, many=True)
    time = serializers.TimeField(read_only=True)
    date = serializers.DateField(read_only=True)
    creator = serializers.CharField(read_only=True)
    latitude = serializers.FloatField(read_only=True)
    longitude = serializers.FloatField(read_only=True)
    yandex_maps_url = serializers.URLField(read_only=True)

    class Meta:
        model = Event
        exclude = ['id']
