
from flask import jsonify
from flask_restful import reqparse, abort, Api, Resource
import elasticsearch, enchant
from database import db
from bson.json_util import dumps
import unicodedata
import json
from bson.objectid import ObjectId


parser = reqparse.RequestParser()
parser.add_argument('jsondata', type=str)
parser.add_argument('entity_name', type=str)



class PostClass(Resource):
    def post(self):
        args = parser.parse_args()

        jsonData = args['jsondata']
        jsonData = jsonData.replace("u\"","\"").replace("u\'","\'").replace("\'","\"")

        jsonData = str(jsonData)
        print jsonData
        data = json.loads(jsonData)

        auditEntry={
		"entity":data["entity"],
		"entityid":data["entityid"],
		"old_value":data["old_value"],
		"new_value":data["new_value"],
		"change_owner":data["change_owner"],
		"timestamp":data["timestamp"]
		}

        getId = db.audits.insert_one(auditEntry).inserted_id



        return json.dumps([])



class Search(Resource):
	def get(self):
		args = parser.parse_args()
		entity_name = args['entity_name']
		auditResult = db.audits.find({'entity':entity_name})

		allResultList=[]

		for oneResult in auditResult:
			auditEntry={ "entity":oneResult.get("entity"), "entityid":oneResult.get("entityid"), "old_value":oneResult.get("old_value"), "ew_value":oneResult.get("new_value"), "change_owner":oneResult.get("change_owner"), "timestamp":oneResult.get("timestamp") }
			allResultList.append(auditEntry)

		print allResultList

		return json.dumps(allResultList)
