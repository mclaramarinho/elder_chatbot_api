from firebase.setup import db
from models.search_result import Search_Result_Information

def find_user_uid(uid):
    return_data = Search_Result_Information()

    main_ref = db.reference('users').get()
    if "caregivers" in main_ref:
        caregiver_data = find_caregiver_uid(uid)

        if caregiver_data["exists"]:
            print(caregiver_data)
            return caregiver_data

    if "elders" in main_ref:
        elder_data = find_elder_uid(uid)

        if elder_data["exists"]:
            print(elder_data)
            return elder_data

    return return_data.get_user_information()


def find_caregiver_uid(uid):
    return_data = Search_Result_Information()

    all_caregivers = db.reference(f'users/caregivers').get()

    if uid in all_caregivers:
        for key in all_caregivers:
            if key == uid:
                caregiver_data = db.reference(f'users/caregivers/{uid}').get()
                return_data.set_exists(True)
                return_data.set_user_type("caregiver")
                return_data.set_user_data(caregiver_data)

    return return_data.get_user_information()


def find_elder_uid(uid):
    return_data = Search_Result_Information()

    all_elders = db.reference(f'users/elders').get()

    if uid in all_elders:
        for key in all_elders:
            if key == uid:
                elder_data = db.reference(f'users/elders/{uid}').get()
                return_data.set_exists(True)
                return_data.set_user_type("elder")
                return_data.set_user_data(elder_data)

    return return_data.get_user_information()