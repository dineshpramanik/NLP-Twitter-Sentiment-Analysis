from flask import Flask, render_template, url_for, request
import pickle

#Load the model
model = 'twitter-sentiment-analysis.pkl'
clf = pickle.load(open(model, 'rb'))
tf = pickle.load(open('transform.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        vect = tf.transform(data).toarray()
        my_prediction = clf.predict(vect)

    return render_template('predict.html', prediction = my_prediction)

if __name__ == '__main__':
    app.run(debug=True)