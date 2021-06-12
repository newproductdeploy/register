from flask import Flask,render_template,request,redirect
from flask_mail import Mail
from flask_mail import Message
from random import randint

app = Flask(__name__)

mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sagarparigi12@gmail.com'
app.config['MAIL_PASSWORD'] = 'sagarjaya1729sagarjaya'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('https://shopnestregister.vercel.app',methods = ['POST','GET'])
def input():
	return render_template("register.html")
@app.route('https://shopnestregister.vercel.app/register',methods = ['POST','GET'])
def register():
	email=request.form.get('data3')
	output = randint(100000, 999999);
	msg = Message("Thanks you for registering..!!", sender='sagarparigi12@gmail.com' , recipients = [email])
	msg.body = f"Welcome to ShopNest.  Your registration id : {output}"
	mail.send(msg)
	return "mail sent"
	
app.run(debug=True)
