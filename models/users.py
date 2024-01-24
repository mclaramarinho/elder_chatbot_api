import abc
from abc import abstractmethod, ABC


class User(ABC):
    def __init__(self, **kwargs):
        self.cpf = kwargs['cpf']
        self.first_name = kwargs['first_name']
        self.last_name = kwargs['last_name']
        self.birthday = kwargs['birthday']
        self.phone_number = kwargs['phone_number']
        self.uid = kwargs['uid']

    @abstractmethod
    def return_user_data(self):
        pass


class Elder(User):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.main_ec_name = kwargs['main_ec_name']
        self.main_ec_phone = kwargs['main_ec_phone']
        self.sec_ec_name = kwargs['sec_ec_name']
        self.sec_ec_phone = kwargs['sec_ec_phone']
        self.caregiver = kwargs['caregiver_uid']

    def return_user_data(self):
        return {
            "cpf": self.cpf,
            "name": {
                "first_name": self.first_name,
                "last_name": self.last_name
            },
            "uid": self.uid,
            "birthday": self.birthday,
            "phone_number": self.phone_number,
            "emergency_contacts":{
                "main": {
                    "name": self.main_ec_name,
                    "phone_number": self.main_ec_phone
                },
                "secondary": {
                    "name": self.sec_ec_name,
                    "phone_number": self.sec_ec_phone
                }
            },
            "caregiver": self.caregiver
        }


class Caregiver(User):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pin = kwargs['pin']

    def return_user_data(self):
        return {
            "cpf": self.cpf,
            "name": {
                "first_name": self.first_name,
                "last_name": self.last_name
            },
            "uid": self.uid,
            "birthday": self.birthday,
            "phone_number": self.phone_number,
            "pin": self.pin,
            "elders_associated": {}
        }
