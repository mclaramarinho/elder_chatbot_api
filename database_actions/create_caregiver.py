from firebase.setup import db
from models.users import Caregiver

def create_caregiver(cpf, first_name, last_name, birthday, phone_number, pin, uid):
    data = Caregiver(cpf=cpf, first_name=first_name, last_name=last_name, birthday=birthday, phone_number=phone_number, pin=pin, uid=uid)
    try:
        db.reference(f"users/caregivers/{uid}").set(data.return_user_data())
        return {"message": "Success!"}
    except Exception as e:
        return {"message": e.__str__()}