# -*- coding: utf-8 -*-

###############################################################################
#
# SetTags
# Sets tags for the specified instance.
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

class SetTags(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SetTags Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SetTags, self).__init__(temboo_session, '/Library/Google/ComputeEngine/Instances/SetTags')


    def new_input_set(self):
        return SetTagsInputSet()

    def _make_result_set(self, result, path):
        return SetTagsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SetTagsChoreographyExecution(session, exec_id, path)

class SetTagsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SetTags
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        super(SetTagsInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        super(SetTagsInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        super(SetTagsInputSet, self)._set_input('ClientSecret', value)
    def set_Fingerprint(self, value):
        """
        Set the value of the Fingerprint input for this Choreo. ((required, string) The current fingerprint of this resource. You must provide the current version of the fingerprint to successfully update tags.)
        """
        super(SetTagsInputSet, self)._set_input('Fingerprint', value)
    def set_Instance(self, value):
        """
        Set the value of the Instance input for this Choreo. ((required, string) The name of the instance that you're setting tags for.)
        """
        super(SetTagsInputSet, self)._set_input('Instance', value)
    def set_Items(self, value):
        """
        Set the value of the Items input for this Choreo. ((required, json) An array of tags. The max length of a tag is 63 characters.)
        """
        super(SetTagsInputSet, self)._set_input('Items', value)
    def set_Project(self, value):
        """
        Set the value of the Project input for this Choreo. ((required, string) The ID of a Google Compute project.)
        """
        super(SetTagsInputSet, self)._set_input('Project', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(SetTagsInputSet, self)._set_input('RefreshToken', value)
    def set_Zone(self, value):
        """
        Set the value of the Zone input for this Choreo. ((required, string) The name of the zone associated with this request.)
        """
        super(SetTagsInputSet, self)._set_input('Zone', value)

class SetTagsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SetTags Choreo.
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

class SetTagsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SetTagsResultSet(response, path)
