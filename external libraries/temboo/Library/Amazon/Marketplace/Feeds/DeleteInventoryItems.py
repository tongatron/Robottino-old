# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteInventoryItems
# Deletes inventory listings from a Seller Central account with a given flat file of SKUs.
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

class DeleteInventoryItems(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteInventoryItems Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteInventoryItems, self).__init__(temboo_session, '/Library/Amazon/Marketplace/Feeds/DeleteInventoryItems')


    def new_input_set(self):
        return DeleteInventoryItemsInputSet()

    def _make_result_set(self, result, path):
        return DeleteInventoryItemsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteInventoryItemsChoreographyExecution(session, exec_id, path)

class DeleteInventoryItemsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteInventoryItems
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_SKUs(self, value):
        """
        Set the value of the SKUs input for this Choreo. ((conditional, multiline) The list of SKUs associating with the products to delete. SKUs are provided as Tab Delimited values (do not include a sku column name).)
        """
        super(DeleteInventoryItemsInputSet, self)._set_input('SKUs', value)
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(DeleteInventoryItemsInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSMarketplaceId(self, value):
        """
        Set the value of the AWSMarketplaceId input for this Choreo. ((required, string) The Marketplace ID provided by Amazon Web Services.)
        """
        super(DeleteInventoryItemsInputSet, self)._set_input('AWSMarketplaceId', value)
    def set_AWSMerchantId(self, value):
        """
        Set the value of the AWSMerchantId input for this Choreo. ((required, string) The Merchant ID provided by Amazon Web Services.)
        """
        super(DeleteInventoryItemsInputSet, self)._set_input('AWSMerchantId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(DeleteInventoryItemsInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_DeleteOptions(self, value):
        """
        Set the value of the DeleteOptions input for this Choreo. ((optional, string) Use 'd' to reduce the listings inventory to 0 and keep details in the system. Use 'x'  to completely delete listings from your current inventory. Defaults to "d".)
        """
        super(DeleteInventoryItemsInputSet, self)._set_input('DeleteOptions', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        super(DeleteInventoryItemsInputSet, self)._set_input('Endpoint', value)
    def set_TimeToWait(self, value):
        """
        Set the value of the TimeToWait input for this Choreo. ((optional, integer) By default, the Choreo will wait for 10 minutes to see if the report is ready for retrieval. Max is 120 minutes.)
        """
        super(DeleteInventoryItemsInputSet, self)._set_input('TimeToWait', value)


class DeleteInventoryItemsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteInventoryItems Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon after submitting the feed.)
        """
        return self._output.get('Response', None)
    def get_ProcessingStatus(self):
        """
        Retrieve the value for the "ProcessingStatus" output from this Choreo execution. ((string) The processing status of the feed submission which is parsed from the Amazon response.)
        """
        return self._output.get('ProcessingStatus', None)
    def get_SubmissionId(self):
        """
        Retrieve the value for the "SubmissionId" output from this Choreo execution. ((integer) The submission id parsed from the Amazon response.)
        """
        return self._output.get('SubmissionId', None)
    def get_SubmissionResult(self):
        """
        Retrieve the value for the "SubmissionResult" output from this Choreo execution. ((string) The submission result returned from Amazon.)
        """
        return self._output.get('SubmissionResult', None)

class DeleteInventoryItemsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteInventoryItemsResultSet(response, path)
