# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateUser
# Updates information for an existing user.
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

class UpdateUser(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateUser Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateUser, self).__init__(temboo_session, '/Library/Parse/Users/UpdateUser')


    def new_input_set(self):
        return UpdateUserInputSet()

    def _make_result_set(self, result, path):
        return UpdateUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateUserChoreographyExecution(session, exec_id, path)

class UpdateUserInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateUser
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_UserInformation(self, value):
        """
        Set the value of the UserInformation input for this Choreo. ((required, json) A JSON string containing the user information to update.)
        """
        super(UpdateUserInputSet, self)._set_input('UserInformation', value)
    def set_ApplicationID(self, value):
        """
        Set the value of the ApplicationID input for this Choreo. ((required, string) The Application ID provided by Parse.)
        """
        super(UpdateUserInputSet, self)._set_input('ApplicationID', value)
    def set_ObjectID(self, value):
        """
        Set the value of the ObjectID input for this Choreo. ((required, string) The ID of the user to update.)
        """
        super(UpdateUserInputSet, self)._set_input('ObjectID', value)
    def set_RESTAPIKey(self, value):
        """
        Set the value of the RESTAPIKey input for this Choreo. ((required, string) The REST API Key provided by Parse.)
        """
        super(UpdateUserInputSet, self)._set_input('RESTAPIKey', value)
    def set_SessionToken(self, value):
        """
        Set the value of the SessionToken input for this Choreo. ((required, string) A valid Session Token. Note that Session Tokens can be retrieved by the Login and SignUp Choreos.)
        """
        super(UpdateUserInputSet, self)._set_input('SessionToken', value)

class UpdateUserResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateUser Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Parse.)
        """
        return self._output.get('Response', None)

class UpdateUserChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateUserResultSet(response, path)
