from django.http import HttpResponse


def index(request):
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")

def hello(request):
    return HttpResponse("Hello World!")

def hello2(request):
    return HttpResponse("Hello 2!!")