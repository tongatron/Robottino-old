# -*- coding: utf-8 -*-

###############################################################################
#
# TopStatsLastWeekByDay
# Retrieves last weeks's top pages, links, and searches, by day.
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

class TopStatsLastWeekByDay(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the TopStatsLastWeekByDay Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(TopStatsLastWeekByDay, self).__init__(temboo_session, '/Library/Clicky/TopStatsLastWeekByDay')


    def new_input_set(self):
        return TopStatsLastWeekByDayInputSet()

    def _make_result_set(self, result, path):
        return TopStatsLastWeekByDayResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TopStatsLastWeekByDayChoreographyExecution(session, exec_id, path)

class TopStatsLastWeekByDayInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the TopStatsLastWeekByDay
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Output(self, value):
        """
        Set the value of the Output input for this Choreo. ((optional, string) What format you want the returned data to be in. Accepted values: xml, php, json, csv. Defaults to 'xml'.)
        """
        super(TopStatsLastWeekByDayInputSet, self)._set_input('Output', value)
    def set_SiteID(self, value):
        """
        Set the value of the SiteID input for this Choreo. ((required, integer) Your request must include the site's ID that you want to access data from. Available from your site preferences page.)
        """
        super(TopStatsLastWeekByDayInputSet, self)._set_input('SiteID', value)
    def set_SiteKey(self, value):
        """
        Set the value of the SiteKey input for this Choreo. ((required, string) The unique key assigned to you when you first register with Clicky. Available from your site preferences page.)
        """
        super(TopStatsLastWeekByDayInputSet, self)._set_input('SiteKey', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((optional, string) The type of data you want to retrieve. Defaults to "pages,links,searches".)
        """
        super(TopStatsLastWeekByDayInputSet, self)._set_input('Type', value)

class TopStatsLastWeekByDayResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the TopStatsLastWeekByDay Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Clicky formatted as specified in the Output parameter. Default is XML.)
        """
        return self._output.get('Response', None)

class TopStatsLastWeekByDayChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return TopStatsLastWeekByDayResultSet(response, path)
