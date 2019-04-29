from flask import render_template,request,redirect,url_for,abort
from ..models import User,Blog,Comment
from . import main
from ..request import *
from flask_login import login_required, current_user
from . forms import CommentForm,BlogForm
from ..email import mail_message
from .. import db
import requests
import json




@main.route('/')
def index():
    index=Blog.query.all()
    random=requests.get('http://quotes.stormconsultancy.co.uk/random.json').json()
    return render_template('index.html',index=index, random=random)

@main.route('/blog', methods = ['GET','POST'])
@login_required
def new_blog():
	form = BlogForm()
	if form.validate_on_submit():
		blog = Blog (body=form.body.data,category=form.category.data)
		blog.save_blog()
		return redirect(url_for('main.index'))
	return render_template('blog.html',form=form)   


@main.route('/comments', methods = ['GET','POST'])
@login_required
def new_comment():
	form = CommentForm()
	if form.validate_on_submit():
		comment = Comment (title=form.comment.data)
		comment.save_comments()
		return redirect(url_for('main.index'))
	return render_template('comments.html',form=form)

# We first import the abort function, that stops a request, and returns a response according to the status code passed in. We then create a dynamic route that is handled by the profile view function.
# We then query the database to find the user according to the username passed. If no user is found the abort is called and a 404 status code is returned as a response. If a user is found we render a template and pass in the user as a variable.
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    index=Pitch.query.all()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)   



# We create a update_blog view function that takes in a username, and instantiates the UpdateBlog form class.
# We query the database to find a user with the same username.
# If the form is validated we update the content of the user.bio property to fill in what the user has submitted and redirect the user back to the pitches page where he can see the new bio.
# If not we render the _update.html_ template and pass in the form instance.
@main.route('/user.<uname>/blog',methods= ['GET','POST'])
@login_required
def update_blog(uname):
	user = User.query.filter_by(username = uname).first
	if user is none:
		abort(404)


	form = blog()


	if form.validate_on_submit():
		user.bio = form.bio.data

		db.session.add(user)
		db.session.commit()

		return redirect(url_for('.profile',uname=user.username))

	return render_template('profile/blog.html',form =form)



@main.route('/user.<uname>/comments',methods= ['GET','POST'])
@login_required
def update_comments(uname):
	user = User.query.filter_by(username = uname).first
	if user is none:
		abort(404)


	form = comments()


	if form.validate_on_submit():
		user.bio = form.bio.data

		db.session.add(user)
		db.session.commit()

		return redirect(url_for('.profile',uname=user.username))

	return render_template('profile/comments.html',form =form)    

