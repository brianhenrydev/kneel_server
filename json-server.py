import json
from http.server import HTTPServer
from nss_handler import RequestHandler, status
from views.order_view import get_all_orders, get_order

banner = r"""
                                                       _ 
 ___  ___ _ ____   _____ _ __   _ __ _   _ _ __  _ __ (_)_ __   __ _       
/ __|/ _ \ '__\ \ / / _ \ '__| | '__| | | | '_ \| '_ \| | '_ \ / _` |      
\__ \  __/ |   \ V /  __/ |    | |  | |_| | | | | | | | | | | | (_| |_ _ _ 
|___/\___|_|    \_/ \___|_|    |_|   \__,_|_| |_|_| |_|_|_| |_|\__, (_|_|_)
                                                               |___/       
Probably... Maybe?
"""

# Add your imports below this line


class JSONServer(RequestHandler):
    """Server class to handle incoming HTTP requests for shipping ships"""

    def do_GET(self):
        """Handle GET requests from a client"""

        response_body = ""
        url = self.parse_url(self.path)
        query_params = url["query_params"]
        if url["requested_resource"] == "orders":
            if "pk" not in query_params:
                response_body = get_all_orders()
                return self.response(response_body, status.HTTP_200_SUCCESS.value)
            else:
                pk = query_params["pk"]
                response_body = get_order(pk)
                return self.response(response_body, status.HTTP_200_SUCCESS.value)

        return self.response(response_body, status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)






#
# THE CODE BELOW THIS LINE IS NOT IMPORTANT FOR REACHING YOUR LEARNING OBJECTIVES
#
def main():
    host = ''
    port = 8000
    HTTPServer((host, port), JSONServer).serve_forever()

if __name__ == "__main__":
    print(banner)
    main()

