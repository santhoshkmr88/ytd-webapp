from flask import Flask, request, render_template
from pytube import YouTube
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def download_video():
    # Get the URL of the YouTube video from the request
    url = request.form['url']

    # Create a YouTube object and download the video
    yt = YouTube(url)
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
    video.download(downloads_folder)

    return "Video downloaded successfully"


if __name__ == '__main__':
    # noinspection PyTypeChecker
    app.run(host='0.0.0.0', port=8080, debug=False)
