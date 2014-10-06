# -*- coding: utf-8 -*-

###############################################################################
#
# UserTimeline
# Retrieves a collection of the most recent Tweets posted by the user whose screen_name or user_id is indicated.
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

class UserTimeline(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UserTimeline Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UserTimeline, self).__init__(temboo_session, '/Library/Twitter/Timelines/UserTimeline')


    def new_input_set(self):
        return UserTimelineInputSet()

    def _make_result_set(self, result, path):
        return UserTimelineResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UserTimelineChoreographyExecution(session, exec_id, path)

class UserTimelineInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UserTimeline
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((conditional, string) The Access Token Secret provided by Twitter or retrieved during the OAuth process.)
        """
        super(UserTimelineInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((conditional, string) The Access Token provided by Twitter or retrieved during the OAuth process.)
        """
        super(UserTimelineInputSet, self)._set_input('AccessToken', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((conditional, string) The Consumer Key provided by Twitter.)
        """
        super(UserTimelineInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((conditional, string) The Consumer Secret provided by Twitter.)
        """
        super(UserTimelineInputSet, self)._set_input('ConsumerSecret', value)
    def set_ContributorDetails(self, value):
        """
        Set the value of the ContributorDetails input for this Choreo. ((optional, boolean) Set to true to include the screen_name of the contributor. By default only the user_id of the contributor is included.)
        """
        super(UserTimelineInputSet, self)._set_input('ContributorDetails', value)
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) Specifies the number of records to retrieve. Must be less than or equal to 200. Defaults to 20.)
        """
        super(UserTimelineInputSet, self)._set_input('Count', value)
    def set_ExcludeReplies(self, value):
        """
        Set the value of the ExcludeReplies input for this Choreo. ((optional, boolean) Set to true to prevent replies from appearing in the returned timeline.)
        """
        super(UserTimelineInputSet, self)._set_input('ExcludeReplies', value)
    def set_IncludeRetweets(self, value):
        """
        Set the value of the IncludeRetweets input for this Choreo. ((optional, boolean) When set to true, the response will include the "entities" node.)
        """
        super(UserTimelineInputSet, self)._set_input('IncludeRetweets', value)
    def set_MaxId(self, value):
        """
        Set the value of the MaxId input for this Choreo. ((optional, string) Returns results with an ID less than (older than) or equal to the specified ID.)
        """
        super(UserTimelineInputSet, self)._set_input('MaxId', value)
    def set_ScreenName(self, value):
        """
        Set the value of the ScreenName input for this Choreo. ((conditional, string) Screen name of the user to return results for. Required unless providing the UserId.)
        """
        super(UserTimelineInputSet, self)._set_input('ScreenName', value)
    def set_SinceId(self, value):
        """
        Set the value of the SinceId input for this Choreo. ((optional, string) Returns results with an ID greater than (more recent than) the specified ID.)
        """
        super(UserTimelineInputSet, self)._set_input('SinceId', value)
    def set_TrimUser(self, value):
        """
        Set the value of the TrimUser input for this Choreo. ((optional, boolean) When set to true, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Defaults to false.)
        """
        super(UserTimelineInputSet, self)._set_input('TrimUser', value)
    def set_UserId(self, value):
        """
        Set the value of the UserId input for this Choreo. ((conditional, string) ID of the user to return results for. Required unless providing the ScreenName.)
        """
        super(UserTimelineInputSet, self)._set_input('UserId', value)

class UserTimelineResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UserTimeline Choreo.
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

class UserTimelineChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UserTimelineResultSet(response, path)
