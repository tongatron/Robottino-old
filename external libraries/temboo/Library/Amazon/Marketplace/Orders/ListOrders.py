# -*- coding: utf-8 -*-

###############################################################################
#
# ListOrders
# Returns orders created during a time frame that you specify.
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListOrders(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListOrders Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListOrders, self).__init__(temboo_session, '/Library/Amazon/Marketplace/Orders/ListOrders')


    def new_input_set(self):
        return ListOrdersInputSet()

    def _make_result_set(self, result, path):
        return ListOrdersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListOrdersChoreographyExecution(session, exec_id, path)

class ListOrdersInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListOrders
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(ListOrdersInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSMarketplaceId(self, value):
        """
        Set the value of the AWSMarketplaceId input for this Choreo. ((required, string) The Marketplace ID provided by Amazon Web Services.)
        """
        super(ListOrdersInputSet, self)._set_input('AWSMarketplaceId', value)
    def set_AWSMerchantId(self, value):
        """
        Set the value of the AWSMerchantId input for this Choreo. ((required, string) The Merchant ID provided by Amazon Web Services.)
        """
        super(ListOrdersInputSet, self)._set_input('AWSMerchantId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(ListOrdersInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_CreatedAfter(self, value):
        """
        Set the value of the CreatedAfter input for this Choreo. ((optional, date) A date used for selecting orders created after (or at) a specified time, in ISO 8601 date format (i.e. 2012-01-01). Defaults to today's date if not provided.)
        """
        super(ListOrdersInputSet, self)._set_input('CreatedAfter', value)
    def set_CreatedBefore(self, value):
        """
        Set the value of the CreatedBefore input for this Choreo. ((optional, date) A date used for selecting orders created before (or at) a specified time, in ISO 8601 date format (i.e. 2012-01-01).)
        """
        super(ListOrdersInputSet, self)._set_input('CreatedBefore', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        super(ListOrdersInputSet, self)._set_input('Endpoint', value)
    def set_FullfillmentChannel(self, value):
        """
        Set the value of the FullfillmentChannel input for this Choreo. ((optional, string) A string indicating how an order was fulfilled. Use "AFN" for Amazon fulfilled orders, and "MFN" for seller fulfilled orders.)
        """
        super(ListOrdersInputSet, self)._set_input('FullfillmentChannel', value)
    def set_MaxResultsPerPage(self, value):
        """
        Set the value of the MaxResultsPerPage input for this Choreo. ((optional, integer) A number that indicates the maximum number of orders that can be returned per page. Valid values are: 1-100.)
        """
        super(ListOrdersInputSet, self)._set_input('MaxResultsPerPage', value)
    def set_OrderStatus(self, value):
        """
        Set the value of the OrderStatus input for this Choreo. ((optional, string) An OrderStatus value to select only orders with a certain status. Valid values are: Pending, Unshipped, PartiallyShipped, Shipped, Canceled, Unfulfillable.)
        """
        super(ListOrdersInputSet, self)._set_input('OrderStatus', value)
    def set_PageToken(self, value):
        """
        Set the value of the PageToken input for this Choreo. ((optional, string) The value returned in the NextPageToken output of this Choreo when there are multiple pages of orders to retrieve.)
        """
        super(ListOrdersInputSet, self)._set_input('PageToken', value)
    def set_PaymentMethod(self, value):
        """
        Set the value of the PaymentMethod input for this Choreo. ((optional, string) Used to select only orders of a certain payment type. Valid values are: COD (cash on delivery), CSV (convenience store payment), or Other (Any payment method other than COD or CVS).)
        """
        super(ListOrdersInputSet, self)._set_input('PaymentMethod', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(ListOrdersInputSet, self)._set_input('ResponseFormat', value)

class ListOrdersResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListOrders Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (Stores the response from Amazon.)
        """
        return self._output.get('Response', None)
    def get_NextPageToken(self):
        """
        Retrieve the value for the "NextPageToken" output from this Choreo execution. ((string) A token used to retrieve the next page of results. If a token is not returned, there are no more results to retrieve. This token can be passed to the PageToken input of this Choreo.)
        """
        return self._output.get('NextPageToken', None)

class ListOrdersChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListOrdersResultSet(response, path)
