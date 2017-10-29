from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///all_info.sqlite')

db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


class AllInfoData(Base):
    __tablename__ = 'all_info'
    id = Column(Integer, primary_key = True)
    user_ip = Column(String(50))
    app_name = Column(String(50))
    active_tab_url = Column(String(200))
    timestamp = Column(DateTime)
    pycharm_project = Column(String(100))
    sublime_path = Column(String(200))

    def __init__(self, app_name = None, active_tab_url = None, timestamp = None, pycharm_project = None, sublime_path = None, user_ip = None):
        self.app_name = app_name
        self.active_tab_url = active_tab_url
        self.timestamp = timestamp
        self.pycharm_project = pycharm_project
        self.sublime_path = sublime_path
        self.user_ip = user_ip

    def __repr__(self):
        return '<info {} {} {} {} {} {}>'.format(self.app_name, self.active_tab_url, self.timestamp, self.pycharm_project, self.sublime_path, self.user_ip)

if __name__ == "__main__":
    #Создает базу данных
    Base.metadata.create_all(bind=engine)