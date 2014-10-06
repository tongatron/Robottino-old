# -*- coding: utf-8 -*-

###############################################################################
#
# GetItem
# Returns item data such as title, description, price information, and seller information.
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

class GetItem(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetItem Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetItem, self).__init__(temboo_session, '/Library/eBay/Trading/GetItem')


    def new_input_set(self):
        return GetItemInputSet()

    def _make_result_set(self, result, path):
        return GetItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetItemChoreographyExecution(session, exec_id, path)

class GetItemInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetItem
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_DetailLevel(self, value):
        """
        Set the value of the DetailLevel input for this Choreo. ((optional, string) The response detail level. Valid values are: ItemReturnAttributes, ItemReturnDescription, and ReturnAll.)
        """
        super(GetItemInputSet, self)._set_input('DetailLevel', value)
    def set_IncludeItemSpecifics(self, value):
        """
        Set the value of the IncludeItemSpecifics input for this Choreo. ((optional, boolean) If set to true, the response returns the ItemSpecifics node (if the listing has custom Item Specifics).)
        """
        super(GetItemInputSet, self)._set_input('IncludeItemSpecifics', value)
    def set_IncludeTaxTable(self, value):
        """
        Set the value of the IncludeTaxTable input for this Choreo. ((optional, boolean) If set to true, an associated tax table is returned in the response.)
        """
        super(GetItemInputSet, self)._set_input('IncludeTaxTable', value)
    def set_IncludeWatchCount(self, value):
        """
        Set the value of the IncludeWatchCount input for this Choreo. ((optional, boolean) Indicates if the caller wants to include watch count for that item in the response when set to true. Only the seller is allowed to use this argument.)
        """
        super(GetItemInputSet, self)._set_input('IncludeWatchCount', value)
    def set_ItemID(self, value):
        """
        Set the value of the ItemID input for this Choreo. ((required, string) The ItemID that uniquely identifies the item listing to retrieve.)
        """
        super(GetItemInputSet, self)._set_input('ItemID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetItemInputSet, self)._set_input('ResponseFormat', value)
    def set_SandboxMode(self, value):
        """
        Set the value of the SandboxMode input for this Choreo. ((optional, boolean) Indicates that the request should be made to the sandbox endpoint instead of the production endpoint. Set to 1 to enable sandbox mode.)
        """
        super(GetItemInputSet, self)._set_input('SandboxMode', value)
    def set_SiteID(self, value):
        """
        Set the value of the SiteID input for this Choreo. ((optional, string) The eBay site ID that you want to access. Defaults to 0 indicating the US site.)
        """
        super(GetItemInputSet, self)._set_input('SiteID', value)
    def set_TransactionID(self, value):
        """
        Set the value of the TransactionID input for this Choreo. ((optional, string) A unique identifier for a transaction (i.e.  an order line item). An order line item is created when the buyer commits to purchasing an item.)
        """
        super(GetItemInputSet, self)._set_input('TransactionID', value)
    def set_UserToken(self, value):
        """
        Set the value of the UserToken input for this Choreo. ((required, string) A valid eBay Auth Token.)
        """
        super(GetItemInputSet, self)._set_input('UserToken', value)

class GetItemResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetItem Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from eBay.)
        """
        return self._output.get('Response', None)

class GetItemChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetItemResultSet(response, path)
