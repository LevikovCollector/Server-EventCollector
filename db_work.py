from db_conf import db_session, AllInfoData

def get_all_data():
    all_data = AllInfoData()
    return all_data.query.all()

