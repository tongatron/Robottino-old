# -*- coding: utf-8 -*-

###############################################################################
#
# DeletePhoneNumber
# Deletes an individual phone from Twilio.
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

class DeletePhoneNumber(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeletePhoneNumber Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeletePhoneNumber, self).__init__(temboo_session, '/Library/Twilio/IncomingPhoneNumbers/DeletePhoneNumber')


    def new_input_set(self):
        return DeletePhoneNumberInputSet()

    def _make_result_set(self, result, path):
        return DeletePhoneNumberResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeletePhoneNumberChoreographyExecution(session, exec_id, path)

class DeletePhoneNumberInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeletePhoneNumber
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountSID(self, value):
        """
        Set the value of the AccountSID input for this Choreo. ((required, string) The AccountSID provided when you signed up for a Twilio account.)
        """
        super(DeletePhoneNumberInputSet, self)._set_input('AccountSID', value)
    def set_AuthToken(self, value):
        """
        Set the value of the AuthToken input for this Choreo. ((required, string) The authorization token provided when you signed up for a Twilio account.)
        """
        super(DeletePhoneNumberInputSet, self)._set_input('AuthToken', value)
    def set_IncomingPhoneNumberSID(self, value):
        """
        Set the value of the IncomingPhoneNumberSID input for this Choreo. ((required, string) The id of the incoming phone number to retrieve.)
        """
        super(DeletePhoneNumberInputSet, self)._set_input('IncomingPhoneNumberSID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(DeletePhoneNumberInputSet, self)._set_input('ResponseFormat', value)
    def set_SubAccountSID(self, value):
        """
        Set the value of the SubAccountSID input for this Choreo. ((optional, string) The SID of the subaccount associated with the phone number. If not specified, the main AccountSID used to authenticate is used in the request.)
        """
        super(DeletePhoneNumberInputSet, self)._set_input('SubAccountSID', value)

class DeletePhoneNumberResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeletePhoneNumber Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Twilio.)
        """
        return self._output.get('Response', None)

class DeletePhoneNumberChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeletePhoneNumberResultSet(response, path)
