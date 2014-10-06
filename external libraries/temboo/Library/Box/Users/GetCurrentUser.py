# -*- coding: utf-8 -*-

###############################################################################
#
# GetCurrentUser
# Retrieves information about the authenticated user.
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

class GetCurrentUser(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetCurrentUser Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetCurrentUser, self).__init__(temboo_session, '/Library/Box/Users/GetCurrentUser')


    def new_input_set(self):
        return GetCurrentUserInputSet()

    def _make_result_set(self, result, path):
        return GetCurrentUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCurrentUserChoreographyExecution(session, exec_id, path)

class GetCurrentUserInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetCurrentUser
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth2 process.)
        """
        super(GetCurrentUserInputSet, self)._set_input('AccessToken', value)
    def set_AsUser(self, value):
        """
        Set the value of the AsUser input for this Choreo. ((optional, string) The ID of the user. Only used for enterprise administrators to make API calls for their managed users.)
        """
        super(GetCurrentUserInputSet, self)._set_input('AsUser', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma-separated list of fields to include in the response.)
        """
        super(GetCurrentUserInputSet, self)._set_input('Fields', value)


class GetCurrentUserResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetCurrentUser Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Box.)
        """
        return self._output.get('Response', None)

class GetCurrentUserChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetCurrentUserResultSet(response, path)
