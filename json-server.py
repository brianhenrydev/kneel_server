from http.server import HTTPServer
import json
from nss_handler import RequestHandler, status
from views import OrderQuery, MetalQuery, StyleQuery, SizeQuery

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
                response_body = OrderQuery().get_all_orders(url)
                return self.response(response_body, status.HTTP_200_SUCCESS)
            else:
                pk = query_params["pk"]
                response_body = OrderQuery().get_single_order(pk)
                return self.response(response_body, status.HTTP_200_SUCCESS)

        elif url["requested_resource"] == "metals":

            if "pk" not in query_params:
                response_body = MetalQuery().get_all_metals()
                return self.response(response_body, status.HTTP_200_SUCCESS)
            else:
                pk = query_params["pk"]
                response_body = MetalQuery().get_metal(pk)
            return self.response(response_body, status.HTTP_200_SUCCESS)
        elif url["requested_resource"] == "styles":

            if "pk" not in query_params:
                response_body = StyleQuery().get_all_styles()
                return self.response(response_body, status.HTTP_200_SUCCESS)
            else:
                pk = query_params["pk"]
                response_body = get_style(pk)
                return self.response(response_body, status.HTTP_200_SUCCESS)
        elif url["requested_resource"] == "sizes":

            if "pk" not in query_params:
                response_body = SizeQuery().get_table()
                return self.response(response_body, status.HTTP_200_SUCCESS)
            else:
                pk = query_params["pk"]
                response_body = SizeQuery().get_item(pk)
                return self.response(response_body, status.HTTP_200_SUCCESS)

        return self.response(
            response_body, status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND
        )

    def do_POST(self):
        # dict containing endpoint & query params from url
        url = self.parse_url(self.path)
        # gets length of content in post request
        content_length = int(self.headers.get("Content-Length"))
        # reads in content_length bytes?
        post_body = self.rfile.read(content_length)
        # decodes the bytes to string
        post_data = post_body.decode("utf-8")
        # converts the str data to dict
        new_order_dict = json.loads(post_data)

        if url["requested_resource"] == "orders":
            response_body = OrderQuery().add_order(new_order_dict)
            if response_body == "Order Created":
                return self.response(response_body, status.HTTP_201_SUCCESS_CREATED)
        return self.response("Oops...", status.HTTP_418_CLIENT_ERROR_IM_A_TEAPOT)

    def do_DELETE(self):
        # dict containing endpoint & query params from url
        url = self.parse_url(self.path)
        params = url["query_params"]

        if url["requested_resource"] == "orders":
            if "pk" in params:
                pk = params["pk"]
                response = OrderQuery().delete_item(pk)
                return self.response(response, status.HTTP_200_SUCCESS)

            return self.response(
                "No pk provided", status.HTTP_418_CLIENT_ERROR_IM_A_TEAPOT
            )

    def do_PUT(self):
        url = self.parse_url(self.path)
        content_length = int(self.headers.get("Content-Length"))

        post_body = self.rfile.read(content_length)
        post_data = post_body.decode("utf-8")


        updated_order = json.loads(post_data)

        if url["requested_resource"] == "metals":
            order_id = url["pk"]
            updated_price = updated_order["price"]
            if MetalQuery().update_metal(order_id, updated_price):
                return self.response("Updated row", status.HTTP_200_SUCCESS)


#
# THE CODE BELOW THIS LINE IS NOT IMPORTANT FOR REACHING YOUR LEARNING OBJECTIVES
#
def main():
    host = ""
    port = 8000
    HTTPServer((host, port), JSONServer).serve_forever()


if __name__ == "__main__":
    print(banner)
    main()
