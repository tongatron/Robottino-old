# -*- coding: utf-8 -*-

###############################################################################
#
# ListMessages
# Retrieves a list of SMS messages from your Twilio account.
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

class ListMessages(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListMessages Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListMessages, self).__init__(temboo_session, '/Library/Twilio/SMSMessages/ListMessages')


    def new_input_set(self):
        return ListMessagesInputSet()

    def _make_result_set(self, result, path):
        return ListMessagesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListMessagesChoreographyExecution(session, exec_id, path)

class ListMessagesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListMessages
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountSID(self, value):
        """
        Set the value of the AccountSID input for this Choreo. ((required, string) The AccountSID provided when you signed up for a Twilio account.)
        """
        super(ListMessagesInputSet, self)._set_input('AccountSID', value)
    def set_AuthToken(self, value):
        """
        Set the value of the AuthToken input for this Choreo. ((required, string) The authorization token provided when you signed up for a Twilio account.)
        """
        super(ListMessagesInputSet, self)._set_input('AuthToken', value)
    def set_DateSent(self, value):
        """
        Set the value of the DateSent input for this Choreo. ((optional, date) A date in YYYY-MM-DD format. If you use this input, the Choreo will retrieve only messages sent on this date.)
        """
        super(ListMessagesInputSet, self)._set_input('DateSent', value)
    def set_From(self, value):
        """
        Set the value of the From input for this Choreo. ((optional, string) If used, the Choreo will only retrieve messages sent from this phone number.)
        """
        super(ListMessagesInputSet, self)._set_input('From', value)
    def set_PageSize(self, value):
        """
        Set the value of the PageSize input for this Choreo. ((optional, integer) The number of results per page.)
        """
        super(ListMessagesInputSet, self)._set_input('PageSize', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page of results to retrieve. Defaults to 0.)
        """
        super(ListMessagesInputSet, self)._set_input('Page', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(ListMessagesInputSet, self)._set_input('ResponseFormat', value)
    def set_ReturnLegacyFormat(self, value):
        """
        Set the value of the ReturnLegacyFormat input for this Choreo. ((optional, boolean) If set to true, the response will be formatted using the deprecated /SMS/Messages resource schema. This should only be used if you have existing code that relies on the older schema.)
        """
        super(ListMessagesInputSet, self)._set_input('ReturnLegacyFormat', value)
    def set_SubAccountSID(self, value):
        """
        Set the value of the SubAccountSID input for this Choreo. ((optional, string) The SID of the subaccount to retrieve the message from. If not specified, the main AccountSID used to authenticate is used in request.)
        """
        super(ListMessagesInputSet, self)._set_input('SubAccountSID', value)
    def set_To(self, value):
        """
        Set the value of the To input for this Choreo. ((optional, string) If used, the Choreo will only retrieve messages sent to this phone number.)
        """
        super(ListMessagesInputSet, self)._set_input('To', value)

class ListMessagesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListMessages Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Twilio.)
        """
        return self._output.get('Response', None)

class ListMessagesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListMessagesResultSet(response, path)
