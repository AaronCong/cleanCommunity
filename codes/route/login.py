from flask import render_template, request, flash, Blueprint, redirect, url_for, jsonify
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from codes.persist.models.User import User
from codes.persist.database import db
from datetime import datetime

loginManager = LoginManager()
loginManager.login_view = "login.login"
loginManager.login_message = "需要先登陆哟"
login_bp = Blueprint("login", __name__)


@loginManager.user_loader
def load_user(username):
    return User.query.filter(User.uname == username).first()


@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        type = request.form.get('type')
        user = load_user(username)
        # 验证表单中提交的用户名和密码
        if user is not None and request.form['password'] == user.password:
            # 通过Flask-Login的login_user方法登录用户
            success = login_user(user, True)
            next = request.args.get('next')

            return jsonify("success")
            # return jsonify(loggedIn=True, redirectUrl=next or url_for('index.home'))
            # return redirect(next or url_for('index.home'))
                # return redirect(url_for('search.searchDumper'))
                # return redirect(url_for('search.history'))
        else:
            return jsonify('fail')
            # flash('用户名或密码错误！')
    # GET 请求
    return render_template('index.html')


@login_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash('您已登出')
    return redirect('/login')
