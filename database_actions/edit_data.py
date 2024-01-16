'''from firebase.setup import db
from database_actions.find_user import find_elder_cpf, find_caregiver_cpf

def edit_data(user_type, user_id, caregiver_pin, data_to_edit, new_data, caregiver_id=""):

   ''' '''
    :param user_type: elder | caregiver
    :param user_id: the user which is going to have their data editted
    :param caregiver_pin: 4-digit number
    :param data_to_edit: last_name | first_name | phone_number | sec_ec_name | sec_ec_phone | main_ec_name | main_ec_phone | pin
    :param new_data: string
    :param caregiver_id: the caregiver's CPF
    :return: Dict - {"message": "Error!} | {"message": "Success!"}
    ''''''


    if user_type == "elder":
        elder_data = find_elder_cpf(user_id)
        if elder_data["caregiver"] == caregiver_id:
            auth = authorize_caregiver_action(caregiver_id, caregiver_pin)
            if auth == True:
                #todo - edit data

            else:
                # todo - do not edit data
        else:
            # todo - do not edit data




    if(user_type == "caregiver"):
        auth = authorize_caregiver_action(caregiver_id, caregiver_pin)
        if auth == True:
            # todo - edit data
        else:
            # todo - do not edit data



def authorize_caregiver_action(auth_id, auth_pin):
    caregiver_data = find_elder_cpf(auth_id)

    if caregiver_data["exists"] == True:
        if caregiver_data["pin"] == auth_pin:
            return True
        else:
            return False
    else:
        return False


def set_data(ref, new_data):
    result ='''