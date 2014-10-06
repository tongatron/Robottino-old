# -*- coding: utf-8 -*-

###############################################################################
#
# ClientLoginAuthentication
# Request an authorization token for Google Analytics.
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

class ClientLoginAuthentication(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ClientLoginAuthentication Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ClientLoginAuthentication, self).__init__(temboo_session, '/Library/Google/Analytics/ClientLoginAuthentication')


    def new_input_set(self):
        return ClientLoginAuthenticationInputSet()

    def _make_result_set(self, result, path):
        return ClientLoginAuthenticationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ClientLoginAuthenticationChoreographyExecution(session, exec_id, path)

class ClientLoginAuthenticationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ClientLoginAuthentication
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google password.)
        """
        super(ClientLoginAuthenticationInputSet, self)._set_input('Password', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your full Google email address e.g., martha.temboo@gmail.com.)
        """
        super(ClientLoginAuthenticationInputSet, self)._set_input('Username', value)

class ClientLoginAuthenticationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ClientLoginAuthentication Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_AuthorizationKey(self):
        """
        Retrieve the value for the "AuthorizationKey" output from this Choreo execution. ((string) The authorization key which is parsed from the Google response.)
        """
        return self._output.get('AuthorizationKey', None)

class ClientLoginAuthenticationChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ClientLoginAuthenticationResultSet(response, path)
