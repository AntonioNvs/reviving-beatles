from flask import Flask, request
from model import create_a_music_with_model

app = Flask(__name__)

@app.route('/get-music')
def get_music():
    print('get-music received of success!')
    title = request.args.get('title')
    size = request.args.get('size')

    predicted = create_a_music_with_model(title, int(size))

    list_predicted = predicted.split('\n')
    list_predicted = [i.replace('\r', '') for i in list_predicted]

    list_predicted.pop(0)
    list_predicted.pop(len(list_predicted)-1)

    return {
        'body': list_predicted
    }


app.run()