import youtube_dl
from django.conf import settings
from django.core.mail import send_mail
from youtubedll.celery import app


@app.task
def download_song(video_url, email):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'media/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url)
        filename = info['title']
        send_mail(
            'Download link',
            'http://127.0.0.1:8000/media/' +
            filename.replace(" ", "%20") + '.mp3',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False
        )
