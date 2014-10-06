# -*- coding: utf-8 -*-

###############################################################################
#
# CreateFavorite
# Marks a specified status as a favorite.
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

class CreateFavorite(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateFavorite Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateFavorite, self).__init__(temboo_session, '/Library/Twitter/Favorites/CreateFavorite')


    def new_input_set(self):
        return CreateFavoriteInputSet()

    def _make_result_set(self, result, path):
        return CreateFavoriteResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateFavoriteChoreographyExecution(session, exec_id, path)

class CreateFavoriteInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateFavorite
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret provided by Twitter or retrieved during the OAuth process.)
        """
        super(CreateFavoriteInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token provided by Twitter or retrieved during the OAuth process.)
        """
        super(CreateFavoriteInputSet, self)._set_input('AccessToken', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Twitter.)
        """
        super(CreateFavoriteInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Twitter.)
        """
        super(CreateFavoriteInputSet, self)._set_input('ConsumerSecret', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((required, string) The ID of the status to favorite.)
        """
        super(CreateFavoriteInputSet, self)._set_input('ID', value)
    def set_IncludeEntities(self, value):
        """
        Set the value of the IncludeEntities input for this Choreo. ((optional, boolean) The "entities" node containing extra metadata will not be included when set to false.)
        """
        super(CreateFavoriteInputSet, self)._set_input('IncludeEntities', value)

class CreateFavoriteResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateFavorite Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Twitter.)
        """
        return self._output.get('Response', None)

class CreateFavoriteChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateFavoriteResultSet(response, path)
