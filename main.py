from flask import Flask,render_template,jsonify

app = Flask(__name__)
JOBS=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Mumbai',
    'salary':'Rs 5,00,000',
  },
  {
    'id':2,
    'title':'Machine Learning Engineer',
    'location':'Hyderabad',
    'salary':'Rs 9,00,000',
  },
  {
    'id':3,
    'title':'Data Scientist',
    'location':'Hyderabad',
    'salary':'Rs 10,00,000',
  },
]

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


@app.route("/")
def hello_world():
  return render_template("home.html",
                         jobs=JOBS)

if(__name__)=='__main__':
  app.run(host='0.0.0.0', debug=True)
  