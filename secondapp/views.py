from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random
import logging
from .models import Coin
from .forms import RandomGames


logger = logging.getLogger(__name__)


def my_log(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f'Была вызвана функция {func.__name__}')
        return result
    return wrapper


@my_log
def coin(request, count=1):
    coin_sides = ['орел', 'решка']
    result = []
    for i in range(count):
        result.append(random.choice(coin_sides))
    return render(request, 'secondapp/index.html', {'result': result})
def coin_statistic(request, n: int):
    return JsonResponse(Coin.get_last_n_flip(n), json_dumps_params={'ensure_ascii': False})

@my_log
def cube(request, count=1):
    result = []
    for i in range(count):
        result.append(random.randint(1, 6))
    return render(request, 'secondapp/index.html', {'result': result})

@my_log
def rand_num(request, count=1):
    result = []
    for i in range(count):
        result.append(random.randint(1, 100))
    return render(request, 'secondapp/index.html', {'result': result})


def random_games(request):
    if request.method == 'POST':
        form = RandomGames(request.POST)
        if form.is_valid():
            game = form.cleaned_data['game']
            count = form.cleaned_data['count']
            if game == 'coin':
                return coin(request, count)
            elif game == 'cube':
                return cube(request, count)
            else:
                return rand_num(request, count)
    else:
        form = RandomGames()
    return render(request, 'secondapp/random_games.html', {'form': form})