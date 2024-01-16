from firebase.setup import db
from database_actions.users import data_structure

def create_elder(cpf, first_name, last_name, birthday, phone_number, main_ec_name, main_ec_phone, sec_ec_phone, sec_ec_name, caregiver_cpf):

    data = data_structure("elder", cpf, first_name, last_name, birthday, phone_number, main_ec_name=main_ec_name, main_ec_phone=main_ec_phone, sec_ec_phone=sec_ec_phone, sec_ec_name=sec_ec_name, caregiver_cpf=caregiver_cpf)
    db.reference(f"users/caregivers/{caregiver_cpf}/elders_associated").update({
        cpf: True
    })
    try:
        db.reference(f"users/elders/{cpf}").set(data)
        return {"message": "Success!"}
    except Exception as e:
        return {"message": e.__str__()}
