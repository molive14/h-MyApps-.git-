from flask import Flask, render_template, request, url_for, redirect 


app = Flask(__name__)
app.debug = True 

interviews = [{   "interviewee" : "Melvin Olive",
                  "interviewer" : "Jai",
                  "interviewerEmail": "Jai@gmail.com",
                  "candidatesEmail" : "melvinolive100@gmail.com",
                  "type" : "intern",
                  "description" : "Developer at Chase",
                  "time" : "7-25-2019" }]



@app.route('/home')
def home():
    return render_template('homePage.html')

@app.route('/interviews', methods=["POST", "GET"])
def interview():
    if request.method == "POST": 
        print(request.form["interviewee"])
        interview =  {   "interviewee" : request.form["interviewee"],
                  "interviewer" : request.form["interviewer"],
                  "interviewerEmail": request.form["interviewee"],
                  "candidatesEmail" : request.form["candidatesEmail"],
                  "type" : request.form["type"],
                  "description" : request.form["description"],
                  "time" : request.form["time"]}
        interviews.append(interview)
        return redirect(url_for( "interview", interviews = interviews ))
    return render_template('interviews.html',interviews=interviews)

@app.route('/login')
def index():
    return render_template('login.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/candidates')
def candidates():
    return render_template('candidates.html')




if __name__== "__main__":
    app.run()

