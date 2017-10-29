from flask import Flask, request
from db_conf import db_session, AllInfoData
from datetime import datetime
import json


app = Flask(__name__)


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