from firebase.setup import db

def find_user_uid(uid):
    returnData = {
        "exists": False,
        "user_type": "",
        "user_data": {}
    }
    main_ref = db.reference('users').get()
    if "caregivers" in main_ref:
        all_caregivers = db.reference('users/caregivers').get()
        for item in all_caregivers:
            caregiver_data = db.reference(f'users/caregivers/{item}').get()
            if caregiver_data["uid"] == uid:
                returnData["exists"] = True
                returnData["user_type"] = "caregiver"
                returnData["user_data"] = caregiver_data

    if "elders" in main_ref:
        all_elders = db.reference('users/elders').get()
        for item in all_elders:
            elder_data = db.reference(f'users/elders/{item}').get()
            if elder_data["uid"] == uid:
                returnData["exists"] = True
                returnData["user_type"] = "elder"
                returnData["user_data"] = elder_data

    return returnData


def find_caregiver_uid(uid):
    returnData = {
        "exists": False,
        "user_type": "",
        "user_data": {}
    }
    all_caregivers = db.reference(f'users/caregivers').get()

    if uid in all_caregivers:
        for key in all_caregivers:
            if key == uid:
                caregiver_data = db.reference(f'users/caregivers/{uid}').get()
                returnData["exists"] = True
                returnData["user_type"] = "caregiver"
                returnData["user_data"] = caregiver_data

    return returnData


def find_elder_uid(uid):
    returnData = {
        "exists": False,
        "user_type": "",
        "user_data": {}
    }
    all_elders = db.reference(f'users/elders').get()

    if uid in all_elders:
        for key in all_elders:
            if key == uid:
                elder_data = db.reference(f'users/elders/{uid}').get()
                returnData["exists"] = True
                returnData["user_type"] = "elder"
                returnData["user_data"] = elder_data

    return returnData