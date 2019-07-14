from codes.createDataBase import db
from flask import render_template, request, flash, Blueprint, redirect, url_for
from flask import request
import traceback
import pymysql
from codes.persist.models import User
from codes.persist.models import Dialog
register_bp = Blueprint('listHistory',__name__)

@register_bp.route('/listHistory',methods=['GET','POST'])
def register():
    if request.method =='POST':
        username = request.form.get('username')
        uid = User.query.filter(User.uname==username).first().id
        relatedUids = [dialog.uid1 for dialog in Dialog.query.filter(Dialog.uid2==uid).distinct().all()]
        relatedUnames = [user.uname for user in User.query.filter(User.uid==relatedUids).distinct().all()]
        print(type(relatedUnames))
        return relatedUnames
    #return render_template('index.html')
    return 'index'