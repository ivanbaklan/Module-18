from django.shortcuts import render


def platform_view(request):
    return render(request, "third_task/platform.html")


def game_view(request):
    game_list = ["Atomic Heart", "Cyberpunk 2077", "PayDay 2"]
    return render(request, "third_task/games.html", context={"game_list": game_list})


def cart_view(request):
    return render(request, "third_task/cart.html")
