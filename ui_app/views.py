from django.shortcuts import render
from ui_app.models import Score


def ui_app(request):
    return render(request, 'ui_app/ui_app.html', {})


def calibrate(request):
    return render(request, 'ui_app/calibrate.html', {})


def score(request):
    data = Score.objects.all()
    data = list(data)
    data.reverse()

    return render(request, 'ui_app/score.html', {
        'scores': data
    })
