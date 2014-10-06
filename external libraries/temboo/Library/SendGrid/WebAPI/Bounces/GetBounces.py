# -*- coding: utf-8 -*-

###############################################################################
#
# GetBounces
# Retrieve a list of bounced emails, with response codes, and optional dates.
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

class GetBounces(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetBounces Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetBounces, self).__init__(temboo_session, '/Library/SendGrid/WebAPI/Bounces/GetBounces')


    def new_input_set(self):
        return GetBouncesInputSet()

    def _make_result_set(self, result, path):
        return GetBouncesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBouncesChoreographyExecution(session, exec_id, path)

class GetBouncesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetBounces
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from SendGrid.)
        """
        super(GetBouncesInputSet, self)._set_input('APIKey', value)
    def set_APIUser(self, value):
        """
        Set the value of the APIUser input for this Choreo. ((required, string) The username registered with SendGrid.)
        """
        super(GetBouncesInputSet, self)._set_input('APIUser', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((optional, string) The timestamp of the Block records. Enter 1 to return a date in a MySQL timestamp format - YYYY-MM-DD HH:MM:SS)
        """
        super(GetBouncesInputSet, self)._set_input('Date', value)
    def set_Days(self, value):
        """
        Set the value of the Days input for this Choreo. ((optional, integer) The number of days (greater than 0) for which block data will be retrieved.)
        """
        super(GetBouncesInputSet, self)._set_input('Days', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((optional, string) The email to search for.)
        """
        super(GetBouncesInputSet, self)._set_input('Email', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((optional, string) The end of the date range for which blocks are to be retireved. The specified date must be in YYYY-MM-DD format.)
        """
        super(GetBouncesInputSet, self)._set_input('EndDate', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number to limit the number of results returned.)
        """
        super(GetBouncesInputSet, self)._set_input('Limit', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) The beginning point in the list to retrieve bounces from.)
        """
        super(GetBouncesInputSet, self)._set_input('Offset', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from SendGrid, in either json, or xml.  Default is set to json.)
        """
        super(GetBouncesInputSet, self)._set_input('ResponseFormat', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((optional, string) The start of the date range for which blocks are to be retireved. The specified date must be in YYYY-MM-DD format, and must be earlier than the EndDate variable value.)
        """
        super(GetBouncesInputSet, self)._set_input('StartDate', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((optional, string) The type of bounce to search for. Choice included are: hard, or soft.)
        """
        super(GetBouncesInputSet, self)._set_input('Type', value)


class GetBouncesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetBounces Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        return self._output.get('Response', None)

class GetBouncesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetBouncesResultSet(response, path)
