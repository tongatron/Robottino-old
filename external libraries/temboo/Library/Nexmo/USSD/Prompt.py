# -*- coding: utf-8 -*-

###############################################################################
#
# Prompt
# Sends a text message to the specified number using USSD protocol.  You can then listen to inbound messages.
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

class Prompt(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Prompt Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Prompt, self).__init__(temboo_session, '/Library/Nexmo/USSD/Prompt')


    def new_input_set(self):
        return PromptInputSet()

    def _make_result_set(self, result, path):
        return PromptResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PromptChoreographyExecution(session, exec_id, path)

class PromptInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Prompt
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) Your API Key provided to you by Nexmo.)
        """
        super(PromptInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) Your API Secret provided to you by Nexmo.)
        """
        super(PromptInputSet, self)._set_input('APISecret', value)
    def set_ClientReference(self, value):
        """
        Set the value of the ClientReference input for this Choreo. ((optional, string) Include a note for your reference. (40 characters max).)
        """
        super(PromptInputSet, self)._set_input('ClientReference', value)
    def set_DeliveryReceipt(self, value):
        """
        Set the value of the DeliveryReceipt input for this Choreo. ((optional, integer) Set to 1 to receive a Delivery Receipt for this message. Make sure to configure your "Callback URL" in your "API Settings".)
        """
        super(PromptInputSet, self)._set_input('DeliveryReceipt', value)
    def set_From(self, value):
        """
        Set the value of the From input for this Choreo. ((required, string) Sender address could be alphanumeric (e.g. MyCompany20). Restrictions may apply depending on the destination.)
        """
        super(PromptInputSet, self)._set_input('From', value)
    def set_NetworkCode(self, value):
        """
        Set the value of the NetworkCode input for this Choreo. ((optional, string) Sends this message to the specifed network operator (MCCMNC).)
        """
        super(PromptInputSet, self)._set_input('NetworkCode', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "json" (the default) and "xml".)
        """
        super(PromptInputSet, self)._set_input('ResponseFormat', value)
    def set_Text(self, value):
        """
        Set the value of the Text input for this Choreo. ((conditional, string) Required when Type is "text".  Body of the text message (with a maximum length of 3200 characters))
        """
        super(PromptInputSet, self)._set_input('Text', value)
    def set_To(self, value):
        """
        Set the value of the To input for this Choreo. ((required, string) Mobile number in international format, and one recipient per request. (e.g. 447525856424 or 00447525856424 when sending to UK))
        """
        super(PromptInputSet, self)._set_input('To', value)

class PromptResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Prompt Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Nexmo. Corresponds to the ResponseFormat input. Defaults to json.)
        """
        return self._output.get('Response', None)

class PromptChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PromptResultSet(response, path)
