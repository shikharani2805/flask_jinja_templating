from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def template_test():
    dic = ["SHIKHA CHAUHAN", "28/05/1997"]
    edu = ["Polytechnic (CSE)", "B.tech (CSE)"]
    exp = ["3 months"]
    email = ["shikhachauhan2805@gmail.com"]
    Llink = "LinkedIn"
    Glink = "Github"
    return render_template('index.html', dic= dic, edu=edu, exp=exp,email=email, Llink=Llink, Glink=Glink)

@app.route("/home")
def home_page():
    # dic = {"name": "Shikha", "dob":"28/05/1997"}
    name = "SHIKHA CHAUHAN"
    dob = "28/05/1997"
    return render_template('home.html', name= name, dob=dob)


@app.route("/about")
def about_page():
    dob = "28/05/1997"
    edu = ["Polytechnic (CSE)", "B.tech (CSE)"]
    exp = "3 months"
    return render_template('about.html',dob=dob, edu=edu, exp=exp)


@app.route("/contact")
def contact_page():
    email = ["shikhachauhan2805@gmail.com"]
    Llink = "LinkedIn"
    Glink = "Github"
    return render_template('contact.html',email=email, Llink=Llink, Glink=Glink)

if __name__ == '__main__':
    app.run(debug=True)