# -*- coding: utf-8 -*-

###############################################################################
#
# TrendingVenues
# Returns a list of venues near the current location with the most people currently checked in.
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

class TrendingVenues(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the TrendingVenues Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(TrendingVenues, self).__init__(temboo_session, '/Library/Foursquare/Venues/TrendingVenues')


    def new_input_set(self):
        return TrendingVenuesInputSet()

    def _make_result_set(self, result, path):
        return TrendingVenuesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TrendingVenuesChoreographyExecution(session, exec_id, path)

class TrendingVenuesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the TrendingVenues
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) The latitude point of the user's location.)
        """
        super(TrendingVenuesInputSet, self)._set_input('Latitude', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Number of results to retun, up to 50.)
        """
        super(TrendingVenuesInputSet, self)._set_input('Limit', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) The longitude point of the user's location.)
        """
        super(TrendingVenuesInputSet, self)._set_input('Longitude', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The Foursquare API OAuth token string.)
        """
        super(TrendingVenuesInputSet, self)._set_input('OauthToken', value)
    def set_Radius(self, value):
        """
        Set the value of the Radius input for this Choreo. ((optional, integer) Radius in meters, up to approximately 2000 meters.)
        """
        super(TrendingVenuesInputSet, self)._set_input('Radius', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(TrendingVenuesInputSet, self)._set_input('ResponseFormat', value)

class TrendingVenuesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the TrendingVenues Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class TrendingVenuesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return TrendingVenuesResultSet(response, path)
