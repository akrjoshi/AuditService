
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
	def get(self,entity_name):
		auditResult = db.audits.find({'entity':entity_name})

		return json.dumps(auditResult)


   #		if doctor:
	#		return jsonify({'returnCode': "SUCCESS", 'data':doctor.serialize(), 'errorCode':None})
#		else:
		#	return 404