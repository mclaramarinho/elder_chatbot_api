from firebase.setup import db
from database_actions.users import data_structure

def create_caregiver(cpf, first_name, last_name, birthday, phone_number, pin, uid):
    data = data_structure("cg", cpf, first_name, last_name, birthday, phone_number, pin=pin, uid=uid)

    try:
        db.reference(f"users/caregivers/{uid}").set(data)
        return {"message": "Success!"}
    except Exception as e:
        return {"message": e.__str__()}