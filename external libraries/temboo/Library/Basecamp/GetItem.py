# -*- coding: utf-8 -*-

###############################################################################
#
# GetItem
# Retrieves a single, specified item in a To-do list.
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
        super(GetItem, self).__init__(temboo_session, '/Library/Basecamp/GetItem')


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
    def set_AccountName(self, value):
        """
        Set the value of the AccountName input for this Choreo. ((required, string) A valid Basecamp account name. This is the first part of the account's URL.)
        """
        super(GetItemInputSet, self)._set_input('AccountName', value)
    def set_ItemID(self, value):
        """
        Set the value of the ItemID input for this Choreo. ((required, integer) The ID of the item to return.)
        """
        super(GetItemInputSet, self)._set_input('ItemID', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The Basecamp account password. Use the value 'X' when specifying an API Key for the Username input.)
        """
        super(GetItemInputSet, self)._set_input('Password', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) A Basecamp account username or API Key.)
        """
        super(GetItemInputSet, self)._set_input('Username', value)

class GetItemResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetItem Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response returned from Basecamp.)
        """
        return self._output.get('Response', None)

class GetItemChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetItemResultSet(response, path)
