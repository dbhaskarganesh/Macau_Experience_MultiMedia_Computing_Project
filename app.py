from flask import Flask, render_template, request, jsonify
from PyDictionary import PyDictionary
from spellchecker import SpellChecker

app = Flask(__name__, template_folder='static/templates')

app = Flask(__name__, template_folder='static/templates')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about_macau')
def about_macau():
    return render_template('about_macau.html')

@app.route('/history_macau')
def history_macau():
    return render_template('history_macau.html')

@app.route('/image')
def image():
    return render_template('image.html')

@app.route('/macau')
def macau():
    return render_template('macau.html')

@app.route('/places_macau')
def places_macau():
    return render_template('places_macau.html')

@app.route('/sound')
def sound():
    return render_template('sound.html')

@app.route('/spelling_checker', methods=['GET', 'POST'])
def spelling_checker():
    if request.method == 'POST':
        word = request.form.get('word')
        spell = SpellChecker()
        dictionary = PyDictionary()
        misspelled = spell.unknown([word])
        word_info = {
            'spell_check': 'Correct' if not misspelled else 'Incorrect',
            'meanings': dictionary.meaning(word),
            'synonyms': dictionary.synonym(word),
            'antonyms': dictionary.antonym(word)
        }
        # Concatenating information into a string
        response_text = word_info['spell_check']
        if word_info['meanings']:
            response_text += " | Definitions: " + ", ".join(word_info['meanings'])
        if word_info['synonyms']:
            response_text += " | Synonyms: " + ", ".join(word_info['synonyms'])
        if word_info['antonyms']:
            response_text += " | Antonyms: " + ", ".join(word_info['antonyms'])
        return response_text
    return render_template('spelling_checker.html')

if __name__ == '__main__':
    app.run(debug=True)
