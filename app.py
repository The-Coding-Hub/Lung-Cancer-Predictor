# Importing Required Packages
from flask import Flask, render_template, request
import pickle

# Initializing Flask App
app = Flask(__name__)

# Opening Model.pkl File
file = open('model.pkl', 'rb')
clf = pickle.load(file)
file.close()

# Route: Home Page
@app.route('/', methods=['GET', 'POST'])
def home():
  home = "active"
  about = ""
  if (request.method == 'POST'):
    smoke = request.form['smoke']
    radonExpo = request.form['radonExpo']
    alchohol = request.form['alchohol']
    bloodCough = request.form['bloodCough']
    breatheDiff = request.form['breatheDiff']
    chestPain = request.form['chestPain']
    inputFeatures = [smoke, radonExpo, alchohol, bloodCough, breatheDiff, chestPain]
    infProb = clf.predict_proba([inputFeatures])[0][1]
    return render_template('result.html', inf=round(infProb*100))
  return render_template('index.html', home=home, about=about)

# Route: About Page
@app.route('/about')
def about():
  home = ""
  about = "active"
  return render_template('about.html', home=home, about=about)

# Running the app
if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0")
