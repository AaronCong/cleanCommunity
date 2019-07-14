from codes.createDataBase import db
from flask import render_template, request, flash, Blueprint, redirect, url_for, jsonify
from flask import request
import traceback
import pymysql
from codes.persist.models.User import User
register_bp = Blueprint('register',__name__)

@register_bp.route('/register',methods=['GET','POST'])
def register():
    if request.method =='POST':
        username = request.form.get('username')
        password = request.form.get('password')
        longitude = request.form.get('aptlon')
        latitude = request.form.get('aptlat')
        phone = request.form.get('phone')
        # print(username)
        # print(password)
        # print(longitude)
        # print(latitude)
        # print(phone)
        try:
            user = User(uname=username,status=0,phone=phone,apt_lat=latitude,apt_lon=longitude,password=password)
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            print(e)
            return jsonify('failed')
        #return redirect(url_for('login.html'))
        return jsonify("success")
    #return render_template('register.html')
    return None
