# -*- coding: utf-8 -*-

###############################################################################
#
# GetRecommendations
# Retrieves a list of catalog title recommendations for a subscriber.
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

class GetRecommendations(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetRecommendations Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetRecommendations, self).__init__(temboo_session, '/Library/Netflix/GetRecommendations')


    def new_input_set(self):
        return GetRecommendationsInputSet()

    def _make_result_set(self, result, path):
        return GetRecommendationsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRecommendationsChoreographyExecution(session, exec_id, path)

class GetRecommendationsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetRecommendations
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Netflix (AKA the OAuth Consumer Key).)
        """
        super(GetRecommendationsInputSet, self)._set_input('APIKey', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(GetRecommendationsInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(GetRecommendationsInputSet, self)._set_input('AccessToken', value)
    def set_MaxResults(self, value):
        """
        Set the value of the MaxResults input for this Choreo. ((optional, integer) Set this to the maximum number of results to return. This number cannot be greater than 500. If you do not specify max_results, the default value is 25)
        """
        super(GetRecommendationsInputSet, self)._set_input('MaxResults', value)
    def set_SharedSecret(self, value):
        """
        Set the value of the SharedSecret input for this Choreo. ((required, string) The Shared Secret provided by Netflix (AKA the OAuth Consumer Secret).)
        """
        super(GetRecommendationsInputSet, self)._set_input('SharedSecret', value)
    def set_StartIndex(self, value):
        """
        Set the value of the StartIndex input for this Choreo. ((optional, integer) The offset number of the results from the query.)
        """
        super(GetRecommendationsInputSet, self)._set_input('StartIndex', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((required, string) The ID associated with the user whose recommendations you want to retrieve.)
        """
        super(GetRecommendationsInputSet, self)._set_input('UserID', value)

class GetRecommendationsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetRecommendations Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Netflix.)
        """
        return self._output.get('Response', None)

class GetRecommendationsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetRecommendationsResultSet(response, path)
