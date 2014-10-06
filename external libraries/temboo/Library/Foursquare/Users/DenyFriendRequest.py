# -*- coding: utf-8 -*-

###############################################################################
#
# DenyFriendRequest
# Denies a pending friend request from another user.
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

class DenyFriendRequest(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DenyFriendRequest Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DenyFriendRequest, self).__init__(temboo_session, '/Library/Foursquare/Users/DenyFriendRequest')


    def new_input_set(self):
        return DenyFriendRequestInputSet()

    def _make_result_set(self, result, path):
        return DenyFriendRequestResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DenyFriendRequestChoreographyExecution(session, exec_id, path)

class DenyFriendRequestInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DenyFriendRequest
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The Foursquare API OAuth token string.)
        """
        super(DenyFriendRequestInputSet, self)._set_input('OauthToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(DenyFriendRequestInputSet, self)._set_input('ResponseFormat', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((required, string) The user ID of a pending friend.)
        """
        super(DenyFriendRequestInputSet, self)._set_input('UserID', value)

class DenyFriendRequestResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DenyFriendRequest Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class DenyFriendRequestChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DenyFriendRequestResultSet(response, path)
