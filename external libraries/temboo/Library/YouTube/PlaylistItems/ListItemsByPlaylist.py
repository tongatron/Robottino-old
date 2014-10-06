# -*- coding: utf-8 -*-

###############################################################################
#
# ListItemsByPlaylist
# Returns a collection of playlist items within a specific playlist.
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

class ListItemsByPlaylist(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListItemsByPlaylist Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListItemsByPlaylist, self).__init__(temboo_session, '/Library/YouTube/PlaylistItems/ListItemsByPlaylist')


    def new_input_set(self):
        return ListItemsByPlaylistInputSet()

    def _make_result_set(self, result, path):
        return ListItemsByPlaylistResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListItemsByPlaylistChoreographyExecution(session, exec_id, path)

class ListItemsByPlaylistInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListItemsByPlaylist
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) The API Key provided by Google for simple API access when you do not need to access user data.)
        """
        super(ListItemsByPlaylistInputSet, self)._set_input('APIKey', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required for OAuth authentication unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        super(ListItemsByPlaylistInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        super(ListItemsByPlaylistInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        super(ListItemsByPlaylistInputSet, self)._set_input('ClientSecret', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) Allows you to specify a subset of fields to include in the response using an xpath-like syntax (i.e. items/snippet/title).)
        """
        super(ListItemsByPlaylistInputSet, self)._set_input('Fields', value)
    def set_MaxResults(self, value):
        """
        Set the value of the MaxResults input for this Choreo. ((optional, integer) The maximum number of results to return.)
        """
        super(ListItemsByPlaylistInputSet, self)._set_input('MaxResults', value)
    def set_PageToken(self, value):
        """
        Set the value of the PageToken input for this Choreo. ((optional, string) The "nextPageToken" found in the response which is used to page through results.)
        """
        super(ListItemsByPlaylistInputSet, self)._set_input('PageToken', value)
    def set_Part(self, value):
        """
        Set the value of the Part input for this Choreo. ((optional, string) Specifies a comma-separated list of playlistItem resource properties that the API response will include. Part names that you can pass are: id, snippet, and contentDetails.)
        """
        super(ListItemsByPlaylistInputSet, self)._set_input('Part', value)
    def set_PlaylistID(self, value):
        """
        Set the value of the PlaylistID input for this Choreo. ((conditional, string) A unique ID of the playlist for which you want to retrieve playlist items.)
        """
        super(ListItemsByPlaylistInputSet, self)._set_input('PlaylistID', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        super(ListItemsByPlaylistInputSet, self)._set_input('RefreshToken', value)
    def set_VideoID(self, value):
        """
        Set the value of the VideoID input for this Choreo. ((optional, string) Indicates that only the playlist items that contain the specified video should be returned.)
        """
        super(ListItemsByPlaylistInputSet, self)._set_input('VideoID', value)

class ListItemsByPlaylistResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListItemsByPlaylist Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from YouTube.)
        """
        return self._output.get('Response', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)

class ListItemsByPlaylistChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListItemsByPlaylistResultSet(response, path)
