from firebase.setup import db

def find_user_phone(phone_number):
    returnData = {
        "exists": False,
        "user_type": "",
        "user_data": {}
    }
    main_ref = db.reference('users').get()
    if "caregivers" in main_ref:
        all_caregivers = db.reference('users/caregivers').get()
        for cpf in all_caregivers:
            caregiver_data = db.reference(f'users/caregivers/{cpf}').get()
            if caregiver_data["phone_number"] == phone_number:
                returnData["exists"] = True
                returnData["user_type"] = "caregiver"
                returnData["user_data"] = caregiver_data
    if "elders" in main_ref:
        all_elders = db.reference('users/elders').get()
        for cpf in all_elders:
            elder_data = db.reference(f'users/elders/{cpf}').get()
            if elder_data["phone_number"] == phone_number:
                returnData["exists"] = True
                returnData["user_type"] = "elder"
                returnData["user_data"] = elder_data

    return returnData


def find_caregiver_cpf(cpf):
    returnData = {
        "exists": False,
        "user_type": "",
        "user_data": {}
    }
    all_caregivers = db.reference(f'users/caregivers').get()

    if cpf in all_caregivers:
        for key in all_caregivers:
            if key == cpf:
                caregiver_data = db.reference(f'users/caregivers/{cpf}').get()
                returnData["exists"] = True
                returnData["user_type"] = "caregiver"
                returnData["user_data"] = caregiver_data

    return returnData


def find_elder_cpf(cpf):
    returnData = {
        "exists": False,
        "user_type": "",
        "user_data": {}
    }
    all_elders = db.reference(f'users/elders').get()

    if cpf in all_elders:
        for key in all_elders:
            if key == cpf:
                elder_data = db.reference(f'users/elders/{cpf}').get()
                returnData["exists"] = True
                returnData["user_type"] = "elder"
                returnData["user_data"] = elder_data

    return returnData