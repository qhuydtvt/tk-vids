import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds159344.mlab.com:59344/tk-services

host = "ds159344.mlab.com"
port = 59344
db_name = "tk-services"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
