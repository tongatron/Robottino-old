# -*- coding: utf-8 -*-

###############################################################################
#
# UserFollows
# Retrieve the list of users that the authenticating user is following.
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

class UserFollows(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UserFollows Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UserFollows, self).__init__(temboo_session, '/Library/Instagram/UserFollows')


    def new_input_set(self):
        return UserFollowsInputSet()

    def _make_result_set(self, result, path):
        return UserFollowsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UserFollowsChoreographyExecution(session, exec_id, path)

class UserFollowsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UserFollows
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((conditional, string) The access token retrieved during the OAuth 2.0 process. Required unless you provide the ClientID.)
        """
        super(UserFollowsInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Instagram after registering your application. Required unless you provide the AccessToken.)
        """
        super(UserFollowsInputSet, self)._set_input('ClientID', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((required, string) The ID of the user associated with the list to return. Defaults to 'self' indicating that the authenticating user is assumed.)
        """
        super(UserFollowsInputSet, self)._set_input('UserID', value)

class UserFollowsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UserFollows Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Instagram.)
        """
        return self._output.get('Response', None)

class UserFollowsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UserFollowsResultSet(response, path)
