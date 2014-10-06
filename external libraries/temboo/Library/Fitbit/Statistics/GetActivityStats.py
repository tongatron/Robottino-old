# -*- coding: utf-8 -*-

###############################################################################
#
# GetActivityStats
# Gets user's activity statistics.
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

class GetActivityStats(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetActivityStats Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetActivityStats, self).__init__(temboo_session, '/Library/Fitbit/Statistics/GetActivityStats')


    def new_input_set(self):
        return GetActivityStatsInputSet()

    def _make_result_set(self, result, path):
        return GetActivityStatsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetActivityStatsChoreographyExecution(session, exec_id, path)

class GetActivityStatsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetActivityStats
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(GetActivityStatsInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(GetActivityStatsInputSet, self)._set_input('AccessToken', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Fitbit.)
        """
        super(GetActivityStatsInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Fitbit.)
        """
        super(GetActivityStatsInputSet, self)._set_input('ConsumerSecret', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in: xml or json. Defaults to json.)
        """
        super(GetActivityStatsInputSet, self)._set_input('ResponseFormat', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) The user's encoded id. Defaults to "-" (dash) which will return data for the user associated with the token credentials provided.)
        """
        super(GetActivityStatsInputSet, self)._set_input('UserID', value)

class GetActivityStatsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetActivityStats Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Fitbit.)
        """
        return self._output.get('Response', None)

class GetActivityStatsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetActivityStatsResultSet(response, path)
