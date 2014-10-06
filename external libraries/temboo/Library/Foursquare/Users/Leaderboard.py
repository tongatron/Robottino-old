# -*- coding: utf-8 -*-

###############################################################################
#
# Leaderboard
# Return the user's Leaderboard
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

class Leaderboard(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Leaderboard Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Leaderboard, self).__init__(temboo_session, '/Library/Foursquare/Users/Leaderboard')


    def new_input_set(self):
        return LeaderboardInputSet()

    def _make_result_set(self, result, path):
        return LeaderboardResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LeaderboardChoreographyExecution(session, exec_id, path)

class LeaderboardInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Leaderboard
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Neighbors(self, value):
        """
        Set the value of the Neighbors input for this Choreo. ((optional, integer) The number of friends' scores to return that are adjacent to your score, in ranked order.)
        """
        super(LeaderboardInputSet, self)._set_input('Neighbors', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The Foursquare API OAuth token string.)
        """
        super(LeaderboardInputSet, self)._set_input('OauthToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(LeaderboardInputSet, self)._set_input('ResponseFormat', value)

class LeaderboardResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Leaderboard Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class LeaderboardChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return LeaderboardResultSet(response, path)
