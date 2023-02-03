from flask import render_template, Blueprint

from auth import login_required

forms_bp = Blueprint('forms_endpoints', __name__, template_folder='forms_templates')


@forms_bp.route('/add_form')
@login_required
def add_form():
    return render_template('add.html')


@forms_bp.route('/delete_form')
@login_required
def delete_form():
    return render_template('delete_type_result.html')


@forms_bp.route('/add_match_form')
@login_required
def add_match_form():
    return render_template('add_match_result.html')


@forms_bp.route('/delete_match_form')
@login_required
def delete_match_form():
    return render_template('delete_match_result.html')
