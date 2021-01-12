class Seller:
    def __init__(self, fullname: str, email: str, phone: str, id: int = None):
        self.id = id
        self.fullname = fullname
        self.email = email
        self.phone = phone
