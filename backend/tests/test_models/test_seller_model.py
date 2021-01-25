import sys 
sys.path.append('.')

from backend.models.seller_model import Seller

class TestSellerModel:
    seller_name = 'Seller_Name'
    seller_phone = '41-9999665'
    seller_email = 'seller@email.com'
    seller_id = 12
    
    def test_atributes(self) -> None:
        seller = Seller(self.seller_name, self.seller_email, self.seller_phone,  self.seller_id)
        assert isinstance(seller, Seller)
        assert seller.fullname is self.seller_name
        assert seller.phone is self.seller_phone
        assert seller.email is self.seller_email
        assert seller.id is self.seller_id

def start_test_seller_model():
    test_seller_model = TestSellerModel()
    test_seller_model.test_atributes()
   
start_test_seller_model()