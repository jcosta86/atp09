from flask import render_template, Blueprint

from backend.controllers.log_controller import read_log

log = Blueprint(__name__, 'log')


@log.route('/logfile')
def list_historico():
    list_logfile = read_log()
    return render_template('logfile.html', lista=list_logfile)
