# -*- coding: utf-8 -*-

###############################################################################
#
# GetBicyclingDirections
#  Generate biking directions between two locations, denoted by address or latitude/longitude coordinates.
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

class GetBicyclingDirections(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetBicyclingDirections Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetBicyclingDirections, self).__init__(temboo_session, '/Library/Google/Directions/GetBicyclingDirections')


    def new_input_set(self):
        return GetBicyclingDirectionsInputSet()

    def _make_result_set(self, result, path):
        return GetBicyclingDirectionsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBicyclingDirectionsChoreographyExecution(session, exec_id, path)

class GetBicyclingDirectionsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetBicyclingDirections
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Alternatives(self, value):
        """
        Set the value of the Alternatives input for this Choreo. ((optional, string) If set to true, additional routes will be returned.)
        """
        super(GetBicyclingDirectionsInputSet, self)._set_input('Alternatives', value)
    def set_Destination(self, value):
        """
        Set the value of the Destination input for this Choreo. ((required, string) Enter the address or latitude/longitude coordinates from which directions will be generated (i.e."104 Franklin St, New York, NY" or "40.7160,-74.0037").)
        """
        super(GetBicyclingDirectionsInputSet, self)._set_input('Destination', value)
    def set_Origin(self, value):
        """
        Set the value of the Origin input for this Choreo. ((required, string) Enter the address or latitude/longitude coordinates from which directions will be computed (i.e."104 Franklin St, New York, NY" or "40.7160,-74.0037").)
        """
        super(GetBicyclingDirectionsInputSet, self)._set_input('Origin', value)
    def set_Region(self, value):
        """
        Set the value of the Region input for this Choreo. ((optional, string) Enter the region code for the directions, specified as a ccTLD two-character value.)
        """
        super(GetBicyclingDirectionsInputSet, self)._set_input('Region', value)
    def set_Sensor(self, value):
        """
        Set the value of the Sensor input for this Choreo. ((optional, boolean) Indicates whether or not the directions request is from a device with a location sensor. Value must be either 1 or 0. Defaults to 0 (false).)
        """
        super(GetBicyclingDirectionsInputSet, self)._set_input('Sensor', value)
    def set_Units(self, value):
        """
        Set the value of the Units input for this Choreo. ((optional, string) Specify the units to be used when displaying results.  Options include, metric, or imperial.)
        """
        super(GetBicyclingDirectionsInputSet, self)._set_input('Units', value)
    def set_Waypoints(self, value):
        """
        Set the value of the Waypoints input for this Choreo. ((optional, string) Specify route waypoints, either by address, or latitude/longitude coordinates.)
        """
        super(GetBicyclingDirectionsInputSet, self)._set_input('Waypoints', value)

class GetBicyclingDirectionsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetBicyclingDirections Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Google.)
        """
        return self._output.get('Response', None)

class GetBicyclingDirectionsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetBicyclingDirectionsResultSet(response, path)
