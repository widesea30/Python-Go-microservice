import os
from flask import Flask, request
from ctypes import cdll, c_char_p
import json


app = Flask(__name__)

# load go library
lib = cdll.LoadLibrary('./dict.so')
lib.init_dict.argtypes = [c_char_p]
lib.get_word.argtypes = [c_char_p]
lib.get_word.restype = c_char_p

app.lib = lib


@app.route('/get_topics', methods=['POST'])
def get_topics():
    if request.method == 'POST':
        # load dictionary
        path = os.getcwd() + '/data.json'  # path of data.json file
        app.lib.init_dict(c_char_p(path.encode('utf-8')))

        txt = request.json.get('text')
        result = filter_text(txt)
        return {'text': txt, 'topics': result}
    return None


def filter_text(text):
    word_list = text.split(' ')  # break text into words
    total_topics = {}
    for i in range(100):  # repeat 100x for test
        for word in word_list:
            res = (app.lib.get_word(c_char_p(word.encode('utf-8')).value).decode('utf-8'))  # get topics from go library
            topic = json.loads(res)
            keys = list(topic.keys())
            total_keys = list(total_topics.keys())
            for k in keys:
                if k in total_keys:
                    if total_topics[k] < topic[k]:
                        total_topics[k] = topic[k]
                else:
                    total_topics[k] = topic[k]
    return total_topics


if __name__ == "__main__":
    app.run(debug=True)
