# -*- coding: utf-8 -*-

###############################################################################
#
# GetRecordByExternalID
# Retrieve records with a specific external ID.
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

class GetRecordByExternalID(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetRecordByExternalID Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetRecordByExternalID, self).__init__(temboo_session, '/Library/Salesforce/Objects/GetRecordByExternalID')


    def new_input_set(self):
        return GetRecordByExternalIDInputSet()

    def _make_result_set(self, result, path):
        return GetRecordByExternalIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRecordByExternalIDChoreographyExecution(session, exec_id, path)

class GetRecordByExternalIDInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetRecordByExternalID
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        super(GetRecordByExternalIDInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Salesforce. Required unless providing a valid AccessToken.)
        """
        super(GetRecordByExternalIDInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Salesforce. Required unless providing a valid AccessToken.)
        """
        super(GetRecordByExternalIDInputSet, self)._set_input('ClientSecret', value)
    def set_FieldName(self, value):
        """
        Set the value of the FieldName input for this Choreo. ((conditional, string) FieldName for external ID)
        """
        super(GetRecordByExternalIDInputSet, self)._set_input('FieldName', value)
    def set_FieldValue(self, value):
        """
        Set the value of the FieldValue input for this Choreo. ((conditional, string) Field value for external ID)
        """
        super(GetRecordByExternalIDInputSet, self)._set_input('FieldValue', value)
    def set_InstanceName(self, value):
        """
        Set the value of the InstanceName input for this Choreo. ((required, string) The server url prefix that indicates which instance your Salesforce account is on (e.g. na1, na2, na3, etc).)
        """
        super(GetRecordByExternalIDInputSet, self)._set_input('InstanceName', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth Refresh Token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(GetRecordByExternalIDInputSet, self)._set_input('RefreshToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetRecordByExternalIDInputSet, self)._set_input('ResponseFormat', value)
    def set_SObjectName(self, value):
        """
        Set the value of the SObjectName input for this Choreo. ((conditional, string) The name of the Salesforce object type being created (e.g. Account, Contact, Lead, etc).)
        """
        super(GetRecordByExternalIDInputSet, self)._set_input('SObjectName', value)

class GetRecordByExternalIDResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetRecordByExternalID Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Salesforce.)
        """
        return self._output.get('Response', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)

class GetRecordByExternalIDChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetRecordByExternalIDResultSet(response, path)
