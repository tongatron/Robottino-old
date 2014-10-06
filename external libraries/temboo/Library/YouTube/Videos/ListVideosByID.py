# -*- coding: utf-8 -*-

###############################################################################
#
# ListVideosByID
# Returns a list of YouTube videos that match the IDs provided.
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

class ListVideosByID(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListVideosByID Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListVideosByID, self).__init__(temboo_session, '/Library/YouTube/Videos/ListVideosByID')


    def new_input_set(self):
        return ListVideosByIDInputSet()

    def _make_result_set(self, result, path):
        return ListVideosByIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListVideosByIDChoreographyExecution(session, exec_id, path)

class ListVideosByIDInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListVideosByID
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) The API Key provided by Google for simple API access when you do not need to access user data.)
        """
        super(ListVideosByIDInputSet, self)._set_input('APIKey', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required for OAuth authentication unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        super(ListVideosByIDInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        super(ListVideosByIDInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        super(ListVideosByIDInputSet, self)._set_input('ClientSecret', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) Allows you to specify a subset of fields to include in the response using an xpath-like syntax (i.e. items/snippet/title).)
        """
        super(ListVideosByIDInputSet, self)._set_input('Fields', value)
    def set_Part(self, value):
        """
        Set the value of the Part input for this Choreo. ((optional, string) A comma-separated list of fields to include. Valid values are: id, snippet, contentDetails, fileDetails, player, processingDetails, recordingDetails, statistics, status, suggestions, and topicDetails.)
        """
        super(ListVideosByIDInputSet, self)._set_input('Part', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        super(ListVideosByIDInputSet, self)._set_input('RefreshToken', value)
    def set_VideoID(self, value):
        """
        Set the value of the VideoID input for this Choreo. ((required, string) A comma-separated list of the YouTube video ID(s) that are being retrieved.)
        """
        super(ListVideosByIDInputSet, self)._set_input('VideoID', value)

class ListVideosByIDResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListVideosByID Choreo.
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

class ListVideosByIDChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListVideosByIDResultSet(response, path)
