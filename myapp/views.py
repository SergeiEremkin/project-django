from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    html = "<h1>Добро пожаловать на мой первый сайт на Django</h1>" \
           "<p>Это главная страница на которой я написал эту информацию.</p>"
    logger.info(f'Показана информация: {html}')
    return HttpResponse(html)


def about(request):
    html = "<h1>Это страница обо мне</h1>" \
           "<p>Меня зовут Сергей. Я хочу стать программистом. Для этого постоянно получаю новые знания и пишу код. </p>"
    logger.info(f'Показана информация: {html}')
    return HttpResponse(html)
