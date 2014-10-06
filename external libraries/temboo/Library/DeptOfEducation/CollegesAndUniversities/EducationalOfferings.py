# -*- coding: utf-8 -*-

###############################################################################
#
# EducationalOfferings
# Returns educational offerings and admissions data for any college or university.
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

class EducationalOfferings(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the EducationalOfferings Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(EducationalOfferings, self).__init__(temboo_session, '/Library/DeptOfEducation/CollegesAndUniversities/EducationalOfferings')


    def new_input_set(self):
        return EducationalOfferingsInputSet()

    def _make_result_set(self, result, path):
        return EducationalOfferingsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return EducationalOfferingsChoreographyExecution(session, exec_id, path)

class EducationalOfferingsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the EducationalOfferings
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_InstitutionID(self, value):
        """
        Set the value of the InstitutionID input for this Choreo. ((optional, string) Specify an institutionID to return data on a specific institution. These ids can be retrieved from the LookupSchool Choreo.)
        """
        super(EducationalOfferingsInputSet, self)._set_input('InstitutionID', value)
    def set_MaxRows(self, value):
        """
        Set the value of the MaxRows input for this Choreo. ((optional, integer) Limits the number of rows returned. Defaults to 20.)
        """
        super(EducationalOfferingsInputSet, self)._set_input('MaxRows', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml (the default) and json.)
        """
        super(EducationalOfferingsInputSet, self)._set_input('ResponseFormat', value)

class EducationalOfferingsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the EducationalOfferings Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Data.ed.gov.)
        """
        return self._output.get('Response', None)

class EducationalOfferingsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return EducationalOfferingsResultSet(response, path)
