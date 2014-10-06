# -*- coding: utf-8 -*-

###############################################################################
#
# GetConnectApp
# Retrieves the details for an individual Connect App associated with a Twilio account.
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

class GetConnectApp(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetConnectApp Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetConnectApp, self).__init__(temboo_session, '/Library/Twilio/ConnectApps/GetConnectApp')


    def new_input_set(self):
        return GetConnectAppInputSet()

    def _make_result_set(self, result, path):
        return GetConnectAppResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetConnectAppChoreographyExecution(session, exec_id, path)

class GetConnectAppInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetConnectApp
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountSID(self, value):
        """
        Set the value of the AccountSID input for this Choreo. ((required, string) The AccountSID provided when you signed up for a Twilio account.)
        """
        super(GetConnectAppInputSet, self)._set_input('AccountSID', value)
    def set_AuthToken(self, value):
        """
        Set the value of the AuthToken input for this Choreo. ((required, string) The authorization token provided when you signed up for a Twilio account.)
        """
        super(GetConnectAppInputSet, self)._set_input('AuthToken', value)
    def set_ConnectAppSID(self, value):
        """
        Set the value of the ConnectAppSID input for this Choreo. ((required, string) The id of the Connect App to retrieve.)
        """
        super(GetConnectAppInputSet, self)._set_input('ConnectAppSID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetConnectAppInputSet, self)._set_input('ResponseFormat', value)

class GetConnectAppResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetConnectApp Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Twilio.)
        """
        return self._output.get('Response', None)

class GetConnectAppChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetConnectAppResultSet(response, path)
