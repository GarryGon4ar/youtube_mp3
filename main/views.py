from django.shortcuts import render
from .tasks import download_song
from .forms import DownloadForm
from .models import Song
from django.contrib import messages


def download(request):
    form = DownloadForm()
    if request.method == "POST":
        form = DownloadForm(request.POST)
        if form.is_valid():
            video_url = form.cleaned_data.get('url')
            email = form.cleaned_data.get('email')
            full_url = request.get_host()
            download_song.delay(video_url, email, full_url)
            Song.objects.create(link=video_url, email=email)
            messages.success(request,
                             'Link for download will be sent to your email.')
            form = DownloadForm()
            return render(request, 'index.html', {'form': form})
    return render(request, "index.html", context={
        'form': form,
    })
