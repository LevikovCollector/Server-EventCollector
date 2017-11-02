from flask import Flask, request, render_template
from db_conf import db_session, AllInfoData
from datetime import datetime
from db_work import get_all_data
import json


app = Flask(__name__)


@app.route('/')
def index():
    data = get_all_data()
    all_data = []
    for row_data in data:
        all_data.append({'app_name':row_data.app_name,
                        'active_tab_url':row_data.active_tab_url,
                        'timestamp':row_data.timestamp,
                        'pycharm_project':row_data.pycharm_project,
                        'sublime_path': row_data.sublime_path,
                        'user_ip': row_data.user_ip
                        })

    return render_template('index.html', all_data = all_data)


@app.route('/tableWithFilter', methods=['POST'])
def table_with_filter():
    data = get_all_data()
    all_data = []
    for row_data in data:
        all_data.append({'app_name': row_data.app_name,
                         'active_tab_url': row_data.active_tab_url,
                         'timestamp': row_data.timestamp,
                         'pycharm_project': row_data.pycharm_project,
                         'sublime_path': row_data.sublime_path,
                         'user_ip': row_data.user_ip
                         })

    return render_template('tableWithFilter.html', all_data = all_data, ch_chr=request.form.get('show_chrome_info'),ch_py = request.form.get('show_pycharm_info'),\
                           ch_sub = request.form.get('show_sublime_info'))


@app.route('/api/v1/save_info_data', methods=['GET', 'POST'])
def save_info_data():
    j_data = json.loads(request.json)
    id_list = []
    for row in j_data:
        data = datetime.strptime(row['timestamp'], '%Y-%m-%dT%H:%M:%S')
        info = AllInfoData(app_name = row['app_name'],
                           active_tab_url = row['active_tab_url'],
                           timestamp = data,
                           pycharm_project = row['pycharm_project'],
                           sublime_path = row['sublime_path'],
                           user_ip = row['user_ip'])
        id_list.append(row['row_id'])
        db_session.add(info)
    db_session.commit()
    return json.dumps({'update_id':id_list})


@app.errorhandler(405)
def error_method(error):
    return 'Не верный метод!'


if __name__ == "__main__":
    app.run()