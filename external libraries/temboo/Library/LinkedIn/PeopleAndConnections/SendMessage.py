# -*- coding: utf-8 -*-

###############################################################################
#
# SendMessage
# Sends a message to a connected member given the member's personID.
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

class SendMessage(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SendMessage Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SendMessage, self).__init__(temboo_session, '/Library/LinkedIn/PeopleAndConnections/SendMessage')


    def new_input_set(self):
        return SendMessageInputSet()

    def _make_result_set(self, result, path):
        return SendMessageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SendMessageChoreographyExecution(session, exec_id, path)

class SendMessageInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SendMessage
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by LinkedIn (AKA the OAuth Consumer Key).)
        """
        super(SendMessageInputSet, self)._set_input('APIKey', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(SendMessageInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(SendMessageInputSet, self)._set_input('AccessToken', value)
    def set_Body(self, value):
        """
        Set the value of the Body input for this Choreo. ((required, multiline) Message body. Cannot contain any HTML.)
        """
        super(SendMessageInputSet, self)._set_input('Body', value)
    def set_Recipients(self, value):
        """
        Set the value of the Recipients input for this Choreo. ((required, string) Comma-separated list of recipients by personID. For sending to 'self', put in a tilda (~). Ex.: "~",  "~,XtdrgWytGD".)
        """
        super(SendMessageInputSet, self)._set_input('Recipients', value)
    def set_SecretKey(self, value):
        """
        Set the value of the SecretKey input for this Choreo. ((required, string) The Secret Key provided by LinkedIn (AKA the OAuth Consumer Secret).)
        """
        super(SendMessageInputSet, self)._set_input('SecretKey', value)
    def set_Subject(self, value):
        """
        Set the value of the Subject input for this Choreo. ((required, string) Subject line of message.)
        """
        super(SendMessageInputSet, self)._set_input('Subject', value)

class SendMessageResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SendMessage Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The Response Status Code from LinkedIn. For a successful message, the status code should be 201.)
        """
        return self._output.get('ResponseStatusCode', None)

class SendMessageChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SendMessageResultSet(response, path)
