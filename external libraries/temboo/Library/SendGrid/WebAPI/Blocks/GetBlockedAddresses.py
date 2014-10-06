# -*- coding: utf-8 -*-

###############################################################################
#
# GetBlockedAddresses
# Retrieve a list of blocked emails, with response codes, and optional dates.
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

class GetBlockedAddresses(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetBlockedAddresses Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetBlockedAddresses, self).__init__(temboo_session, '/Library/SendGrid/WebAPI/Blocks/GetBlockedAddresses')


    def new_input_set(self):
        return GetBlockedAddressesInputSet()

    def _make_result_set(self, result, path):
        return GetBlockedAddressesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBlockedAddressesChoreographyExecution(session, exec_id, path)

class GetBlockedAddressesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetBlockedAddresses
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from SendGrid.)
        """
        super(GetBlockedAddressesInputSet, self)._set_input('APIKey', value)
    def set_APIUser(self, value):
        """
        Set the value of the APIUser input for this Choreo. ((required, string) The username registered with SendGrid.)
        """
        super(GetBlockedAddressesInputSet, self)._set_input('APIUser', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((optional, string) The timestamp of the Block records. Enter 1 to return a date in a MySQL timestamp format - YYYY-MM-DD HH:MM:SS)
        """
        super(GetBlockedAddressesInputSet, self)._set_input('Date', value)
    def set_Days(self, value):
        """
        Set the value of the Days input for this Choreo. ((optional, integer) The number of days (greater than 0) for which block data will be retrieved.)
        """
        super(GetBlockedAddressesInputSet, self)._set_input('Days', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((optional, string) Specify the end of the date range for which blocks are to be retireved. The specified date must be in YYYY-MM-DD format.)
        """
        super(GetBlockedAddressesInputSet, self)._set_input('EndDate', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from SendGrid, in either json, or xml.  Default is set to json.)
        """
        super(GetBlockedAddressesInputSet, self)._set_input('ResponseFormat', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((optional, string) The start of the date range for which blocks are to be retireved. The specified date must be in YYYY-MM-DD format, and must be earlier than the EndDate variable value.)
        """
        super(GetBlockedAddressesInputSet, self)._set_input('StartDate', value)


class GetBlockedAddressesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetBlockedAddresses Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        return self._output.get('Response', None)

class GetBlockedAddressesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetBlockedAddressesResultSet(response, path)
