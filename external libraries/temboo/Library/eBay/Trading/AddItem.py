# -*- coding: utf-8 -*-

###############################################################################
#
# AddItem
# Defines a single new item and lists it on a specified eBay site.
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

class AddItem(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddItem Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(AddItem, self).__init__(temboo_session, '/Library/eBay/Trading/AddItem')


    def new_input_set(self):
        return AddItemInputSet()

    def _make_result_set(self, result, path):
        return AddItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddItemChoreographyExecution(session, exec_id, path)

class AddItemInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddItem
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AddItemRequest(self, value):
        """
        Set the value of the AddItemRequest input for this Choreo. ((required, xml) The complete XML request body containing item properties you wish to set.)
        """
        super(AddItemInputSet, self)._set_input('AddItemRequest', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(AddItemInputSet, self)._set_input('ResponseFormat', value)
    def set_SandboxMode(self, value):
        """
        Set the value of the SandboxMode input for this Choreo. ((optional, boolean) Indicates that the request should be made to the sandbox endpoint instead of the production endpoint. Set to 1 to enable sandbox mode.)
        """
        super(AddItemInputSet, self)._set_input('SandboxMode', value)
    def set_SiteID(self, value):
        """
        Set the value of the SiteID input for this Choreo. ((optional, string) The eBay site ID that you want to access. Defaults to 0 indicating the US site.)
        """
        super(AddItemInputSet, self)._set_input('SiteID', value)
    def set_UserToken(self, value):
        """
        Set the value of the UserToken input for this Choreo. ((required, string) A valid eBay Auth Token.)
        """
        super(AddItemInputSet, self)._set_input('UserToken', value)

class AddItemResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddItem Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from eBay.)
        """
        return self._output.get('Response', None)

class AddItemChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AddItemResultSet(response, path)
