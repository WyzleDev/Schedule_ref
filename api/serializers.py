from rest_framework import serializers
from schedule.models import Year, Week, Day, Building, Professor, Group, Lesson, TimeTable


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
    title = serializers.CharField(read_only=True)
    week = WeekSerializer(read_only=True)
    day = DaySerializer(read_only=True)
    professor = ProfessorSerializer(read_only=True)
    building = BuildingSerializer(read_only=True)
    group = GroupSerializer(read_only=True)

    class Meta:
        model = Lesson
        exclude = ['id']


class TimeTableSerializer(serializers.ModelSerializer):
    time_from = serializers.TimeField(read_only=True)
    time_to = serializers.TimeField(read_only=True)
    lesson = LessonSerializer(read_only=True)

    class Meta:
        model = TimeTable
        exclude = ['id']
