class Search_Result_Information:
    def __init__(self):
        self._exists = False
        self._user_type = ""
        self._user_data = {}

    def set_exists(self, exists):
        self._exists = exists

    def set_user_type(self, user_type):
        self._user_type = user_type

    def set_user_data(self, user_data):
        self._user_data = user_data

    def get_user_information(self):
        return {
            "exists": self._exists,
            "user_type": self._user_type,
            "user_data": self._user_data
        }