from flask import Flask,render_template,request,session,redirect
from flask_sqlalchemy import SQLAlchemy
import json,os
from werkzeug.utils import secure_filename


with open('C://Users//SS Computer//PycharmProjects//Myportfolio//config.json','r') as c:
    params = json.load(c)["params"]

app = Flask(__name__)
local_host=True
if (local_host):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_server']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['production_server']

db = SQLAlchemy(app)
app.secret_key="super-secret-key"
UPLOAD_FOLDER = params['upload_location']
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#`sno``title``content``image`SELECT * FROM `myservice` WHERE 1
class Myservice(db.Model):
    sno= db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.String(120))
    image = db.Column(db.String(120))


    def __repr__(self):
        return '<User %r>' % self.username


class Client_review(db.Model):
    sno= db.Column(db.Integer, primary_key=True)
    c_name= db.Column(db.String(80))
    c_content = db.Column(db.String(300))
    c_title = db.Column(db.String(120))
    c_image=db.Column(db.String(120))

    def __repr__(self):
        return '<User %r>' % self.username


class Worked(db.Model):
    sno= db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(80))
    content = db.Column(db.String(100))
    css_class = db.Column(db.String(100))
    image=db.Column(db.String(120))

    def __repr__(self):
        return '<User %r>' % self.username


class Skills(db.Model):
    sno= db.Column(db.Integer, primary_key=True)
    s_name= db.Column(db.String(80))
    s_expertise = db.Column(db.String(300))



    def __repr__(self):
        return '<User %r>' % self.username

#Education sno``in_name``in_des``in_city``in_date_s``in_date_l


class Education(db.Model):
    sno= db.Column(db.Integer, primary_key=True)
    in_name= db.Column(db.String(80))
    in_des = db.Column(db.String(100))
    in_city = db.Column(db.String(100))
    in_date_s=db.Column(db.String(120))
    in_date_l = db.Column(db.String(120))

    def __repr__(self):
        return '<User %r>' % self.username


#Experince `sno``e_name``e_role``e_title``date`

class Experince(db.Model):
    sno= db.Column(db.Integer, primary_key=True)
    e_name= db.Column(db.String(80))
    e_role = db.Column(db.String(100))
    e_title = db.Column(db.String(100))
    s_date=db.Column(db.String(120))
    l_date = db.Column(db.String(120))


    def __repr__(self):
        return '<User %r>' % self.username


#MYSERVCIES AT DIFFERENT WEBSITRS
class Fiverlinks(db.Model):
    sno= db.Column(db.Integer, primary_key=True)
    heading= db.Column(db.String(300))
    points = db.Column(db.String(100))
    links = db.Column(db.String(100))



    def __repr__(self):
        return '<User %r>' % self.username

class Contact(db.Model):
    sno= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(80))
    email = db.Column(db.String(100))
    phone_num = db.Column(db.String(100))
    msg=db.Column(db.String(300))



    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/',methods=['POST','GET'])
def index():
    myservice=Myservice.query.filter_by().all()
    clientr=Client_review.query.filter_by().all()
    skills = Skills.query.filter_by().all()
    worked=Worked.query.filter_by().all()
    educations = Education.query.filter_by().all()
    experinces = Experince.query.filter_by().all()
    fiverlinks=Fiverlinks.query.filter_by().all()
    if request.method=='POST':
        name=request.form.get('name')
        email = request.form.get('email')
        msg = request.form.get('msg')
        phone_num = request.form.get('phone_num')
        contact=Contact(name=name,email=email,msg=msg,phone_num=phone_num)
        db.session.add(contact)
        db.session.commit()


    return render_template('index.html',params=params,myservice=myservice,clientrw=clientr,skills=skills,worked=worked,educations=educations,experinces=experinces,fiverlinks=fiverlinks)

@app.route('/dashboard',methods=['GET','POST'])
def dashboard():
     if 'user' in session and session['user'] == params['admin_user']:
         worked = Worked.query.filter_by().all()
         myservice = Myservice.query.filter_by().all()
         clientr = Client_review.query.filter_by().all()
         skills = Skills.query.filter_by().all()
         worked = Worked.query.filter_by().all()
         educations = Education.query.filter_by().all()
         experinces = Experince.query.filter_by().all()
         contacts = Contact.query.filter_by().all()
         fiverlinks = Fiverlinks.query.filter_by().all()
         return render_template('dashboard.html', params=params,myservice=myservice,clientrw=clientr,skills=skills,worked=worked,educations=educations,contacts=contacts,experinces=experinces,fiverlinks=fiverlinks)

     if request.method == 'POST':
         # redirect to admin panel
         username = request.form.get('uname')
         userpass = request.form.get('pass')
         if (params['admin_user'] == username and params['admin_password'] == userpass):
             # set the session varibble
             session['user'] = username
             worked = Worked.query.filter_by().all()
             myservice = Myservice.query.filter_by().all()
             clientr = Client_review.query.filter_by().all()
             skills = Skills.query.filter_by().all()
             worked = Worked.query.filter_by().all()
             educations = Education.query.filter_by().all()
             experinces = Experince.query.filter_by().all()
             contacts = Contact.query.filter_by().all()
             return render_template('dashboard.html', params=params,myservice=myservice,clientrw=clientr,skills=skills,worked=worked,educations=educations,experinces=experinces)

     return render_template('login.html', params=params)



