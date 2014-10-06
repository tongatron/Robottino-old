# -*- coding: utf-8 -*-

###############################################################################
#
# Push
# Sends a text message to the specified number using USSD protocol. 
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

class Push(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Push Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Push, self).__init__(temboo_session, '/Library/Nexmo/USSD/Push')


    def new_input_set(self):
        return PushInputSet()

    def _make_result_set(self, result, path):
        return PushResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PushChoreographyExecution(session, exec_id, path)

class PushInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Push
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) Your API Key provided to you by Nexmo.)
        """
        super(PushInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) Your API Secret provided to you by Nexmo.)
        """
        super(PushInputSet, self)._set_input('APISecret', value)
    def set_ClientReference(self, value):
        """
        Set the value of the ClientReference input for this Choreo. ((optional, string) Include a note for your reference. (40 characters max).)
        """
        super(PushInputSet, self)._set_input('ClientReference', value)
    def set_DeliveryReceipt(self, value):
        """
        Set the value of the DeliveryReceipt input for this Choreo. ((optional, integer) Set to 1 to receive a Delivery Receipt for this message. Make sure to configure your "Callback URL" in your "API Settings".)
        """
        super(PushInputSet, self)._set_input('DeliveryReceipt', value)
    def set_From(self, value):
        """
        Set the value of the From input for this Choreo. ((required, string) Sender address could be alphanumeric (e.g. MyCompany20). Restrictions may apply depending on the destination.)
        """
        super(PushInputSet, self)._set_input('From', value)
    def set_NetworkCode(self, value):
        """
        Set the value of the NetworkCode input for this Choreo. ((optional, string) Sends this message to the specifed network operator (MCCMNC).)
        """
        super(PushInputSet, self)._set_input('NetworkCode', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "json" (the default) and "xml".)
        """
        super(PushInputSet, self)._set_input('ResponseFormat', value)
    def set_Text(self, value):
        """
        Set the value of the Text input for this Choreo. ((conditional, string) Required when Type is "text".  Body of the text message. (with a maximum length of 3200 characters).)
        """
        super(PushInputSet, self)._set_input('Text', value)
    def set_To(self, value):
        """
        Set the value of the To input for this Choreo. ((required, string) Mobile number in international format, and one recipient per request. (e.g. 447525856424 or 00447525856424 when sending to UK.))
        """
        super(PushInputSet, self)._set_input('To', value)

class PushResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Push Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Nexmo. Corresponds to the ResponseFormat input. Defaults to json.)
        """
        return self._output.get('Response', None)

class PushChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PushResultSet(response, path)
