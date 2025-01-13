from flask import Flask, render_template
app = Flask(__name__)
JOBS = [
    {
        'id' : 1 ,
        'title' : 'Data Analyst' ,
        'location' : 'Bengaluru,India',
        'salary' : '10,00,000'
    },
    {
        'id' : 2 ,
        'title' : 'Data Scientist' ,
        'location' : 'Delhi,India',
        'salary' : '15,00,000'
    },
    {
        'id' : 3 ,
        'title' : 'Backend Developer' ,
        'location' : 'Pune,India',
        'salary' : '6,00,000'
    },
    {
        'id' : 4 ,
        'title' : 'Full Stack' ,
        'location' : 'Remote',
        'salary' : '8,00,000'
    }
]
@app.route("/")
def home():
    return render_template('home.html', jobs = JOBS)
if __name__=="__main__" :
   app.run(host= '0.0.0.0', debug = True)