# -*- coding: utf-8 -*-

###############################################################################
#
# ListOrderItems
# Returns order items based on a specified AmazonOrderId.
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

class ListOrderItems(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListOrderItems Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListOrderItems, self).__init__(temboo_session, '/Library/Amazon/Marketplace/Orders/ListOrderItems')


    def new_input_set(self):
        return ListOrderItemsInputSet()

    def _make_result_set(self, result, path):
        return ListOrderItemsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListOrderItemsChoreographyExecution(session, exec_id, path)

class ListOrderItemsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListOrderItems
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(ListOrderItemsInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSMarketplaceId(self, value):
        """
        Set the value of the AWSMarketplaceId input for this Choreo. ((required, string) The Marketplace ID provided by Amazon Web Services.)
        """
        super(ListOrderItemsInputSet, self)._set_input('AWSMarketplaceId', value)
    def set_AWSMerchantId(self, value):
        """
        Set the value of the AWSMerchantId input for this Choreo. ((required, string) The Merchant ID provided by Amazon Web Services.)
        """
        super(ListOrderItemsInputSet, self)._set_input('AWSMerchantId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(ListOrderItemsInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_AmazonOrderId(self, value):
        """
        Set the value of the AmazonOrderId input for this Choreo. ((required, string) An Amazon-defined order identifier.)
        """
        super(ListOrderItemsInputSet, self)._set_input('AmazonOrderId', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        super(ListOrderItemsInputSet, self)._set_input('Endpoint', value)
    def set_PageToken(self, value):
        """
        Set the value of the PageToken input for this Choreo. ((optional, string) The value returned in the NextPageToken output of this Choreo when there are multiple pages of order items to retrieve.)
        """
        super(ListOrderItemsInputSet, self)._set_input('PageToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(ListOrderItemsInputSet, self)._set_input('ResponseFormat', value)

class ListOrderItemsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListOrderItems Choreo.
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

class ListOrderItemsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListOrderItemsResultSet(response, path)
