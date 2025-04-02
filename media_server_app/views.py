from django.shortcuts import redirect
from django.http import FileResponse, Http404
from django.conf import settings
import os


def media_server(request, path):

    file_path = os.path.join(settings.MEDIA_ROOT, path)

    if ".." in file_path:
        return redirect("https://giphy.com/gifs/Tgn493H3TI544")

    if not os.path.exists(file_path):
        raise Http404("Non existing file")

    return FileResponse(open(file_path, "rb"))
