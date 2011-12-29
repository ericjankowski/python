#! /usr/local/bin/python3


import athletemodel
import yate
import json



print(yate.start_response("application/json"))
print(json.dumps(athletemodel.get_names_from_store()))