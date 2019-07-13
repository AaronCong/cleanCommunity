from flask import render_template, request, flash, Blueprint, redirect, url_for, jsonify
from flask_login import login_required, current_user
from codes.persist.models.Dialog import Dialog
from codes.persist.models.User import User
from codes.persist.DAO import userDAO

search_bp = Blueprint('search',__name__)


@search_bp.route('/searchDumper', methods=['GET','POST'])
@login_required
def searchDumper():
    #current_user = User('a','a','1','123',36.3151251475,117.2021484375)
    nearest = userDAO.searchDumper(current_user)
    return jsonify(nearest)



@search_bp.route('/listHistory',methods=['GET','POST'])
@login_required
def listHistory():
    if current_user.status == 2:
        relatedUids = [dialog.uid1 for dialog in Dialog.query.filter(Dialog.uid2 == current_user.id).distinct().all()]
        relatedUnames = [user.uname for user in User.query.filter(User.id.in_(relatedUids)).distinct().all()]
        return jsonify(relatedUnames)
    #return render_template('index.html')
    return 'index'