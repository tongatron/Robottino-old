# -*- coding: utf-8 -*-

###############################################################################
#
# ReverseGeocode
# Given a latitude and a longitude coordinates, returns up to 20 places that can be used as a Place ID when updating a status.
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

class ReverseGeocode(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ReverseGeocode Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ReverseGeocode, self).__init__(temboo_session, '/Library/Twitter/PlacesAndGeo/ReverseGeocode')


    def new_input_set(self):
        return ReverseGeocodeInputSet()

    def _make_result_set(self, result, path):
        return ReverseGeocodeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ReverseGeocodeChoreographyExecution(session, exec_id, path)

class ReverseGeocodeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ReverseGeocode
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret provided by Twitter or retrieved during the OAuth process.)
        """
        super(ReverseGeocodeInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token provided by Twitter or retrieved during the OAuth process.)
        """
        super(ReverseGeocodeInputSet, self)._set_input('AccessToken', value)
    def set_Accuracy(self, value):
        """
        Set the value of the Accuracy input for this Choreo. ((optional, string) A hint on the "region" in which to search. If a number, then this is a radius in meters. You can also specify feet by using the ft suffix (i.e. 5ft).)
        """
        super(ReverseGeocodeInputSet, self)._set_input('Accuracy', value)
    def set_Callback(self, value):
        """
        Set the value of the Callback input for this Choreo. ((optional, string) If supplied, the response will use the JSONP format with a callback of the given name.)
        """
        super(ReverseGeocodeInputSet, self)._set_input('Callback', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Twitter.)
        """
        super(ReverseGeocodeInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Twitter.)
        """
        super(ReverseGeocodeInputSet, self)._set_input('ConsumerSecret', value)
    def set_Granularity(self, value):
        """
        Set the value of the Granularity input for this Choreo. ((optional, string) This is the minimal granularity of place types to return and must be one of: poi, neighborhood, city, admin or country. Defaults to neighborhood.)
        """
        super(ReverseGeocodeInputSet, self)._set_input('Granularity', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) The latitude to search around.)
        """
        super(ReverseGeocodeInputSet, self)._set_input('Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) The longitude to search around.)
        """
        super(ReverseGeocodeInputSet, self)._set_input('Longitude', value)
    def set_MaxResults(self, value):
        """
        Set the value of the MaxResults input for this Choreo. ((optional, integer) The maximum number of results to return.)
        """
        super(ReverseGeocodeInputSet, self)._set_input('MaxResults', value)

class ReverseGeocodeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ReverseGeocode Choreo.
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

class ReverseGeocodeChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ReverseGeocodeResultSet(response, path)
