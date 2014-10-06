# -*- coding: utf-8 -*-

###############################################################################
#
# GetListingsCounts
# Retrieves counts of real estate listings from New York Times Web Service.
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

class GetListingsCounts(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetListingsCounts Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetListingsCounts, self).__init__(temboo_session, '/Library/NYTimes/RealEstate/GetListingsCounts')


    def new_input_set(self):
        return GetListingsCountsInputSet()

    def _make_result_set(self, result, path):
        return GetListingsCountsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetListingsCountsChoreographyExecution(session, exec_id, path)

class GetListingsCountsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetListingsCounts
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by NY Times.)
        """
        super(GetListingsCountsInputSet, self)._set_input('APIKey', value)
    def set_Bedrooms(self, value):
        """
        Set the value of the Bedrooms input for this Choreo. ((optional, integer) Limits the results by number of bedrooms to search for. Defaults to 1.)
        """
        super(GetListingsCountsInputSet, self)._set_input('Bedrooms', value)
    def set_DateRange(self, value):
        """
        Set the value of the DateRange input for this Choreo. ((required, string) Sets the quarter, month, week or day for the results (i.e. 2008-Q1, 2008-W52, 2007-07, 2010-10-01, etc).)
        """
        super(GetListingsCountsInputSet, self)._set_input('DateRange', value)
    def set_GeoExtentLevel(self, value):
        """
        Set the value of the GeoExtentLevel input for this Choreo. ((required, string) The geographical unit for the results (i.e. borough, neighborhood, or zip).)
        """
        super(GetListingsCountsInputSet, self)._set_input('GeoExtentLevel', value)
    def set_GeoExtentValue(self, value):
        """
        Set the value of the GeoExtentValue input for this Choreo. ((required, string) Limits the search to a specific area.  For example, if GeoExtentLevel is borough, the value for GeoExtentValue could be Brooklyn.)
        """
        super(GetListingsCountsInputSet, self)._set_input('GeoExtentValue', value)
    def set_GeoSummaryLevel(self, value):
        """
        Set the value of the GeoSummaryLevel input for this Choreo. ((required, string) The geographic unit for grouping the results (borough, neighborhood, or zip).)
        """
        super(GetListingsCountsInputSet, self)._set_input('GeoSummaryLevel', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetListingsCountsInputSet, self)._set_input('ResponseFormat', value)

class GetListingsCountsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetListingsCounts Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the NY Times API)
        """
        return self._output.get('Response', None)

class GetListingsCountsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetListingsCountsResultSet(response, path)
