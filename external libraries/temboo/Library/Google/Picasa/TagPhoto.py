# -*- coding: utf-8 -*-

###############################################################################
#
# TagPhoto
# Creates a tag for a specified photo in Google Picasa.
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

class TagPhoto(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the TagPhoto Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(TagPhoto, self).__init__(temboo_session, '/Library/Google/Picasa/TagPhoto')


    def new_input_set(self):
        return TagPhotoInputSet()

    def _make_result_set(self, result, path):
        return TagPhotoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TagPhotoChoreographyExecution(session, exec_id, path)

class TagPhotoInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the TagPhoto
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        super(TagPhotoInputSet, self)._set_input('AccessToken', value)
    def set_AlbumID(self, value):
        """
        Set the value of the AlbumID input for this Choreo. ((required, integer) The id of the album which contains the photo you want to tag.)
        """
        super(TagPhotoInputSet, self)._set_input('AlbumID', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        super(TagPhotoInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        super(TagPhotoInputSet, self)._set_input('ClientSecret', value)
    def set_PhotoID(self, value):
        """
        Set the value of the PhotoID input for this Choreo. ((required, integer) The id of the photo you want to tag.)
        """
        super(TagPhotoInputSet, self)._set_input('PhotoID', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth Refresh Token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(TagPhotoInputSet, self)._set_input('RefreshToken', value)
    def set_Tag(self, value):
        """
        Set the value of the Tag input for this Choreo. ((required, string) The text for the photo tag.)
        """
        super(TagPhotoInputSet, self)._set_input('Tag', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) Google Picasa username. Defaults to "default" which means the server will use the UserID of the user whose access token was specified.)
        """
        super(TagPhotoInputSet, self)._set_input('UserID', value)

class TagPhotoResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the TagPhoto Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Google Picasa.)
        """
        return self._output.get('Response', None)
    def get_AccessToken(self):
        """
        Retrieve the value for the "AccessToken" output from this Choreo execution. ((optional, string) A valid access token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        return self._output.get('AccessToken', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)

class TagPhotoChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return TagPhotoResultSet(response, path)
