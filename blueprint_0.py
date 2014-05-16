from flask import Blueprint, render_template

blueprint = Blueprint('blueprint_0', __name__,
                      template_folder='blueprint_0')


@blueprint.route('/')
def show():
    return render_template('bp.html')
