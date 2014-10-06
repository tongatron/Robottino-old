# -*- coding: utf-8 -*-

###############################################################################
#
# GenerateAuthToken
# Generates an authentication token.
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

class GenerateAuthToken(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GenerateAuthToken Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GenerateAuthToken, self).__init__(temboo_session, '/Library/Zoho/CRM/GenerateAuthToken')


    def new_input_set(self):
        return GenerateAuthTokenInputSet()

    def _make_result_set(self, result, path):
        return GenerateAuthTokenResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GenerateAuthTokenChoreographyExecution(session, exec_id, path)

class GenerateAuthTokenInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GenerateAuthToken
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, string) Your Zoho password.)
        """
        super(GenerateAuthTokenInputSet, self)._set_input('Password', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your Zoho CRM username.)
        """
        super(GenerateAuthTokenInputSet, self)._set_input('Username', value)

class GenerateAuthTokenResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GenerateAuthToken Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_AuthenticationToken(self):
        """
        Retrieve the value for the "AuthenticationToken" output from this Choreo execution. ((string) The authentication token returned from Zoho.)
        """
        return self._output.get('AuthenticationToken', None)

class GenerateAuthTokenChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GenerateAuthTokenResultSet(response, path)
