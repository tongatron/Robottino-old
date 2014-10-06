# -*- coding: utf-8 -*-

###############################################################################
#
# DeletePlaylist
# Deletes a given playlist action.
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

class DeletePlaylist(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeletePlaylist Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeletePlaylist, self).__init__(temboo_session, '/Library/Facebook/Actions/Music/Playlists/DeletePlaylist')


    def new_input_set(self):
        return DeletePlaylistInputSet()

    def _make_result_set(self, result, path):
        return DeletePlaylistResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeletePlaylistChoreographyExecution(session, exec_id, path)

class DeletePlaylistInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeletePlaylist
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        super(DeletePlaylistInputSet, self)._set_input('AccessToken', value)
    def set_ActionID(self, value):
        """
        Set the value of the ActionID input for this Choreo. ((required, string) The id of an action to delete.)
        """
        super(DeletePlaylistInputSet, self)._set_input('ActionID', value)

class DeletePlaylistResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeletePlaylist Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((boolean) The response from Facebook. Returns "true" on success.)
        """
        return self._output.get('Response', None)

class DeletePlaylistChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeletePlaylistResultSet(response, path)
