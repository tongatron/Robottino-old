# -*- coding: utf-8 -*-

###############################################################################
#
# GetCountryMetricsForLink
# Returns metrics about the countries referring click traffic to a single bitly link.
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

class GetCountryMetricsForLink(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetCountryMetricsForLink Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetCountryMetricsForLink, self).__init__(temboo_session, '/Library/Bitly/LinkMetrics/GetCountryMetricsForLink')


    def new_input_set(self):
        return GetCountryMetricsForLinkInputSet()

    def _make_result_set(self, result, path):
        return GetCountryMetricsForLinkResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCountryMetricsForLinkChoreographyExecution(session, exec_id, path)

class GetCountryMetricsForLinkInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetCountryMetricsForLink
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The oAuth access token provided by Bitly.)
        """
        super(GetCountryMetricsForLinkInputSet, self)._set_input('AccessToken', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The result limit. Defaults to 100. Range is 1 to 1000.)
        """
        super(GetCountryMetricsForLinkInputSet, self)._set_input('Limit', value)
    def set_Link(self, value):
        """
        Set the value of the Link input for this Choreo. ((required, string) A bitly link.)
        """
        super(GetCountryMetricsForLinkInputSet, self)._set_input('Link', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in. Accepted values are "json" or "xml". Defaults to "json".)
        """
        super(GetCountryMetricsForLinkInputSet, self)._set_input('ResponseFormat', value)
    def set_Rollup(self, value):
        """
        Set the value of the Rollup input for this Choreo. ((optional, boolean) Accepted values are true or false. When set to true, this returns data for multiple units rolled up to a single result instead of a separate value for each period of time.)
        """
        super(GetCountryMetricsForLinkInputSet, self)._set_input('Rollup', value)
    def set_Timestamp(self, value):
        """
        Set the value of the Timestamp input for this Choreo. ((optional, date) An epoch timestamp, indicating the most recent time for which to pull metrics.)
        """
        super(GetCountryMetricsForLinkInputSet, self)._set_input('Timestamp', value)
    def set_Timezone(self, value):
        """
        Set the value of the Timezone input for this Choreo. ((optional, string) An integer hour offset from UTC (-12..12), or a timezone string. Defaults to "America/New_York".)
        """
        super(GetCountryMetricsForLinkInputSet, self)._set_input('Timezone', value)
    def set_UnitName(self, value):
        """
        Set the value of the UnitName input for this Choreo. ((optional, string) The unit of time that corresponds to query you want to run. Accepted values are: minute, hour, day, week, month, and day. Defaults to "day".)
        """
        super(GetCountryMetricsForLinkInputSet, self)._set_input('UnitName', value)
    def set_UnitValue(self, value):
        """
        Set the value of the UnitValue input for this Choreo. ((optional, integer) An integer representing the amount of time to query for. Corresponds to the UnitName input. Defaults to -1 indicating to return all units of time.)
        """
        super(GetCountryMetricsForLinkInputSet, self)._set_input('UnitValue', value)

class GetCountryMetricsForLinkResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetCountryMetricsForLink Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Bitly.)
        """
        return self._output.get('Response', None)

class GetCountryMetricsForLinkChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetCountryMetricsForLinkResultSet(response, path)