"""---------------------------------------Delete Start from here------------------------------------------------------"""
@app.route('/deleteserv/<string:sno>',methods=['POST','GET'])
def deleteserv(sno):
    if 'user' in session and session['user']==params['admin_user']:
        myservice=Myservice.query.filter_by(sno=sno).first()
        db.session.delete(myservice)
        db.session.commit()
        return redirect('/dashboard')

#myportfilio delete
@app.route('/deletept/<string:sno>',methods=['POST','GET'])
def deletesport(sno):
    if 'user' in session and session['user']==params['admin_user']:
        myservice=Worked.query.filter_by(sno=sno).first()
        db.session.delete(myservice)
        db.session.commit()
        return redirect('/dashboard')

# myportfilio delete
@app.route('/deletefl/<string:sno>', methods=['POST', 'GET'])
def deletefl(sno):
    if 'user' in session and session['user'] == params['admin_user']:
         myservice = Fiverlinks.filter_by(sno=sno).first()
         db.session.delete(myservice)
         db.session.commit()
         return redirect('/dashboard')


#myskill delete
@app.route('/deletems/<string:sno>',methods=['POST','GET'])
def deletems(sno):
    if 'user' in session and session['user']==params['admin_user']:
        myservice=Skills.query.filter_by(sno=sno).first()
        db.session.delete(myservice)
        db.session.commit()
        return redirect('/dashboard')

#Clientee
@app.route('/deletetestimental/<string:sno>',methods=['POST','GET'])
def deletetestim(sno):
    if 'user' in session and session['user']==params['admin_user']:
        myservice=Client_review.query.filter_by(sno=sno).first()
        db.session.delete(myservice)
        db.session.commit()
        return redirect('/dashboard')
#TEducational
@app.route('/deleteed/<string:sno>',methods=['POST','GET'])
def deleteed(sno):
    if 'user' in session and session['user']==params['admin_user']:
        myservice=Education.query.filter_by(sno=sno).first()
        db.session.delete(myservice)
        db.session.commit()
        return redirect('/dashboard')


#Work Experince
@app.route('/deletewe/<string:sno>',methods=['POST','GET'])
def deletewe(sno):
    if 'user' in session and session['user']==params['admin_user']:
        myservice=Experince.query.filter_by(sno=sno).first()
        db.session.delete(myservice)
        db.session.commit()
        return redirect('/dashboard')


"""---------------------------------------Delete End here------------------------------------------------------"""


"""---------------------------------------Edit Start from here------------------------------------------------------"""
#Edit client review
@app.route("/edit_client_review/<string:sno>",methods=['GET','POST'])
def edit(sno):
    if 'user' in session and session['user'] == params['admin_user']:
        if request.method=='POST':
            c_name = request.form.get('c_name')
            c_content = request.form.get('c_content')
            c_title = request.form.get('c_title')
            c_image = request.form.get('c_image')
            file = request.files['inputFile']
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


            if sno=='0':
                client_review = Client_review(c_name=c_name, c_content=c_content, c_title=c_title, c_image=file.filename)
                db.session.add(client_review)
                db.session.commit()
                return redirect('/dashboard')


            else:

                client_review = Client_review.query.filter_by(sno=sno).first()
                client_review.c_name = c_name
                client_review.c_content = c_content
                client_review.c_title = c_title
                client_review.c_image = file.filename
                db.session.commit()
                return redirect('/edit_client_review/' + sno)
    client_review = Client_review.query.filter_by(sno=sno).first()
    return render_template('edit_clinet_re.html', params=params, client_review=client_review, sno=sno)

#Edit Education
@app.route("/edit_ex/<string:sno>",methods=['GET','POST'])
def edit_Education(sno):
    if 'user' in session and session['user'] == params['admin_user']:
        if request.method=='POST':
            in_name = request.form.get('in_name')
            in_des= request.form.get('in_des')
            in_city = request.form.get('in_city')
            in_date_s = request.form.get('in_date_s')
            in_date_l = request.form.get('in_date_l')


            if sno=='0':
                experince = Education(in_name=in_name,in_des=in_des,in_city=in_city,in_date_s=in_date_s,in_date_l=in_date_l)
                db.session.add(experince)
                db.session.commit()
                return redirect('/dashboard')


            else:

                experince = Education.query.filter_by(sno=sno).first()
                experince.in_name = in_name
                experince.in_des =in_des
                experince.in_city = in_city
                experince.in_date_s = in_date_s
                experince.in_date_l=in_date_l
                db.session.commit()
                return redirect('/edit_ex/' + sno)
            #client_revww chnage nh krrhe qqk km  bhht barh jayega :-D
    client_review = Education.query.filter_by(sno=sno).first()
    return render_template('edit_education.html', params=params, client_review=client_review, sno=sno)




