from firebase.setup import db
from database_actions.users import data_structure

def create_caregiver(cpf, first_name, last_name, birthday, phone_number, pin):
    data = data_structure("cg", cpf, first_name, last_name, birthday, phone_number, pin=pin)

    try:
        db.reference(f"users/caregivers/{cpf}").set(data)
        return {"message": "Success!"}
    except Exception as e:
        return {"message": e.__str__()}