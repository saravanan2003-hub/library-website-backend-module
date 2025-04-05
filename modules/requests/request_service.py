from .request_model import Request, requestDAO
from .request_schema import RequestCreate 
from .request_validator import RequestValidator
from uuid import UUID



class RequestService:
    
    def create_request(self, request_data:RequestCreate):
        request = requestDAO.create_request(self, request_data)
        return request
    
    def get_all_request(self):
        requests = requestDAO.get_requests(self)
        return requests
    
    def get_request_by_id(self, request_id: UUID): 
        RequestValidator.validate_request_id(self, request_id)
        request = requestDAO.get_request_by_id(self, request_id)
        return request
    
    def update_request(self, request_id:UUID , request_data:RequestCreate):
        RequestValidator.validate_request_id(self, request_id)
        request = requestDAO.update_request(self, request_id, request_data)
        return request
    
    def delete_request(self, request_id:UUID):
        RequestValidator.validate_request_id(self, request_id) 
        request = requestDAO.delete_request(self, request_id)
        return request

    def get_request_by_user_id(self, user_id:UUID):
        RequestValidator.validate_user_id(self, user_id)
        requests = requestDAO.get_request_by_user_id(self, user_id)
        return requests
    
    def get_request_by_book_id(self, book_id:UUID):
        RequestValidator.validate_book_id(self, book_id)
        requests = requestDAO.get_request_by_book_id(self, book_id)
        return requests
    
    
        