import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds119640.mlab.com:19640/muadongkhonglanh-c4e17

host = "ds119640.mlab.com"
port = 19640
db_name = "muadongkhonglanh-c4e17"
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
