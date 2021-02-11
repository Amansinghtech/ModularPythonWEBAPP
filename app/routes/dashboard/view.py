from flask import Blueprint, render_template

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard', methods=['GET', 'POST'])
def index():
    return render_template('dashboard.html')

@dashboard.route('/dashboard/admin', methods=['GET', 'POST'])
def admin():
    return "WE are in Admin PAge"