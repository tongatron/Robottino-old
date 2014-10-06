# -*- coding: utf-8 -*-

###############################################################################
#
# GetNearbyFriends
# Returns a list of recent friends' check-ins that are nearby the specified location.
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

class GetNearbyFriends(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetNearbyFriends Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetNearbyFriends, self).__init__(temboo_session, '/Library/Foursquare/Checkins/GetNearbyFriends')


    def new_input_set(self):
        return GetNearbyFriendsInputSet()

    def _make_result_set(self, result, path):
        return GetNearbyFriendsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetNearbyFriendsChoreographyExecution(session, exec_id, path)

class GetNearbyFriendsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetNearbyFriends
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Distance(self, value):
        """
        Set the value of the Distance input for this Choreo. ((optional, integer) The distance (in meters) between the supplied coordinates and the checkin location. This returns friends' checkins where the distance is less than or equal to this value. Default is 500.)
        """
        super(GetNearbyFriendsInputSet, self)._set_input('Distance', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) The latitude point of the user's location.)
        """
        super(GetNearbyFriendsInputSet, self)._set_input('Latitude', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Number of results to return, up to 100.)
        """
        super(GetNearbyFriendsInputSet, self)._set_input('Limit', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) The longitude point of the user's location.)
        """
        super(GetNearbyFriendsInputSet, self)._set_input('Longitude', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The Foursquare API OAuth token string.)
        """
        super(GetNearbyFriendsInputSet, self)._set_input('OauthToken', value)
    def set_ResponseMode(self, value):
        """
        Set the value of the ResponseMode input for this Choreo. ((optional, string) Used to simplify the response. Valid values are: simple and verbose. When set to simple, an array of user objects are returned. Verbose mode returns an array of checkin objects. Defaults to "simple".)
        """
        super(GetNearbyFriendsInputSet, self)._set_input('ResponseMode', value)

class GetNearbyFriendsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetNearbyFriends Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class GetNearbyFriendsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetNearbyFriendsResultSet(response, path)
