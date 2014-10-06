# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteItem
# Deletes a specified item from a To-do list.
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

class DeleteItem(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteItem Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteItem, self).__init__(temboo_session, '/Library/Basecamp/DeleteItem')


    def new_input_set(self):
        return DeleteItemInputSet()

    def _make_result_set(self, result, path):
        return DeleteItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteItemChoreographyExecution(session, exec_id, path)

class DeleteItemInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteItem
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountName(self, value):
        """
        Set the value of the AccountName input for this Choreo. ((required, string) A valid Basecamp account name. This is the first part of the account's URL.)
        """
        super(DeleteItemInputSet, self)._set_input('AccountName', value)
    def set_ItemID(self, value):
        """
        Set the value of the ItemID input for this Choreo. ((required, integer) The ID for the list item to delete.)
        """
        super(DeleteItemInputSet, self)._set_input('ItemID', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The Basecamp account password. Use the value 'X' when specifying an API Key for the Username input.)
        """
        super(DeleteItemInputSet, self)._set_input('Password', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) A Basecamp account username or API Key.)
        """
        super(DeleteItemInputSet, self)._set_input('Username', value)

class DeleteItemResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteItem Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (No structured response is returned for delete item requests.)
        """
        return self._output.get('Response', None)

class DeleteItemChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteItemResultSet(response, path)
