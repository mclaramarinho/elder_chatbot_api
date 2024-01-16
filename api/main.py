from flask import Flask, request, jsonify
from database_actions.create_caregiver import create_caregiver
from database_actions.create_elder import create_elder
from database_actions.find_user import find_user_phone

from firebase.setup import init_firebase_app

init_firebase_app()

app = Flask(__name__)

@app.get("/api/create/caregiver/")
def endpoint_create_caregiver():
    args = {
        "cpf": request.args.get("cpf"),
        "f_name": request.args.get("firstName"),
        "l_name": request.args.get("lastName"),
        "bday": request.args.get("birthday"),
        "phone": request.args.get("phoneNumber"),
        "pin": request.args.get("securityPin")
    }
    result = create_caregiver(cpf=args["cpf"], first_name=args["f_name"], last_name=args["l_name"], birthday=args["bday"], phone_number=args["phone"], pin=args["pin"])

    if result["message"] == "Success!":
        return jsonify(result), 200
    else:
        return jsonify(result), 500

@app.get("/api/create/elder/")
def endpoint_create_elder():
    args = {
        "cpf": request.args.get("cpf"),
        "f_name": request.args.get("firstName"),
        "l_name": request.args.get("lastName"),
        "bday": request.args.get("birthday"),
        "phone": request.args.get("phoneNumber"),
        "main_ec_name": request.args.get("mainECName"),
        "main_ec_phone": request.args.get("mainECPhone"),
        "sec_ec_name": request.args.get("secECName"),
        "sec_ec_phone": request.args.get("secECPhone"),
        "caregiver_cpf": request.args.get("caregiverCPF")
    }
    result = create_elder(cpf=args["cpf"], first_name=args["f_name"], last_name=args["l_name"],
                          birthday=args["bday"], phone_number=args["phone"], main_ec_name=args["main_ec_name"],
                          main_ec_phone=args["main_ec_phone"], sec_ec_name=args["sec_ec_name"],
                          sec_ec_phone=args["sec_ec_phone"], caregiver_cpf=args["caregiver_cpf"])

    if result["message"] == "Success!":
        return jsonify(result), 200
    else:
        return jsonify(result), 500

@app.get('/api/find/user')
def endpoint_find_user():
    phone_number = request.args.get("phoneNumber")
    result = find_user_phone(phone_number)
    return result

if __name__ == '__main__':
    app.run()