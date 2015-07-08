from flask import Flask
from flask import request, render_template, flash, redirect, url_for
import os
import json
from flask import jsonify
import bson
from bson.objectid import ObjectId
import pymongo
import unicodedata
from flask.ext.restful import Api
from bson.json_util import dumps
from database import db
from database import init_db

app = Flask(__name__)
app.debug = True
api = Api(app)

from resources import PostClass, Search

baseURL = '/api'

api.add_resource(PostClass,baseURL + '/post')
api.add_resource(Search, baseURL + '/get')




'''
@app.route('/api/post', methods=['POST'])
def index():

#	if request.args.get('entity') is None:
#		return json.dumps([])

    jsondata = request.form['jsondata']
    data = json.loads(jsondata)



	#entity = request.args.get('entity').encode('utf8')
	##entityid = request.args.get('entityid').encode('utf8')
	#old_value = request.args.get('old_value').encode('utf8')
	#new_value = request.args.get('new_value').encode('utf8')
	#change_owner = request.args.get('change_owner').encode('utf8')
	#timestamp = request.args.get('timestamp').encode('utf8')

    if request.method=='POST':
			auditEntry={
			"entity":data["entity"],
			"entityid":data["entityid"],
			"old_value":data["old_value"],
			"new_value":data["new_value"],
			"change_owner":data["change_owner"],
			"timestamp":data["timestamp"]
			}
			db.audits.insert_one(auditEntry)


    return json.dumps(auditEntry)


@app.route('/search/<entity_name>',methods=['GET'])
def searchByName(entity_name):
	auditResult = db.audits.find({'entity':entity_name})

	return json.dumps(auditResult)


@app.route('/search/<change_owner>',methods=['GET'])
def search(change_owner):
	auditResult = db.audits.find({'change_owner':change_owner})

	return json.dumps(auditResult)

'''

if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'AuditPracto'
    app.run(host='0.0.0.0')
