# -*- coding: utf-8 -*-

###############################################################################
#
# AddToFavorites
# Adds a photo to a user's favorites list.
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

class AddToFavorites(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddToFavorites Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(AddToFavorites, self).__init__(temboo_session, '/Library/Flickr/Favorites/AddToFavorites')


    def new_input_set(self):
        return AddToFavoritesInputSet()

    def _make_result_set(self, result, path):
        return AddToFavoritesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddToFavoritesChoreographyExecution(session, exec_id, path)

class AddToFavoritesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddToFavorites
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        super(AddToFavoritesInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) The API Secret provided by Flickr (AKA the OAuth Consumer Secret).)
        """
        super(AddToFavoritesInputSet, self)._set_input('APISecret', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(AddToFavoritesInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(AddToFavoritesInputSet, self)._set_input('AccessToken', value)
    def set_PhotoID(self, value):
        """
        Set the value of the PhotoID input for this Choreo. ((required, integer) The id of the photo to add a favorites list.)
        """
        super(AddToFavoritesInputSet, self)._set_input('PhotoID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml and json. Defaults to json.)
        """
        super(AddToFavoritesInputSet, self)._set_input('ResponseFormat', value)

class AddToFavoritesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddToFavorites Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Flickr.)
        """
        return self._output.get('Response', None)

class AddToFavoritesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AddToFavoritesResultSet(response, path)
