from django.shortcuts import render


def ui_app(request):
    return render(request, 'ui_app/ui_app.html', {})


def calibrate(request):
    return render(request, 'ui_app/calibrate.html', {})
