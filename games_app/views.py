import random
from django.http import HttpResponse
import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)



def eagle(request):
    game_list = ['орел', 'решка']
    response = random.choice(game_list)
    logger.info(f'Значение: {response}')
    return HttpResponse(response)


def cube(request):
    cube_value = random.randint(1, 6)
    logger.info(f'Кубик выпал стороной: {cube_value}')
    return HttpResponse(cube_value)


def random_number(request):
    number = random.randint(0, 100)
    logger.info(f'Случайное число: {number}')
    return HttpResponse(number)
