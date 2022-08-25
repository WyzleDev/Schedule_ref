from django.shortcuts import render
from django.views.generic import TemplateView
from schedule.models import Lesson, TimeTable, Group


class IndexPage(TemplateView):
    def get(self, request, group):
        lessons = Lesson.objects.filter(group__abbreviation_on_eng=group)
        time_tables = TimeTable.objects.all()

        learn_days = ['Понедельник', "Вторник", "Среда", "Четверг", "Пятница"]
        lessons_and_info = zip(lessons, time_tables)

        # forming context to pass into django template
        context = {'lessons_and_info': lessons_and_info, "learn_days": learn_days}
        return render(request, 'index.html', context=context)
