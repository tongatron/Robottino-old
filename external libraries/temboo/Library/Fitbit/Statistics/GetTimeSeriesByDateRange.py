# -*- coding: utf-8 -*-

###############################################################################
#
# GetTimeSeriesByDateRange
# Gets time series data for a given resource based on a date range you specify.
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

class GetTimeSeriesByDateRange(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTimeSeriesByDateRange Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetTimeSeriesByDateRange, self).__init__(temboo_session, '/Library/Fitbit/Statistics/GetTimeSeriesByDateRange')


    def new_input_set(self):
        return GetTimeSeriesByDateRangeInputSet()

    def _make_result_set(self, result, path):
        return GetTimeSeriesByDateRangeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTimeSeriesByDateRangeChoreographyExecution(session, exec_id, path)

class GetTimeSeriesByDateRangeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTimeSeriesByDateRange
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(GetTimeSeriesByDateRangeInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(GetTimeSeriesByDateRangeInputSet, self)._set_input('AccessToken', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Fitbit.)
        """
        super(GetTimeSeriesByDateRangeInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Fitbit.)
        """
        super(GetTimeSeriesByDateRangeInputSet, self)._set_input('ConsumerSecret', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((required, date) The end date of the date range for the data you want to retrieve (in the format yyyy-MM-dd). You can also specify the value 'today'.)
        """
        super(GetTimeSeriesByDateRangeInputSet, self)._set_input('EndDate', value)
    def set_ResourcePath(self, value):
        """
        Set the value of the ResourcePath input for this Choreo. ((required, string) The resource path that you want to access (for example: activities/log/distance). See Choreo documentation for a full list of resource paths.)
        """
        super(GetTimeSeriesByDateRangeInputSet, self)._set_input('ResourcePath', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in: xml or json. Defaults to json.)
        """
        super(GetTimeSeriesByDateRangeInputSet, self)._set_input('ResponseFormat', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((required, date) The start date of the date range for the data you want to retrieve (in the format yyyy-MM-dd). You can also specify the value 'today'.)
        """
        super(GetTimeSeriesByDateRangeInputSet, self)._set_input('StartDate', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) The user's encoded id. Defaults to "-" (dash) which will return data for the user associated with the token credentials provided.)
        """
        super(GetTimeSeriesByDateRangeInputSet, self)._set_input('UserID', value)

class GetTimeSeriesByDateRangeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTimeSeriesByDateRange Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Fitbit.)
        """
        return self._output.get('Response', None)

class GetTimeSeriesByDateRangeChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetTimeSeriesByDateRangeResultSet(response, path)
