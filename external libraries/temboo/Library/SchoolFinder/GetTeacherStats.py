# -*- coding: utf-8 -*-

###############################################################################
#
# GetTeacherStats
# Returns teacher statistics for a school, district, or state. 
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

class GetTeacherStats(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTeacherStats Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetTeacherStats, self).__init__(temboo_session, '/Library/SchoolFinder/GetTeacherStats')


    def new_input_set(self):
        return GetTeacherStatsInputSet()

    def _make_result_set(self, result, path):
        return GetTeacherStatsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTeacherStatsChoreographyExecution(session, exec_id, path)

class GetTeacherStatsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTeacherStats
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) Your School Finder API Key.)
        """
        super(GetTeacherStatsInputSet, self)._set_input('APIKey', value)
    def set_DistrictID(self, value):
        """
        Set the value of the DistrictID input for this Choreo. ((conditional, string) The education.com district id.)
        """
        super(GetTeacherStatsInputSet, self)._set_input('DistrictID', value)
    def set_DistrictLEA(self, value):
        """
        Set the value of the DistrictLEA input for this Choreo. ((conditional, string) The LEA id of the district.)
        """
        super(GetTeacherStatsInputSet, self)._set_input('DistrictLEA', value)
    def set_NCES(self, value):
        """
        Set the value of the NCES input for this Choreo. ((conditional, string) The National Center for Education Statistics (NCES) id of the school.)
        """
        super(GetTeacherStatsInputSet, self)._set_input('NCES', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Format of the response returned by Education.com. Defaluts to XML. JSON is also possible.)
        """
        super(GetTeacherStatsInputSet, self)._set_input('ResponseFormat', value)
    def set_SchoolID(self, value):
        """
        Set the value of the SchoolID input for this Choreo. ((conditional, string) The Education.com id of the school you want to find.)
        """
        super(GetTeacherStatsInputSet, self)._set_input('SchoolID', value)

class GetTeacherStatsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTeacherStats Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Education.com.)
        """
        return self._output.get('Response', None)

class GetTeacherStatsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetTeacherStatsResultSet(response, path)
