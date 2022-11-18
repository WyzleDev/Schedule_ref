from django.shortcuts import render
from django.views.generic import TemplateView
from schedule.models import Lesson, Group


class IndexPage(TemplateView):
    def get(self, request, group):
        lessons = Lesson.objects.filter(group__abbreviation_on_eng=group)

        learn_days = ['Понедельник', "Вторник", "Среда", "Четверг", "Пятница"]
        lessons_and_info = lessons
        # forming context to pass into django template
        context = {'lessons_and_info': lessons_and_info,
                   "learn_days": learn_days}
        return render(request, 'index.html', context=context)
