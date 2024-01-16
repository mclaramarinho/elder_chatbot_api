def data_structure(type, cpf, first_name, last_name, birthday, phone_number, main_ec_name = "", main_ec_phone = "", sec_ec_phone="", sec_ec_name="", pin="", caregiver_cpf=""):
    data = {
        "cpf": cpf,
        "name": {
            "first_name": first_name,
            "last_name": last_name
        },
        "birthday": birthday,
        "phone_number": phone_number,
    }
    try:
        if type == "elder":
            data["emergency_contacts"] = {
                "main": {
                    "name": main_ec_name,
                    "phone_number": main_ec_phone
                },
                "secondary": {
                    "name": sec_ec_name,
                    "phone_number": sec_ec_phone
                }
            }
            data["caregiver"] = caregiver_cpf
        elif type == "cg":
            data["pin"] = pin
            data["elders_associated"] = {}
        else:
            raise Exception("Invalid user type.")

        return data
    except Exception as e:
        print(e.__str__())
        return {"message": e.__str__()}

