from django.shortcuts import render
from .forms import UserRegister


def validate_vals(username, password, repeat_password, age, info, users):
    try:
        age = int(age)
    except ValueError:
        info["error"] = "возраст должно быть числом"
        return info
    if username in users:
        info["error"] = "Пользователь уже существует"
        return info
    if password != repeat_password:
        info["error"] = "Пароли не совпадают"
        return info
    if int(age) < 18:
        info["error"] = "Вы должны быть старше 18"
        return info
    users.append(username)
    info["content"] = f"Приветствуем, {username}!"
    return info


def sign_up_by_django(request):
    users = ["user1", "user2", "user3"]
    info = {}
    if not request.method == "POST":
        info["form"] = UserRegister()
        return render(request, "fifth_task/registration_page.html", context=info)
    form = UserRegister(request.POST)
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        repeat_password = form.cleaned_data["repeat_password"]
        age = form.cleaned_data["age"]
        info = validate_vals(username, password, repeat_password, age, info, users)
        info["form"] = form
        return render(request, "fifth_task/registration_page.html", context=info)
    else:
        info["error"] = "Ошибка валидации формы"
        return render(request, "fifth_task/registration_page.html", context=info)


def sign_up_by_html(request):
    users = ["user1", "user2", "user3"]
    info = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get("age")
        info = validate_vals(username, password, repeat_password, age, info, users)
    return render(request, "fifth_task/registration_page.html", context=info)
