# -*- coding: utf-8 -*-

###############################################################################
#
# UserDetail
# Returns profile information for a given user.
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

class UserDetail(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UserDetail Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UserDetail, self).__init__(temboo_session, '/Library/Foursquare/Users/UserDetail')


    def new_input_set(self):
        return UserDetailInputSet()

    def _make_result_set(self, result, path):
        return UserDetailResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UserDetailChoreographyExecution(session, exec_id, path)

class UserDetailInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UserDetail
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The Foursquare API Oauth token string.)
        """
        super(UserDetailInputSet, self)._set_input('OauthToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(UserDetailInputSet, self)._set_input('ResponseFormat', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) The ID of the user to get details for. Pass "self" to get details of the acting user. Defaults to "self".)
        """
        super(UserDetailInputSet, self)._set_input('UserID', value)


class UserDetailResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UserDetail Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class UserDetailChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UserDetailResultSet(response, path)
