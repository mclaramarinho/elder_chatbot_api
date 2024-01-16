from firebase.setup import db
from database_actions.users import data_structure
from database_actions.find_user import find_caregiver_uid

def create_elder(cpf, first_name, last_name, birthday, phone_number, main_ec_name, main_ec_phone, sec_ec_phone, sec_ec_name, caregiver_uid, uid):


    data = data_structure("elder", cpf, first_name, last_name, birthday, phone_number,
                          uid=uid, main_ec_name=main_ec_name, main_ec_phone=main_ec_phone,
                          sec_ec_phone=sec_ec_phone, sec_ec_name=sec_ec_name,
                          caregiver_uid=caregiver_uid)



    db.reference(f"users/caregivers/{caregiver_uid}/elders_associated").update({
        uid: True
    })

    try:
        db.reference(f"users/elders/{uid}").set(data)
        return {"message": "Success!"}
    except Exception as e:
        return {"message": e.__str__()}
