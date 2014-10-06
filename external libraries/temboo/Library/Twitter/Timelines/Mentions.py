# -*- coding: utf-8 -*-

###############################################################################
#
# Mentions
# Retrieves the 20 most recent mentions for the authenticating user.
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

class Mentions(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Mentions Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Mentions, self).__init__(temboo_session, '/Library/Twitter/Timelines/Mentions')


    def new_input_set(self):
        return MentionsInputSet()

    def _make_result_set(self, result, path):
        return MentionsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MentionsChoreographyExecution(session, exec_id, path)

class MentionsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Mentions
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret provided by Twitter or retrieved during the OAuth process.n)
        """
        super(MentionsInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token provided by Twitter or retrieved during the OAuth process.)
        """
        super(MentionsInputSet, self)._set_input('AccessToken', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Twitter.)
        """
        super(MentionsInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Twitter.)
        """
        super(MentionsInputSet, self)._set_input('ConsumerSecret', value)
    def set_ContributorDetails(self, value):
        """
        Set the value of the ContributorDetails input for this Choreo. ((optional, boolean) Set to true to include the screen_name of the contributor. By default only the user_id of the contributor is included.)
        """
        super(MentionsInputSet, self)._set_input('ContributorDetails', value)
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) Specifies the number of tweets to retrieve. Must be less than or equal to 200. Defaults to 20.)
        """
        super(MentionsInputSet, self)._set_input('Count', value)
    def set_IncludeEntities(self, value):
        """
        Set the value of the IncludeEntities input for this Choreo. ((optional, boolean) The "entities" node containing extra metadata will not be included when set to false.)
        """
        super(MentionsInputSet, self)._set_input('IncludeEntities', value)
    def set_MaxId(self, value):
        """
        Set the value of the MaxId input for this Choreo. ((optional, string) Returns results with an ID less than (older than) or equal to the specified ID.)
        """
        super(MentionsInputSet, self)._set_input('MaxId', value)
    def set_SinceId(self, value):
        """
        Set the value of the SinceId input for this Choreo. ((optional, string) Returns results with an ID greater than (more recent than) the specified ID.)
        """
        super(MentionsInputSet, self)._set_input('SinceId', value)
    def set_TrimUser(self, value):
        """
        Set the value of the TrimUser input for this Choreo. ((optional, boolean) When set to true, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Defaults to false, which returns the complete user object.)
        """
        super(MentionsInputSet, self)._set_input('TrimUser', value)

class MentionsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Mentions Choreo.
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

class MentionsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return MentionsResultSet(response, path)
