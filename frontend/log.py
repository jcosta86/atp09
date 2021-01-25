from flask import render_template, Blueprint

from backend.controllers.log_controller import LogController

log = Blueprint(__name__, 'log')
CONTROLLER = LogController()


@log.route('/logfile')
def list_historico():
    list_logfile = CONTROLLER.read_all()
    return render_template('logfile.html', lista=list_logfile)
