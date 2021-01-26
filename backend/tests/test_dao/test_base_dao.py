import sys

sys.path.append('.')

from backend.dao.base_dao import BaseDao
from backend.models.seller_model import Seller
from backend.dao.session import Session


class TestBaseDao:
    DAO = BaseDao(Seller)
    name = '%%@@^&&*@'
    phone = '41-99955533'
    email = 'mail@mail.com'

    def test_instantiate_a_class(self) -> None:
        assert isinstance(self.DAO, BaseDao)

    def test_save(self) -> None:
        seller = Seller(self.name, self.email, self.phone)
        self.DAO.save(seller)
        with Session() as session:
            model = session.query(Seller).filter_by(fullname=self.name).first()
        model_name = model.fullname
        model_phone = model.phone
        model_email = model.email
        assert model_name == self.name
        assert model_phone == self.phone
        assert model_email == self.email
        self.DAO.delete(seller)

    def test_read_all(self) -> None:
        result = self.DAO.read_all()
        assert isinstance(result, list)

    def test_read_by_id(self) -> None:
        seller = Seller(self.name, self.email, self.phone)
        self.DAO.save(seller)
        with Session() as session:
            model = session.query(Seller).filter_by(fullname=self.name).first()
        id_ = model.id
        seller_from_database = self.DAO.read_by_id(id_)
        model_name = seller_from_database.fullname
        model_phone = seller_from_database.phone
        model_email = seller_from_database.email
        assert model_name == self.name
        assert model_phone == self.phone
        assert model_email == self.email
        self.DAO.delete(seller)

    def test_delete(self) -> None:
        seller = Seller(self.name, self.email, self.phone)
        self.DAO.save(seller)
        with Session() as session:
            model = session.query(Seller).filter_by(fullname=self.name).first()
        id_ = model.id
        seller_from_database = self.DAO.read_by_id(id_)
        self.DAO.delete(seller_from_database)
        seller_after_delete = self.DAO.read_by_id(id_)
        assert seller_after_delete is None



def start_test_base_dao() -> None:
    test_base_dao = TestBaseDao()
    test_base_dao.test_instantiate_a_class()
    test_base_dao.test_save()
    test_base_dao.test_read_all()
    test_base_dao.test_read_by_id()
    test_base_dao.test_delete()


start_test_base_dao()
