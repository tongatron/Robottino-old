# -*- coding: utf-8 -*-

###############################################################################
#
# GetMostViewed
# Retrieves information for the blog posts and articles that are most frequently viewed.
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

class GetMostViewed(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetMostViewed Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetMostViewed, self).__init__(temboo_session, '/Library/NYTimes/MostPopular/GetMostViewed')


    def new_input_set(self):
        return GetMostViewedInputSet()

    def _make_result_set(self, result, path):
        return GetMostViewedResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetMostViewedChoreographyExecution(session, exec_id, path)

class GetMostViewedInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetMostViewed
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by NY Times.)
        """
        super(GetMostViewedInputSet, self)._set_input('APIKey', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) The first 20 results are shown by default. To page through the results, set Offset to the appropriate value.)
        """
        super(GetMostViewedInputSet, self)._set_input('Offset', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetMostViewedInputSet, self)._set_input('ResponseFormat', value)
    def set_Section(self, value):
        """
        Set the value of the Section input for this Choreo. ((required, string) Limits the results by one or more sections (i.e. arts).  To get all sections, specify all-sections.)
        """
        super(GetMostViewedInputSet, self)._set_input('Section', value)
    def set_TimePeriod(self, value):
        """
        Set the value of the TimePeriod input for this Choreo. ((required, integer) Allowed integer values: 1, 7, or 30, which corresponds to a day (1) , a week (7), or a month (30) of content.)
        """
        super(GetMostViewedInputSet, self)._set_input('TimePeriod', value)

class GetMostViewedResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetMostViewed Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the NY Times API.)
        """
        return self._output.get('Response', None)

class GetMostViewedChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetMostViewedResultSet(response, path)
