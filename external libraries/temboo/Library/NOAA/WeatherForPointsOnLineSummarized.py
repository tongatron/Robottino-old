# -*- coding: utf-8 -*-

###############################################################################
#
# WeatherForPointsOnLineSummarized
# Retrieve weather information for all points on a line defined by a set of latitude and longitude coordinates.
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

class WeatherForPointsOnLineSummarized(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the WeatherForPointsOnLineSummarized Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(WeatherForPointsOnLineSummarized, self).__init__(temboo_session, '/Library/NOAA/WeatherForPointsOnLineSummarized')


    def new_input_set(self):
        return WeatherForPointsOnLineSummarizedInputSet()

    def _make_result_set(self, result, path):
        return WeatherForPointsOnLineSummarizedResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return WeatherForPointsOnLineSummarizedChoreographyExecution(session, exec_id, path)

class WeatherForPointsOnLineSummarizedInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the WeatherForPointsOnLineSummarized
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Endpoint1Latitude(self, value):
        """
        Set the value of the Endpoint1Latitude input for this Choreo. ((required, integer) Enter the latitude of the first endpoint of the line for which weather data is requested. North latitude is positive.)
        """
        super(WeatherForPointsOnLineSummarizedInputSet, self)._set_input('Endpoint1Latitude', value)
    def set_Endpoint1Longitude(self, value):
        """
        Set the value of the Endpoint1Longitude input for this Choreo. ((required, integer) Enter the longitude of the first endpoint of the line for which weather data is requested. West longitude is negative.)
        """
        super(WeatherForPointsOnLineSummarizedInputSet, self)._set_input('Endpoint1Longitude', value)
    def set_Endpoint2Latitude(self, value):
        """
        Set the value of the Endpoint2Latitude input for this Choreo. ((required, integer) Enter the latitude of the second endpoint of the line for which weather data is requested. North latitude is positive.)
        """
        super(WeatherForPointsOnLineSummarizedInputSet, self)._set_input('Endpoint2Latitude', value)
    def set_Endpoint2Longitude(self, value):
        """
        Set the value of the Endpoint2Longitude input for this Choreo. ((required, integer) Enter the longitude of the second endpoint of the line for which weather data is requested. West longitude is negative.)
        """
        super(WeatherForPointsOnLineSummarizedInputSet, self)._set_input('Endpoint2Longitude', value)
    def set_Format(self, value):
        """
        Set the value of the Format input for this Choreo. ((required, string) Specify a timespan for which NDFD data will be summarized. Enter: 24 hourly, for a 24 hour summary, or: 12 hourly, for a 12 hour weather summary.)
        """
        super(WeatherForPointsOnLineSummarizedInputSet, self)._set_input('Format', value)
    def set_NumberOfDays(self, value):
        """
        Set the value of the NumberOfDays input for this Choreo. ((optional, integer) Specify the number of days to retieve data for. If null, data from the earliest date in the dabase is returned.)
        """
        super(WeatherForPointsOnLineSummarizedInputSet, self)._set_input('NumberOfDays', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((optional, date) Enter the start time for retrieval of NDWD information in UTC format. If null, the earliest date in the database is returned. Format: 2004-04-27T12:00.)
        """
        super(WeatherForPointsOnLineSummarizedInputSet, self)._set_input('StartDate', value)
    def set_Unit(self, value):
        """
        Set the value of the Unit input for this Choreo. ((optional, string) Enter the unit format the data will be displayed in. Default is: e, for Standard English (U.S. Standard).  Or: m, for Metric (SI Units).)
        """
        super(WeatherForPointsOnLineSummarizedInputSet, self)._set_input('Unit', value)

class WeatherForPointsOnLineSummarizedResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the WeatherForPointsOnLineSummarized Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) Response from NDFD servers.)
        """
        return self._output.get('Response', None)

class WeatherForPointsOnLineSummarizedChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return WeatherForPointsOnLineSummarizedResultSet(response, path)
