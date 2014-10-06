# -*- coding: utf-8 -*-

###############################################################################
#
# GetTimestampFromDateString
# Returns the the specified date string, expressed as seconds or milliseconds since January 1, 1970 (epoch time).
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

class GetTimestampFromDateString(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTimestampFromDateString Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetTimestampFromDateString, self).__init__(temboo_session, '/Library/Utilities/Dates/GetTimestampFromDateString')


    def new_input_set(self):
        return GetTimestampFromDateStringInputSet()

    def _make_result_set(self, result, path):
        return GetTimestampFromDateStringResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTimestampFromDateStringChoreographyExecution(session, exec_id, path)

class GetTimestampFromDateStringInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTimestampFromDateString
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AddDays(self, value):
        """
        Set the value of the AddDays input for this Choreo. ((optional, integer) Adds the specified number of days to the specified date serial number. A negative number will subtract.)
        """
        super(GetTimestampFromDateStringInputSet, self)._set_input('AddDays', value)
    def set_AddHours(self, value):
        """
        Set the value of the AddHours input for this Choreo. ((optional, integer) Adds the specified number of hours to the specified date serial number. A negative number will subtract.)
        """
        super(GetTimestampFromDateStringInputSet, self)._set_input('AddHours', value)
    def set_AddMinutes(self, value):
        """
        Set the value of the AddMinutes input for this Choreo. ((optional, integer) Adds the specified number of minutes to the specified date serial number. A negative number will subtract.)
        """
        super(GetTimestampFromDateStringInputSet, self)._set_input('AddMinutes', value)
    def set_AddMonths(self, value):
        """
        Set the value of the AddMonths input for this Choreo. ((optional, integer) Adds the specified number of months to the specified date serial number. A negative number will subtract.)
        """
        super(GetTimestampFromDateStringInputSet, self)._set_input('AddMonths', value)
    def set_AddSeconds(self, value):
        """
        Set the value of the AddSeconds input for this Choreo. ((optional, integer) Adds the specified number of seconds to the specified date serial number. A negative number will subtract.)
        """
        super(GetTimestampFromDateStringInputSet, self)._set_input('AddSeconds', value)
    def set_AddYears(self, value):
        """
        Set the value of the AddYears input for this Choreo. ((optional, integer) Adds the specified number of years to the specified date serial number. A negative number will subtract.)
        """
        super(GetTimestampFromDateStringInputSet, self)._set_input('AddYears', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((required, string) A date string to convert to a timestamp (e.g., March 2, 2014).)
        """
        super(GetTimestampFromDateStringInputSet, self)._set_input('Date', value)
    def set_Granularity(self, value):
        """
        Set the value of the Granularity input for this Choreo. ((optional, string) Set to "seconds" to return the number of seconds since the epoch. Defaults to "milliseconds".)
        """
        super(GetTimestampFromDateStringInputSet, self)._set_input('Granularity', value)
    def set_SetDay(self, value):
        """
        Set the value of the SetDay input for this Choreo. ((optional, integer) Sets the day of month (1–31) of the specified date serial number.)
        """
        super(GetTimestampFromDateStringInputSet, self)._set_input('SetDay', value)
    def set_SetHour(self, value):
        """
        Set the value of the SetHour input for this Choreo. ((optional, integer) Sets the hours (0–23) of the specified date serial number.)
        """
        super(GetTimestampFromDateStringInputSet, self)._set_input('SetHour', value)
    def set_SetMinute(self, value):
        """
        Set the value of the SetMinute input for this Choreo. ((optional, integer) Sets the minutes (0–59) of the specified date serial number.)
        """
        super(GetTimestampFromDateStringInputSet, self)._set_input('SetMinute', value)
    def set_SetMonth(self, value):
        """
        Set the value of the SetMonth input for this Choreo. ((optional, integer) Sets the month (1–12) of the specified date serial number.)
        """
        super(GetTimestampFromDateStringInputSet, self)._set_input('SetMonth', value)
    def set_SetSecond(self, value):
        """
        Set the value of the SetSecond input for this Choreo. ((optional, integer) Sets the seconds (0–59) of the specified date serial number.)
        """
        super(GetTimestampFromDateStringInputSet, self)._set_input('SetSecond', value)
    def set_SetYear(self, value):
        """
        Set the value of the SetYear input for this Choreo. ((optional, integer) Sets the year (such as 1989) of the specified date serial number.)
        """
        super(GetTimestampFromDateStringInputSet, self)._set_input('SetYear', value)

class GetTimestampFromDateStringResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTimestampFromDateString Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Timestamp(self):
        """
        Retrieve the value for the "Timestamp" output from this Choreo execution. ((date) A the current timestamp, expressed as the number of seconds or milliseconds since January 1, 1970 (epoch time). The Granularity input is used to indicate seconds or milliseconds.)
        """
        return self._output.get('Timestamp', None)

class GetTimestampFromDateStringChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetTimestampFromDateStringResultSet(response, path)
