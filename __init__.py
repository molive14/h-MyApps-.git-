from flask import Flask, render_template, request, url_for, redirect 
import json

app = Flask(__name__)
app.debug = True 

interviews = [{   }]




@app.route('/home')
def home():
    return render_template('homePage.html')

@app.route('/interviews', methods=["POST", "GET"])
def interview():
    if request.method == "POST": 
        print(request.form["interviewee"])
        interview =  {   "interviewee" : request.form["interviewee"],
                  "interviewer" : request.form["interviewer"],
                  "interviewerEmail": request.form["interviewerEmail"],
                  "candidatesEmail" : request.form["candidatesEmail"],
                  "job" : request.form["job"],
                  "description" : request.form["description"],
                  "time" : request.form["time"]}
        interviews.append(interview)
     
        # interview=json.dumps(interview)

        print(interview)

        print(type(interview))
        with open("interviews.json", 'r') as f:
            # f.append(interview)
            current_interview_list = json.loads(f.read())
        with open("interviews.json", 'w') as f:
            current_interview_list[interview["time"]] = interview
            print(current_interview_list)
            json.dump(current_interview_list, f)
            
        return redirect(url_for( "interview", interviews = interviews,  ))
    return render_template('interviews.html',interviews=interviews, )

@app.route('/candidates', methods=["POST", "GET"])
def candidates():
    if request.method == "POST": 
       print(request.form["interviewee"])
       interview =  {   "interviewee" : request.form["interviewee"],
                  "interviewer" : request.form["interviewer"],
                  "interviewerEmail": request.form["interviewerEmail"],
                  "candidatesEmail" : request.form["candidatesEmail"],
                  "job" : request.form["job"],
                  "description" : request.form["description"],
                  "time" : request.form["time"]}
       interviews.append(interview)

       return redirect(url_for( "interview", interviews = interviews ))
    with open ("interviews.json", 'r') as f:
       interviews2 = json.loads(f.read()) 
       print (interviews2)
       interviews3 = [ ]
       for i in interviews2 :
            interviews3.append(interviews2[i])

        
    return render_template('candidates.html',interviews=interviews3)
    

@app.route('/login')
def index():
    return render_template('login.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/about')
def about():
    return render_template('about.html')





if __name__== "__main__":
    app.run()
