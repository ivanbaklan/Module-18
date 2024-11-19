from django.shortcuts import render
from django.views.generic import TemplateView


def function_view(request):
    return render(request, "second_task/func_template.html")


class ClassView(TemplateView):
    template_name = "second_task/class_template.html"
