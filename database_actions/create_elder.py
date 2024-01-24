from firebase.setup import db
from models.users import Elder


def create_elder(cpf, first_name, last_name, birthday, phone_number, main_ec_name, main_ec_phone, sec_ec_phone, sec_ec_name, caregiver_uid, uid):

    data = Elder(cpf=cpf, first_name=first_name, last_name=last_name, birthday=birthday,
                 phone_number=phone_number, uid=uid, main_ec_name=main_ec_name,
                 main_ec_phone=main_ec_phone, sec_ec_phone=sec_ec_phone, sec_ec_name=sec_ec_name,
                 caregiver_uid=caregiver_uid)

    db.reference(f"users/caregivers/{caregiver_uid}/elders_associated").update({
        uid: True
    })

    try:
        db.reference(f"users/elders/{uid}").set(data.return_user_data())
        return {"message": "Success!"}
    except Exception as e:
        return {"message": e.__str__()}
