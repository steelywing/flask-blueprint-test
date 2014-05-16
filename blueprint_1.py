from flask import Blueprint, render_template

blueprint = Blueprint('blueprint_1', __name__,
                      template_folder='blueprint_1')


@blueprint.route('/')
def show():
    return render_template('bp.html')
