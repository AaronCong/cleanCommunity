from flask import render_template, request, flash, Blueprint, redirect, url_for, jsonify
from flask_login import login_required, current_user

search_bp = Blueprint('search',__name__)
@search_bp.route('/searchDumper', method=['GET','POST'])
@login_required
def searchDumper():
    return jsonify("")


@search_bp.route('/history', method=['GET','POST'])
@login_required
def history():
    return jsonify("")