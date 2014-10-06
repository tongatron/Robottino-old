# -*- coding: utf-8 -*-

###############################################################################
#
# Like
# Allows the authenticated user to like or unlike a check-in.
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

class Like(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Like Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Like, self).__init__(temboo_session, '/Library/Foursquare/Checkins/Like')


    def new_input_set(self):
        return LikeInputSet()

    def _make_result_set(self, result, path):
        return LikeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LikeChoreographyExecution(session, exec_id, path)

class LikeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Like
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CheckinID(self, value):
        """
        Set the value of the CheckinID input for this Choreo. ((required, string) The ID of the check-in to like or unlike.)
        """
        super(LikeInputSet, self)._set_input('CheckinID', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The Foursquare API OAuth token string.)
        """
        super(LikeInputSet, self)._set_input('OauthToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(LikeInputSet, self)._set_input('ResponseFormat', value)
    def set_Set(self, value):
        """
        Set the value of the Set input for this Choreo. ((optional, boolean) Set to 1 (the default) to like this check-in. Set to 0 to undo a previous like.)
        """
        super(LikeInputSet, self)._set_input('Set', value)

class LikeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Like Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class LikeChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return LikeResultSet(response, path)
