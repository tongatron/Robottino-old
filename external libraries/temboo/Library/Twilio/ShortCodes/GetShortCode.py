# -*- coding: utf-8 -*-

###############################################################################
#
# GetShortCode
# Retrieves an individual short code resource.
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

class GetShortCode(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetShortCode Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetShortCode, self).__init__(temboo_session, '/Library/Twilio/ShortCodes/GetShortCode')


    def new_input_set(self):
        return GetShortCodeInputSet()

    def _make_result_set(self, result, path):
        return GetShortCodeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetShortCodeChoreographyExecution(session, exec_id, path)

class GetShortCodeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetShortCode
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountSID(self, value):
        """
        Set the value of the AccountSID input for this Choreo. ((required, string) The AccountSID provided when you signed up for a Twilio account.)
        """
        super(GetShortCodeInputSet, self)._set_input('AccountSID', value)
    def set_AuthToken(self, value):
        """
        Set the value of the AuthToken input for this Choreo. ((required, string) The authorization token provided when you signed up for a Twilio account.)
        """
        super(GetShortCodeInputSet, self)._set_input('AuthToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetShortCodeInputSet, self)._set_input('ResponseFormat', value)
    def set_ShortCodeSID(self, value):
        """
        Set the value of the ShortCodeSID input for this Choreo. ((required, string) The id of the short code to retrieve.)
        """
        super(GetShortCodeInputSet, self)._set_input('ShortCodeSID', value)
    def set_SubAccountSID(self, value):
        """
        Set the value of the SubAccountSID input for this Choreo. ((optional, string) The SID of the subaccount associated with short code. If not specified, the main AccountSID used to authenticate is used in the request.)
        """
        super(GetShortCodeInputSet, self)._set_input('SubAccountSID', value)

class GetShortCodeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetShortCode Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Twilio.)
        """
        return self._output.get('Response', None)

class GetShortCodeChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetShortCodeResultSet(response, path)
