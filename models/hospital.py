from db import db
from requests import Response, post


class HospitalModel(db.Model):
    __tablename__ = "hospitals"

    hospital_id = db.Column(db.Integer, primary_key=True)
    hospital_name = db.Column(db.String(80), nullable=False, unique=True)
    doctor_id = db.Column(db.Integer, unique=True, nullable=False)
    doctor_name = db.Column(db.String(80), nullable=False)

    @classmethod
    def find_hospital_by_name(cls, hospital_name) -> "HospitalModel":
        return cls.query.filter_by(hospital_name=hospital_name).first()

    @classmethod
    def find_hospital_by_id(cls, hospital_id) -> "HospitalModel":
        return cls.query.filter_by(hospital_id=hospital_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
