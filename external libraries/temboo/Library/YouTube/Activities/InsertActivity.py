# -*- coding: utf-8 -*-

###############################################################################
#
# InsertActivity
# Posts a bulletin for a specific channel.
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

class InsertActivity(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the InsertActivity Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(InsertActivity, self).__init__(temboo_session, '/Library/YouTube/Activities/InsertActivity')


    def new_input_set(self):
        return InsertActivityInputSet()

    def _make_result_set(self, result, path):
        return InsertActivityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return InsertActivityChoreographyExecution(session, exec_id, path)

class InsertActivityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the InsertActivity
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ActivityMetadata(self, value):
        """
        Set the value of the ActivityMetadata input for this Choreo. ((required, json) A JSON representation of the activity resource to create. See documentation for examples.)
        """
        super(InsertActivityInputSet, self)._set_input('ActivityMetadata', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required for OAuth authentication unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        super(InsertActivityInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        super(InsertActivityInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        super(InsertActivityInputSet, self)._set_input('ClientSecret', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) Allows you to specify a subset of fields to include in the response using an xpath-like syntax (i.e. items/snippet/title).)
        """
        super(InsertActivityInputSet, self)._set_input('Fields', value)
    def set_Part(self, value):
        """
        Set the value of the Part input for this Choreo. ((optional, string) A comma-separated list of fields that are being set and that will be returned in the response. Part names that can be passed are: snippet and contentDetails.)
        """
        super(InsertActivityInputSet, self)._set_input('Part', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        super(InsertActivityInputSet, self)._set_input('RefreshToken', value)

class InsertActivityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the InsertActivity Choreo.
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

class InsertActivityChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return InsertActivityResultSet(response, path)
