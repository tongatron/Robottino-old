# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteVideo
# Deletes a YouTube video.
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

class DeleteVideo(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteVideo Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteVideo, self).__init__(temboo_session, '/Library/YouTube/Videos/DeleteVideo')


    def new_input_set(self):
        return DeleteVideoInputSet()

    def _make_result_set(self, result, path):
        return DeleteVideoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteVideoChoreographyExecution(session, exec_id, path)

class DeleteVideoInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteVideo
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required for OAuth authentication unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        super(DeleteVideoInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        super(DeleteVideoInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        super(DeleteVideoInputSet, self)._set_input('ClientSecret', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        super(DeleteVideoInputSet, self)._set_input('RefreshToken', value)
    def set_VideoID(self, value):
        """
        Set the value of the VideoID input for this Choreo. ((required, string) The id of the video to delete.)
        """
        super(DeleteVideoInputSet, self)._set_input('VideoID', value)

class DeleteVideoResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteVideo Choreo.
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

class DeleteVideoChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteVideoResultSet(response, path)
