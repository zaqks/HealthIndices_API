from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from datetime import datetime

from django.shortcuts import render
from model_app.ai.ai import model, calc_bri


def get_bri_json(request):
    widths, heights = [], []

    titles = ['Original 1', 'Original 2', 'Mask 1',
              'Mask 2', 'Ellipse 1', 'Ellipse 2']

    imgs = []
    masks = []
    curves = []

    # Get the files from the request
    fs = FileSystemStorage()
    files = request.FILES

    # Save each file
    for index, file in enumerate(files.values()):

        # Generate filename with current datetime
        current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = fs.save(f"{current_datetime}_{index}.jpg", file)

        imgs.append(fs.url(filename))
        masks.append(fs.url(filename.split('.')[0] + '_mask.png'))
        curves.append(fs.url(filename.split('.')[0] + '_lines.png'))

        ########################################
        # MAKE THE PREDICTIONS
        model.set_body(fs.path(filename))
        #
        heights.append(model.get_body_height())
        widths.append(model.get_body_width(level=0.45))
        #
        model.draw_markers(level=0.45)

    rslt_urls = imgs + masks + curves
    rslt_urls = {titles[_]: rslt_urls[_] for _ in range(len(rslt_urls))}

    p, h, bri = calc_bri(widths, heights)

    return JsonResponse({'urls': rslt_urls,
                         'bri': round(bri, 1),
                         #
                         'p': p, 'h': h
                         #
                         })


@csrf_exempt
@require_http_methods(["POST"])
def model_app(request):
    return get_bri_json(request)


@csrf_exempt
@require_http_methods(["POST"])
def calibrate(request):
    fs = FileSystemStorage()
    files = request.FILES

    # Save each file
    for index, file in enumerate(files.values()):

        # Generate filename with current datetime
        current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = fs.save(f"{current_datetime}_{index}.jpg", file)

        # calibrate
        model.calibrate(fs.path(filename), 179)

        with open('calibration.txt', 'w') as f:
            f.write(f"{model.resize_factor}")

    return JsonResponse({})
