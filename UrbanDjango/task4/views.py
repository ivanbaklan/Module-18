from django.shortcuts import render


def platform_view(request):
    return render(request, "fourth_task/platform.html")


def game_view(request):
    return render(
        request,
        "fourth_task/games.html",
        context={"games": ["Atomic Heart", "Cyberpunk 2077", "PayDay 2"]}
    )


def cart_view(request):
    return render(request, "fourth_task/cart.html")
