from flask_restful import Resource
from flask import request
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
)
from models.hospital import HospitalModel
from schemas.hospital import HospitalSchema
import traceback

hospital_schema = HospitalSchema()

class HospitalRegister(Resource):
    @classmethod
    def post(cls):
        hospital = HospitalSchema.load(request.get_json())
        if HospitalModel.find_hospital_by_name(hospital.hospital_name):
            return {"message": "A user with that username already exists."}, 400
        try:
            hospital.save_to_db()
        except:
            traceback.print_exc()
            return {"message": "Failed to create Hospital"}, 500
        return {"message": "Hospital onboarded successfully"}, 201