import json
import os

from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class OrdersAPI(APIView):
    def get(self, request):
        """
        You will receive date parameter, and if not received you should a bad request status.
        For statuses use the imported "status" module
        """

        if "date" not in request.query_params:
            return Response(
                {"message": "date param is required and not provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Add OrdersGrouperData class that should return:
        # 1. Orders data with grouped products by "location".
        # [
        # {
        #
        # }
        # ]
        # 2. It also should return information on bad tolocations, where bad tolocations
        # are those used across multiple Orders.
        # 3. Additional query params like products, pickers can be passed
        # which should lead to additional data returned by this API
        # 3.1. Products: response should include following data
        # products: {
        #   product_code: {quantity: 50, pickers: 10, locations: 25, tolocations: 5}
        # }
        # 3.2. Pickers: response should include following data
        # pickers: [unique pickers list]
        # 4. As a final query param, you should expect "export=csv|xml", which based on the other
        # query params should produce an appropriate response (file). Exports can be tricky,
        # especially the XML format, which would require building of a totally different documents.
        # You may, or you may not use several additional grouping and / or error collecting classes.

        # By default, the Response status return status 200 which is totally fine.
        return Response()
