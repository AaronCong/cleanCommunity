from flask import render_template, request, flash, Blueprint, redirect, url_for, jsonify
from flask_login import login_required, current_user
from codes.persist.models.Dialog import Dialog
from codes.persist.models.User import User
from codes.persist.DAO import userDAO

index_bp = Blueprint('index',__name__)


@index_bp.route('/index', methods=['GET','POST'])
@login_required
def home():
    if current_user.status == 2:
        return redirect('search.searchDumper')
    return redirect('search.listHistory')

