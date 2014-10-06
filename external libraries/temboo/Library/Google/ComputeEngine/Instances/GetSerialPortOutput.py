# -*- coding: utf-8 -*-

###############################################################################
#
# GetSerialPortOutput
# Returns the specified instance's serial port output.
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

class GetSerialPortOutput(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetSerialPortOutput Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetSerialPortOutput, self).__init__(temboo_session, '/Library/Google/ComputeEngine/Instances/GetSerialPortOutput')


    def new_input_set(self):
        return GetSerialPortOutputInputSet()

    def _make_result_set(self, result, path):
        return GetSerialPortOutputResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetSerialPortOutputChoreographyExecution(session, exec_id, path)

class GetSerialPortOutputInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetSerialPortOutput
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        super(GetSerialPortOutputInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        super(GetSerialPortOutputInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        super(GetSerialPortOutputInputSet, self)._set_input('ClientSecret', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) Comma-seperated list of fields you want to include in the response.)
        """
        super(GetSerialPortOutputInputSet, self)._set_input('Fields', value)
    def set_Instance(self, value):
        """
        Set the value of the Instance input for this Choreo. ((required, string) The name of the instance associated with the serial port output to retrieve.)
        """
        super(GetSerialPortOutputInputSet, self)._set_input('Instance', value)
    def set_Project(self, value):
        """
        Set the value of the Project input for this Choreo. ((required, string) The ID of a Google Compute project.)
        """
        super(GetSerialPortOutputInputSet, self)._set_input('Project', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(GetSerialPortOutputInputSet, self)._set_input('RefreshToken', value)
    def set_Zone(self, value):
        """
        Set the value of the Zone input for this Choreo. ((required, string) The name of the zone associated with this request.)
        """
        super(GetSerialPortOutputInputSet, self)._set_input('Zone', value)

class GetSerialPortOutputResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetSerialPortOutput Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Google.)
        """
        return self._output.get('Response', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)

class GetSerialPortOutputChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetSerialPortOutputResultSet(response, path)
