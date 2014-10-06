# -*- coding: utf-8 -*-

###############################################################################
#
# GetUserFeed
# Retrieves the authenticated user's feed.
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

class GetUserFeed(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetUserFeed Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetUserFeed, self).__init__(temboo_session, '/Library/Instagram/GetUserFeed')


    def new_input_set(self):
        return GetUserFeedInputSet()

    def _make_result_set(self, result, path):
        return GetUserFeedResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetUserFeedChoreographyExecution(session, exec_id, path)

class GetUserFeedInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetUserFeed
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth 2.0 process.)
        """
        super(GetUserFeedInputSet, self)._set_input('AccessToken', value)
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) The number of results to return.)
        """
        super(GetUserFeedInputSet, self)._set_input('Count', value)
    def set_MaxID(self, value):
        """
        Set the value of the MaxID input for this Choreo. ((optional, string) Returns media earlier than this max_id.)
        """
        super(GetUserFeedInputSet, self)._set_input('MaxID', value)
    def set_MinID(self, value):
        """
        Set the value of the MinID input for this Choreo. ((optional, string) Returns media later than this min_id.)
        """
        super(GetUserFeedInputSet, self)._set_input('MinID', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) The ID of the user whose feed to retrieve. Defaults to 'self' indicating that the authenticating user is assumed.)
        """
        super(GetUserFeedInputSet, self)._set_input('UserID', value)

class GetUserFeedResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetUserFeed Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Instagram.)
        """
        return self._output.get('Response', None)

class GetUserFeedChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetUserFeedResultSet(response, path)
