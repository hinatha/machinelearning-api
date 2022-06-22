import json

from flask import Blueprint, jsonify, request

from api import calculation, preparation

from .json_validate import validate_json, validate_schema

api = Blueprint("api", __name__, url_prefix="/v1")


@api.get("/health")
def health():
    return{"health": "ok"}


# Save name of pictures in handwriting_pics to DB and return file_id.
@api.post("/file-id")
@validate_json
@validate_schema("check_dir_name")
def file_id():
    return preparation.insert_filenames(request)


# Save picture file to local folder and filename to DB and return file_id.
@api.post("/file-upload")
def file_upload():
    return preparation.insert_filedata(request)


# Send file_id and return the result of predicting photo.
@api.post("/probabilities")
@validate_json
@validate_schema("check_file_id")
def probabilities():
    return calculation.evaluate_probs(request)


# For health check.
# Send file_id, file_name and return the same context.
@api.post("/check-schema")
# json schemaの有無のチェックをするデコレーター
@validate_json
# json schemaの定義があっているかどうかのチェックをするデコレーター
@validate_schema("check_file_schema")
def check_schema():
    data = json.loads(request.data)
    print(data["file_id"])
    print(data["file_name"])
    d = data["file_name"]
    return f"Successfully get {d}"


@api.errorhandler(400)
@api.errorhandler(404)
@api.errorhandler(500)
def error_handler(error):
    
    response = jsonify(
        {"error_message": error.description["error_message"], "result": error.code}
    )
    return response, error.code
