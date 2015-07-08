import datetime
from flask import url_for
from mongoengine import *

class Audits(Document):
    entity = StringField(max_length=255, required=True)
    entityid = StringField(max_length=255, required=True)
    old_value = StringField(required=True)
    new_value = StringField(required=True)
    change_owner = StringField(max_length=255, required=True)
    timestamp = DateTimeField(default=datetime.datetime.now, required=True)


    meta = {
        'indexes': ['-timestamp', 'entity'],
        'ordering': ['-timestamp']
    }
