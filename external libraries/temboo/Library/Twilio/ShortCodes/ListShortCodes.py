# -*- coding: utf-8 -*-

###############################################################################
#
# ListShortCodes
# Returns a list of Twilio short codes which can send and receive SMS messages with mobile phones.
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

class ListShortCodes(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListShortCodes Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListShortCodes, self).__init__(temboo_session, '/Library/Twilio/ShortCodes/ListShortCodes')


    def new_input_set(self):
        return ListShortCodesInputSet()

    def _make_result_set(self, result, path):
        return ListShortCodesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListShortCodesChoreographyExecution(session, exec_id, path)

class ListShortCodesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListShortCodes
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountSID(self, value):
        """
        Set the value of the AccountSID input for this Choreo. ((required, string) The AccountSID provided when you signed up for a Twilio account.)
        """
        super(ListShortCodesInputSet, self)._set_input('AccountSID', value)
    def set_AuthToken(self, value):
        """
        Set the value of the AuthToken input for this Choreo. ((required, string) The authorization token provided when you signed up for a Twilio account.)
        """
        super(ListShortCodesInputSet, self)._set_input('AuthToken', value)
    def set_FriendlyName(self, value):
        """
        Set the value of the FriendlyName input for this Choreo. ((optional, string) Only return the short code resources with friendly names that exactly match this name.)
        """
        super(ListShortCodesInputSet, self)._set_input('FriendlyName', value)
    def set_PageSize(self, value):
        """
        Set the value of the PageSize input for this Choreo. ((optional, integer) The number of results per page.)
        """
        super(ListShortCodesInputSet, self)._set_input('PageSize', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page of results to retrieve. Defaults to 0.)
        """
        super(ListShortCodesInputSet, self)._set_input('Page', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(ListShortCodesInputSet, self)._set_input('ResponseFormat', value)
    def set_ShortCode(self, value):
        """
        Set the value of the ShortCode input for this Choreo. ((optional, string) Only return the short code resources that match this pattern. You can specify partial numbers and use '*' as a wildcard for any digit.)
        """
        super(ListShortCodesInputSet, self)._set_input('ShortCode', value)
    def set_SubAccountSID(self, value):
        """
        Set the value of the SubAccountSID input for this Choreo. ((optional, string) The SID of the subaccount associated with the list of short codes. If not specified, the main AccountSID used to authenticate is used in the request.)
        """
        super(ListShortCodesInputSet, self)._set_input('SubAccountSID', value)

class ListShortCodesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListShortCodes Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Twilio.)
        """
        return self._output.get('Response', None)

class ListShortCodesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListShortCodesResultSet(response, path)
