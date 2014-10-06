# -*- coding: utf-8 -*-

###############################################################################
#
# SetCommonInstanceMetadata
# Sets metadata common to all instances within the specified Project.
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

class SetCommonInstanceMetadata(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SetCommonInstanceMetadata Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SetCommonInstanceMetadata, self).__init__(temboo_session, '/Library/Google/ComputeEngine/Projects/SetCommonInstanceMetadata')


    def new_input_set(self):
        return SetCommonInstanceMetadataInputSet()

    def _make_result_set(self, result, path):
        return SetCommonInstanceMetadataResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SetCommonInstanceMetadataChoreographyExecution(session, exec_id, path)

class SetCommonInstanceMetadataInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SetCommonInstanceMetadata
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        super(SetCommonInstanceMetadataInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        super(SetCommonInstanceMetadataInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        super(SetCommonInstanceMetadataInputSet, self)._set_input('ClientSecret', value)
    def set_Fingerprint(self, value):
        """
        Set the value of the Fingerprint input for this Choreo. ((required, string) The fingerprint of this resource, which is a hash of the metadata's contents. This field is used for optimistic locking. Providing an up-to-date metadata fingerprint is required to modify metadata.)
        """
        super(SetCommonInstanceMetadataInputSet, self)._set_input('Fingerprint', value)
    def set_Items(self, value):
        """
        Set the value of the Items input for this Choreo. ((conditional, json) An array of key/value pairs. The max size of all keys and values is 512 KB.)
        """
        super(SetCommonInstanceMetadataInputSet, self)._set_input('Items', value)
    def set_Project(self, value):
        """
        Set the value of the Project input for this Choreo. ((required, string) The ID of a Google Compute project.)
        """
        super(SetCommonInstanceMetadataInputSet, self)._set_input('Project', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(SetCommonInstanceMetadataInputSet, self)._set_input('RefreshToken', value)

class SetCommonInstanceMetadataResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SetCommonInstanceMetadata Choreo.
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

class SetCommonInstanceMetadataChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SetCommonInstanceMetadataResultSet(response, path)
