# -*- coding: utf-8 -*-

###############################################################################
#
# GetSuggestedUsers
# Retrieves users in a given category of the Twitter suggested user list.
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

class GetSuggestedUsers(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetSuggestedUsers Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetSuggestedUsers, self).__init__(temboo_session, '/Library/Twitter/SuggestedUsers/GetSuggestedUsers')


    def new_input_set(self):
        return GetSuggestedUsersInputSet()

    def _make_result_set(self, result, path):
        return GetSuggestedUsersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetSuggestedUsersChoreographyExecution(session, exec_id, path)

class GetSuggestedUsersInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetSuggestedUsers
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret provided by Twitter or retrieved during the OAuth process.)
        """
        super(GetSuggestedUsersInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token provided by Twitter or retrieved during the OAuth process.)
        """
        super(GetSuggestedUsersInputSet, self)._set_input('AccessToken', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Twitter.)
        """
        super(GetSuggestedUsersInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Twitter.)
        """
        super(GetSuggestedUsersInputSet, self)._set_input('ConsumerSecret', value)
    def set_Language(self, value):
        """
        Set the value of the Language input for this Choreo. ((optional, string) Restricts the suggested categories to the requested language. The language must be specified by the appropriate two letter ISO 639-1 code (e.g., en).)
        """
        super(GetSuggestedUsersInputSet, self)._set_input('Language', value)
    def set_Members(self, value):
        """
        Set the value of the Members input for this Choreo. ((optional, boolean) When set to true, makes a request to users/suggestions/:slug/members and retrieves the most recent statuses for users that are not protected.)
        """
        super(GetSuggestedUsersInputSet, self)._set_input('Members', value)
    def set_Slug(self, value):
        """
        Set the value of the Slug input for this Choreo. ((required, string) The short name of  the category (e.g., news, technology, government). These are returned in the response of the GetSuggestedCategories Choreo.)
        """
        super(GetSuggestedUsersInputSet, self)._set_input('Slug', value)

class GetSuggestedUsersResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetSuggestedUsers Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Twitter.)
        """
        return self._output.get('Response', None)
    def get_Limit(self):
        """
        Retrieve the value for the "Limit" output from this Choreo execution. ((integer) The rate limit ceiling for this particular request.)
        """
        return self._output.get('Limit', None)
    def get_Remaining(self):
        """
        Retrieve the value for the "Remaining" output from this Choreo execution. ((integer) The number of requests left for the 15 minute window.)
        """
        return self._output.get('Remaining', None)
    def get_Reset(self):
        """
        Retrieve the value for the "Reset" output from this Choreo execution. ((date) The remaining window before the rate limit resets in UTC epoch seconds.)
        """
        return self._output.get('Reset', None)

class GetSuggestedUsersChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetSuggestedUsersResultSet(response, path)
