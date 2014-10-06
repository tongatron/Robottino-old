# -*- coding: utf-8 -*-

###############################################################################
#
# InsertAddress
# Creates an Address resource in the specified project.
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

class InsertAddress(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the InsertAddress Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(InsertAddress, self).__init__(temboo_session, '/Library/Google/ComputeEngine/Addresses/InsertAddress')


    def new_input_set(self):
        return InsertAddressInputSet()

    def _make_result_set(self, result, path):
        return InsertAddressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return InsertAddressChoreographyExecution(session, exec_id, path)

class InsertAddressInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the InsertAddress
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AddressResource(self, value):
        """
        Set the value of the AddressResource input for this Choreo. ((optional, json) A JSON string containing the address resource properties you wish to set. This can be used as an alternative to individual inputs that represent address resource properties.)
        """
        super(InsertAddressInputSet, self)._set_input('AddressResource', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        super(InsertAddressInputSet, self)._set_input('AccessToken', value)
    def set_Address(self, value):
        """
        Set the value of the Address input for this Choreo. ((optional, string) The IP address represented by this resource.)
        """
        super(InsertAddressInputSet, self)._set_input('Address', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        super(InsertAddressInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        super(InsertAddressInputSet, self)._set_input('ClientSecret', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) A description of the address.)
        """
        super(InsertAddressInputSet, self)._set_input('Description', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((conditional, string) The name of the address resource.)
        """
        super(InsertAddressInputSet, self)._set_input('Name', value)
    def set_Project(self, value):
        """
        Set the value of the Project input for this Choreo. ((required, string) The ID of a Google Compute project.)
        """
        super(InsertAddressInputSet, self)._set_input('Project', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(InsertAddressInputSet, self)._set_input('RefreshToken', value)
    def set_Region(self, value):
        """
        Set the value of the Region input for this Choreo. ((required, string) Name of the region associated with the request.)
        """
        super(InsertAddressInputSet, self)._set_input('Region', value)

class InsertAddressResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the InsertAddress Choreo.
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

class InsertAddressChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return InsertAddressResultSet(response, path)