#Edit Fiverlinks
@app.route("/edit_fl/<string:sno>",methods=['GET','POST'])
def edit_fiver(sno):
    if 'user' in session and session['user'] == params['admin_user']:
        if request.method=='POST':
            heading = request.form.get('heading')
            points = request.form.get('points')
            links = request.form.get('links')



            if sno=='0':
                client_review = Fiverlinks(heading=heading,points=points,links=links)
                db.session.add(client_review)
                db.session.commit()
                return redirect('/dashboard')


            else:

                client_review = Fiverlinks.query.filter_by(sno=sno).first()
                client_review.heading = heading
                client_review.points= points
                client_review.links = links
                db.session.commit()
                return redirect('/edit_fl/' + sno)
    client_review = Fiverlinks.query.filter_by(sno=sno).first()
    return render_template('edit_fiverlinks.html', params=params, client_review=client_review, sno=sno)



#Edit Skills
@app.route("/edit_skills/<string:sno>",methods=['GET','POST'])
def edit_skills(sno):
    if 'user' in session and session['user'] == params['admin_user']:
        if request.method=='POST':
            s_name = request.form.get('s_name')
            s_expertise = request.form.get('s_expertise')



            if sno=='0':
                client_review = Skills(s_name=s_name,s_expertise=s_expertise)
                db.session.add(client_review)
                db.session.commit()
                return redirect('/dashboard')


            else:

                client_review = Skills.query.filter_by(sno=sno).first()
                client_review.s_name = s_name
                client_review.s_expertise = s_expertise
                db.session.commit()
                return redirect('/edit_skills/' + sno)
    client_review = Skills.query.filter_by(sno=sno).first()
    return render_template('edit_skills.html', params=params, client_review=client_review, sno=sno)

#`sno``e_name``e_role``e_title``date`
#Edit Experince
@app.route("/edit_ed/<string:sno>",methods=['GET','POST'])
def edit_exper(sno):
    if 'user' in session and session['user'] == params['admin_user']:
        if request.method=='POST':
            e_name = request.form.get('e_name')
            e_role = request.form.get('e_role')
            e_title = request.form.get('e_title')
            s_date = request.form.get('s_date')
            l_date=request.form.get('l_date')




            if sno=='0':
                client_review = Experince(e_name=e_name, e_role=e_role, e_title=e_title,s_date=s_date,l_date=l_date)
                db.session.add(client_review)
                db.session.commit()
                return redirect('/dashboard')


            else:

                client_review = Experince.query.filter_by(sno=sno).first()
                client_review.e_name = e_name
                client_review. e_rolet =  e_role
                client_review.e_title = e_title
                client_review.s_date=s_date
                client_review.l_date =l_date
                db.session.commit()
                return redirect('/edit_ed/' + sno)
    client_review = Experince.query.filter_by(sno=sno).first()
    return render_template('edit_experience.html', params=params, client_review=client_review, sno=sno)


#Edit myservice
@app.route("/edit_service/<string:sno>",methods=['GET','POST'])
def edit_service(sno):
    if 'user' in session and session['user'] == params['admin_user']:
        if request.method=='POST':
            title = request.form.get('title')
            content = request.form.get('content')
            file = request.files['inputFile']
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))


            if sno=='0':
                client_review = Myservice(content=content,title=title, image=file.filename)
                db.session.add(client_review)
                db.session.commit()
                return redirect('/dashboard')


            else:

                client_review = Myservice.query.filter_by(sno=sno).first()
                client_review.content = content
                client_review.title = title
                client_review.image = file.filename
                db.session.commit()
                return redirect('/edit_service/' + sno)
    client_review = Myservice.query.filter_by(sno=sno).first()
    return render_template('edit_my_service.html', params=params, client_review=client_review, sno=sno)


#Edit work /portfolio
@app.route("/edit_wk/<string:sno>",methods=['GET','POST'])
def edit_work_portfolio(sno):
    if 'user' in session and session['user'] == params['admin_user']:
        if request.method=='POST':
            css_class = request.form.get('css_class')
            content = request.form.get('content')
            title = request.form.get('title')
            file = request.files['inputFile']
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


            if sno=='0':
                client_review = Worked(css_class=css_class, content=content, title=title,image=file.filename)

                db.session.add(client_review)
                db.session.commit()
                return redirect('/dashboard')


            else:

                client_review = Worked.query.filter_by(sno=sno).first()
                client_review.css_class = css_class
                client_review.content = content
                client_review.title = title
                client_review.image = file.filename
                db.session.commit()
                return redirect('/edit_wk/' + sno)
    client_review = Worked.query.filter_by(sno=sno).first()
    return render_template('edit_worked.html', params=params, client_review=client_review, sno=sno)




"""---------------------------------------Edit End here------------------------------------------------------"""
@app.route('/logout',methods=['POST','GET'])
def logout():
    session.pop('user')
    return redirect('/dashboard')


app.run(debug=True)


