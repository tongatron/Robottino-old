# -*- coding: utf-8 -*-

###############################################################################
#
# FriendRequests
# Retrieves a list of friend requests for a specified user.
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

class FriendRequests(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FriendRequests Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(FriendRequests, self).__init__(temboo_session, '/Library/Facebook/Reading/FriendRequests')


    def new_input_set(self):
        return FriendRequestsInputSet()

    def _make_result_set(self, result, path):
        return FriendRequestsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FriendRequestsChoreographyExecution(session, exec_id, path)

class FriendRequestsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FriendRequests
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        super(FriendRequestsInputSet, self)._set_input('AccessToken', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma separated list of fields to return (i.e. id,name).)
        """
        super(FriendRequestsInputSet, self)._set_input('Fields', value)
    def set_Limt(self, value):
        """
        Set the value of the Limt input for this Choreo. ((optional, integer) Used to page through results. Limits the number of records returned in the response.)
        """
        super(FriendRequestsInputSet, self)._set_input('Limt', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Used to page through results. Returns results starting from the specified number.)
        """
        super(FriendRequestsInputSet, self)._set_input('Offset', value)
    def set_ProfileID(self, value):
        """
        Set the value of the ProfileID input for this Choreo. ((optional, string) The id of the profile to retrieve friend requests for. Defaults to "me" indicating the authenticated user.)
        """
        super(FriendRequestsInputSet, self)._set_input('ProfileID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(FriendRequestsInputSet, self)._set_input('ResponseFormat', value)
    def set_Since(self, value):
        """
        Set the value of the Since input for this Choreo. ((optional, date) Used for time-based pagination. Values can be a unix timestamp or any date accepted by strtotime.)
        """
        super(FriendRequestsInputSet, self)._set_input('Since', value)
    def set_Until(self, value):
        """
        Set the value of the Until input for this Choreo. ((optional, date) Used for time-based pagination. Values can be a unix timestamp or any date accepted by strtotime.)
        """
        super(FriendRequestsInputSet, self)._set_input('Until', value)

class FriendRequestsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FriendRequests Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class FriendRequestsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return FriendRequestsResultSet(response, path)
