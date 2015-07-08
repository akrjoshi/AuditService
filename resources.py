
from flask import jsonify
from flask_restful import reqparse, abort, Api, Resource
import elasticsearch, enchant
from database import db
from bson.json_util import dumps
import unicodedata
import json
from bson.objectid import ObjectId
from models import *
from flask import Response

parser = reqparse.RequestParser()
parser.add_argument('jsondata', type=str)
parser.add_argument('entity_name', type=str)
parser.add_argument('entity_id', type=str)
parser.add_argument('change_owner', type=str)
parser.add_argument('from_date', type=str)
parser.add_argument('to_date', type=str)
parser.add_argument('limit', type=str)


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

        getId = db.Audits.insert_one(auditEntry).inserted_id
        return json.dumps([])



class Search(Resource):
	def get(self):
		args = parser.parse_args()
		
		entity_name = args['entity_name']
		if entity_name == None or entity_name =='':
			entity_name="."
		else:
			entity_name = "^"+entity_name+"$"
		
		entity_id = args['entity_id']
		if entity_id == None or entity_id =='':
			entity_id="."	
		else:
			entity_id = "^"+entity_id+"$"	
		
		change_owner = args['change_owner']
		if change_owner == None or change_owner =='':
			change_owner="."
		else:
			change_owner = "^"+change_owner+"$"	

		from_date = args['from_date']
		if from_date == None:
			from_date="."

		to_date = args['to_date']
		if to_date == None:
			to_date="."

		limit = args['limit']
		if limit == None and limit =='':
			limitResult=0
		else:
			print limit
			limitResult = int(limit)	

		auditResult = db.Audits.find({'entity':{'$regex':entity_name},'entityid':{'$regex':entity_id},'change_owner':{'$regex':change_owner}}).limit(limitResult)

		allResultList=[]

		for oneResult in auditResult:
			auditEntry={ "entity":oneResult.get("entity"), "entityid":oneResult.get("entityid"), "old_value":oneResult.get("old_value"), "new_value":oneResult.get("new_value"), "change_owner":oneResult.get("change_owner"), "timestamp":oneResult.get("timestamp") }
			allResultList.append(auditEntry)

		return Response(json.dumps(allResultList),  mimetype='application/json')
