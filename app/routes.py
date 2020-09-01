from app import app, db, bcrypt
from flask import render_template, url_for, request, flash, redirect
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import LoginForm, SignUpForm, DeveloperForm
from app.models import User, Developers


@app.route('/')
@app.route('/index', methods=['GET','POST'])
@login_required
def index():
    if request.method == 'GET':
        developer = Developers.query.all()
        return render_template('index.html', title='Homepage', developer=developer)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignUpForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('The User is Successfully added')
        return redirect(url_for('login'))
    return render_template('signup.html', title='SignUp', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, form.remember.data)
            return redirect(url_for('index'))
        else:
            flash('Please check your Email and Password')
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/about')
@login_required
def about():
    return render_template('about.html', title='About')


@app.route('/index/<int:developer_id>/edit', methods=['GET','POST'])
@login_required
def edit(developer_id):
    developer = Developers.query.get_or_404(developer_id)
    form = DeveloperForm()
    if form.validate_on_submit():
        developer.first_name = form.first_name.data
        developer.last_name = form.last_name.data
        developer.email = form.email.data
        developer.address = form.address.data
        developer.langueges = form.langueges.data
        developer.level = form.level.data
        developer.info = form.info.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.first_name.data = developer.first_name
        form.last_name.data = developer.last_name
        form.email.data = developer.email
        form.address.data = developer.address
        form.langueges.data = developer.langueges
        form.level.data = developer.level
        form.info.data = developer.info
    return render_template('edit.html', title='Edit', form=form)


@app.route('/delete')
@login_required
def delete():
    
    return render_template('delete.html', title='Delete')


@app.route('/create', methods=['GET','POST'])
@login_required
def create():
    form = DeveloperForm()
    if form.validate_on_submit():
        developer = Developers(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, address=form.address.data, langueges=form.langueges.data, level=form.level.data, info=form.info.data)
        db.session.add(developer)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html', form=form, title='Create')


@app.route('/index/<int:developer_id>', methods=['GET','POST'])
@login_required
def detail(developer_id):
    developer = Developers.query.get_or_404(developer_id)
    return render_template('detail.html', title='Detail', developer=developer)
