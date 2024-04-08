from flask import Flask, render_template, request, redirect
from segment.predict import predict, test_mp4
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', result=False)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        from segment.delete import clear_folder
        clear_folder("runs/predict-seg")

        from datetime import datetime
        history = "history/" + datetime.now().strftime('%Y%m%d%H%M%S')
        os.mkdir(history)
        if file.filename.split('.')[-1] in ["jpg", "jpeg", "png", 'JPG', 'JPEG', 'PNG']:
            file.save(os.path.join('static', 'view.jpg'))
            file.save(os.path.join(history, 'input.jpg'))

            if file.filename.split('.')[-1] == "png":
                from PIL import Image
                img = Image.open(os.path.join('static', 'view.jpg'))
                img = img.convert('RGB')
                img.save(os.path.join('static', 'view.jpg'))
                img.save(os.path.join(history, 'input.jpg'))

            predict(history)
            return render_template('index.html', result=True, video=False)
        else:
            file.save(os.path.join('static', 'view.mp4'))
            file.save(os.path.join(history, 'input.mp4'))

            test_mp4(history)

            from segment.to_h264 import video_trans_size
            video_trans_size('static/view.mp4', 'static/viewh264.mp4')

            return render_template('index.html', result=True, video=True)


if __name__ == '__main__':
    app.run(debug=True, port=1145)
