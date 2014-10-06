# -*- coding: utf-8 -*-

###############################################################################
#
# EndItem
# Ends the specified item listing before the date and time that it is scheduled to end per the listing duration.
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

class EndItem(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the EndItem Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(EndItem, self).__init__(temboo_session, '/Library/eBay/Trading/EndItem')


    def new_input_set(self):
        return EndItemInputSet()

    def _make_result_set(self, result, path):
        return EndItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return EndItemChoreographyExecution(session, exec_id, path)

class EndItemInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the EndItem
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_EndingReason(self, value):
        """
        Set the value of the EndingReason input for this Choreo. ((required, string) The reason the listing is ending early. Valid values are: LostOrBroken, NotAvailable, Incorrect, OtherListingError, CustomCode, SellToHighBidder, or Sold.)
        """
        super(EndItemInputSet, self)._set_input('EndingReason', value)
    def set_ItemID(self, value):
        """
        Set the value of the ItemID input for this Choreo. ((required, string) The ID of the item to end.)
        """
        super(EndItemInputSet, self)._set_input('ItemID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(EndItemInputSet, self)._set_input('ResponseFormat', value)
    def set_SandboxMode(self, value):
        """
        Set the value of the SandboxMode input for this Choreo. ((optional, boolean) Indicates that the request should be made to the sandbox endpoint instead of the production endpoint. Set to 1 to enable sandbox mode.)
        """
        super(EndItemInputSet, self)._set_input('SandboxMode', value)
    def set_SellerInventoryID(self, value):
        """
        Set the value of the SellerInventoryID input for this Choreo. ((optional, string) Unique identifier that the seller specified when they listed the Half.com item. This paramater only applies to Half.com.)
        """
        super(EndItemInputSet, self)._set_input('SellerInventoryID', value)
    def set_SiteID(self, value):
        """
        Set the value of the SiteID input for this Choreo. ((optional, string) The eBay site ID that you want to access. Defaults to 0 indicating the US site.)
        """
        super(EndItemInputSet, self)._set_input('SiteID', value)
    def set_UserToken(self, value):
        """
        Set the value of the UserToken input for this Choreo. ((required, string) A valid eBay Auth Token.)
        """
        super(EndItemInputSet, self)._set_input('UserToken', value)

class EndItemResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the EndItem Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from eBay.)
        """
        return self._output.get('Response', None)

class EndItemChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return EndItemResultSet(response, path)
