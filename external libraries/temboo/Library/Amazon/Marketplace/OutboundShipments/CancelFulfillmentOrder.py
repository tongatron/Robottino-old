# -*- coding: utf-8 -*-

###############################################################################
#
# CancelFulfillmentOrder
# Makes a requests to Amazon to cancel an existing fulfillment order.
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

class CancelFulfillmentOrder(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CancelFulfillmentOrder Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CancelFulfillmentOrder, self).__init__(temboo_session, '/Library/Amazon/Marketplace/OutboundShipments/CancelFulfillmentOrder')


    def new_input_set(self):
        return CancelFulfillmentOrderInputSet()

    def _make_result_set(self, result, path):
        return CancelFulfillmentOrderResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CancelFulfillmentOrderChoreographyExecution(session, exec_id, path)

class CancelFulfillmentOrderInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CancelFulfillmentOrder
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(CancelFulfillmentOrderInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSMarketplaceId(self, value):
        """
        Set the value of the AWSMarketplaceId input for this Choreo. ((required, string) The Marketplace ID provided by Amazon Web Services.)
        """
        super(CancelFulfillmentOrderInputSet, self)._set_input('AWSMarketplaceId', value)
    def set_AWSMerchantId(self, value):
        """
        Set the value of the AWSMerchantId input for this Choreo. ((required, string) The Merchant ID provided by Amazon Web Services.)
        """
        super(CancelFulfillmentOrderInputSet, self)._set_input('AWSMerchantId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(CancelFulfillmentOrderInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        super(CancelFulfillmentOrderInputSet, self)._set_input('Endpoint', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(CancelFulfillmentOrderInputSet, self)._set_input('ResponseFormat', value)
    def set_SellerFulfillmentOrderId(self, value):
        """
        Set the value of the SellerFulfillmentOrderId input for this Choreo. ((required, string) The fulfillment order id that you created and submitted using the CreateFulfillmentOrder Choreo.)
        """
        super(CancelFulfillmentOrderInputSet, self)._set_input('SellerFulfillmentOrderId', value)

class CancelFulfillmentOrderResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CancelFulfillmentOrder Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) Stores the response from Amazon.)
        """
        return self._output.get('Response', None)

class CancelFulfillmentOrderChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CancelFulfillmentOrderResultSet(response, path)
