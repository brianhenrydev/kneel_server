from enum import Enum
from urllib.parse import urlparse,parse_qs 
from http.server import BaseHTTPRequestHandler


class status(Enum):
    HTTP_405_CLIENT_ERROR_METHOD_NOT_ALLOWED = 405
    
    HTTP_200_SUCCESS = 200
    HTTP_201_SUCCESS_CREATED = 201
    HTTP_204_SUCCESS_NO_RESPONSE_BODY = 204
    HTTP_418_CLIENT_ERROR_IM_A_TEAPOT = 418
    
    
    HTTP_400_CLIENT_ERROR_BAD_REQUEST_DATA = 400
    HTTP_401_CLIENT_ERROR_UNAUTHORIZED = 401
    HTTP_402_CLIENT_ERROR_PAYMENT_REQUIRED = 402
    HTTP_403_CLIENT_ERROR_FORBIDDEN = 403
    HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND = 404
    HTTP_406_CLIENT_ERROR_NOT_ACCEPTABLE = 406
    HTTP_408_CLIENT_ERROR_REQUEST_TIMEOUT = 408
    HTTP_410_CLIENT_ERROR_GONE = 410
    HTTP_412_CLIENT_ERROR_PRECONDITION_FAILED = 412
    HTTP_417_CLIENT_ERROR_EXPECTATION_FAILED = 417
    HTTP_421_CLIENT_ERROR_MISDIRECTED_REQUEST = 421
    HTTP_422_CLIENT_ERROR_UNPROCESSABLE_ENTITY = 422
    HTTP_429_CLIENT_ERROR_TOO_MANY_REQUESTS = 429
    HTTP_451_CLIENT_ERROR_UNAVAILABLE_FOR_LEGAL_REASONS = 451
    
    HTTP_500_SERVER_ERROR = 500
    HTTP_501_SERVER_ERROR_NOT_IMPLEMENTED = 501
    HTTP_502_SERVER_ERROR_BAD_GATEWAY = 502
    HTTP_503_SERVER_ERROR_SERVICE_UNAVAILABLE = 503
    HTTP_504_SERVER_ERROR_GATEWAY_TIMEOUT = 5

class RequestHandler(BaseHTTPRequestHandler):

    def response(self,body,status_code):
        """Response"""
        self.set_res_code(status_code)
        self.wfile.write(body.encode())

    def parse_url(self,path):
        """Parse url into resource and id"""
        parsed = urlparse(path)
        params = parsed.path.split('/')
        resource = params[1]

        url_dict = {
            "requested_resource": resource,
            "query_params": {},
            "pk": 0
        }

        if not parsed.query:
            pass
        else:
            query = parse_qs(parsed.query)
            url_dict["query_params"] = query
            try:
                if "pk" in url_dict["query_params"]:
                    pk = int(query["pk"][0])
                    url_dict["pk"] = pk
            except (IndexError, ValueError):
                pass
              
        return url_dict



    def set_res_code(self, status_code):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
 
    def do_OPTS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()
