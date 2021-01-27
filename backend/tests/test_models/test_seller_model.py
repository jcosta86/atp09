import sys 
sys.path.append('.')

from backend.models.seller_model import Seller

class TestSellerModel:
    seller_fullname = 'Seller_Name'
    seller_phone = '41-9999665'
    seller_email = 'seller@email.com'
    seller_id = 12
    
    def test_atributes(self) -> None:
        seller = Seller(self.seller_fullname, self.seller_email, self.seller_phone,  self.seller_id)
        assert isinstance(seller, Seller)
        assert seller.fullname is self.seller_fullname
        assert seller.phone is self.seller_phone
        assert seller.email is self.seller_email
        assert seller.id is self.seller_id

    def test_validator_blank_name(self) -> None:
        seller = Seller(self.seller_fullname, self.seller_email, self.seller_phone)
        try:
            seller.fullname = '' 
        except Exception as error:
            assert isinstance(error, ValueError)

    def test_validator_blank_email(self) -> None:
        seller = Seller(self.seller_fullname, self.seller_email, self.seller_phone)
        try:
            seller.email = '' 
        except Exception as error:
            assert isinstance(error, ValueError)

    def test_validator_blank_phone(self) -> None:
        seller = Seller(self.seller_fullname, self.seller_email, self.seller_phone)
        try:
            seller.phone = '' 
        except Exception as error:
            assert isinstance(error, ValueError)

def start_test_seller_model():
    test_seller_model = TestSellerModel()
    test_seller_model.test_atributes()
    test_seller_model.test_validator_blank_name()
    test_seller_model.test_validator_blank_email()
    test_seller_model.test_validator_blank_phone()
   
start_test_seller_model()