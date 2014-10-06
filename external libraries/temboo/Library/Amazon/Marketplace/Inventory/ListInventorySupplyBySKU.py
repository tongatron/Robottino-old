# -*- coding: utf-8 -*-

###############################################################################
#
# ListInventorySupplyBySKU
# Returns information about the availability of a seller's inventory using a given SellerSKU.
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

class ListInventorySupplyBySKU(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListInventorySupplyBySKU Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListInventorySupplyBySKU, self).__init__(temboo_session, '/Library/Amazon/Marketplace/Inventory/ListInventorySupplyBySKU')


    def new_input_set(self):
        return ListInventorySupplyBySKUInputSet()

    def _make_result_set(self, result, path):
        return ListInventorySupplyBySKUResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListInventorySupplyBySKUChoreographyExecution(session, exec_id, path)

class ListInventorySupplyBySKUInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListInventorySupplyBySKU
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(ListInventorySupplyBySKUInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSMarketplaceId(self, value):
        """
        Set the value of the AWSMarketplaceId input for this Choreo. ((required, string) The Marketplace ID provided by Amazon Web Services.)
        """
        super(ListInventorySupplyBySKUInputSet, self)._set_input('AWSMarketplaceId', value)
    def set_AWSMerchantId(self, value):
        """
        Set the value of the AWSMerchantId input for this Choreo. ((required, string) The Merchant ID provided by Amazon Web Services.)
        """
        super(ListInventorySupplyBySKUInputSet, self)._set_input('AWSMerchantId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(ListInventorySupplyBySKUInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        super(ListInventorySupplyBySKUInputSet, self)._set_input('Endpoint', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(ListInventorySupplyBySKUInputSet, self)._set_input('ResponseFormat', value)
    def set_ResponseGroup(self, value):
        """
        Set the value of the ResponseGroup input for this Choreo. ((optional, string) Indicates whether or not to return the SupplyDetail element in the response. Valid values are: "Basic" (does not include SupplyDetail), and "Detailed" (includes SupplyDetail). Defaults to "Basic".)
        """
        super(ListInventorySupplyBySKUInputSet, self)._set_input('ResponseGroup', value)
    def set_SellerSKU(self, value):
        """
        Set the value of the SellerSKU input for this Choreo. ((required, string) A seller SKU for an item that you want inventory availability information about.)
        """
        super(ListInventorySupplyBySKUInputSet, self)._set_input('SellerSKU', value)

class ListInventorySupplyBySKUResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListInventorySupplyBySKU Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (Stores the response from Amazon.)
        """
        return self._output.get('Response', None)

class ListInventorySupplyBySKUChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListInventorySupplyBySKUResultSet(response, path)
