# -*- coding: utf-8 -*-

###############################################################################
#
# GetUnreadMessagesFromUser
# Retrieves a list of messages in the authenticating user's inbox that are marked as unread and sent from a specified user.
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

class GetUnreadMessagesFromUser(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetUnreadMessagesFromUser Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetUnreadMessagesFromUser, self).__init__(temboo_session, '/Library/Facebook/Reading/GetUnreadMessagesFromUser')


    def new_input_set(self):
        return GetUnreadMessagesFromUserInputSet()

    def _make_result_set(self, result, path):
        return GetUnreadMessagesFromUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetUnreadMessagesFromUserChoreographyExecution(session, exec_id, path)

class GetUnreadMessagesFromUserInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetUnreadMessagesFromUser
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        super(GetUnreadMessagesFromUserInputSet, self)._set_input('AccessToken', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) The name of the user who may have sent messages that you want to retrieve. The parameter is used in a 'contains' query, so a partial name is acceptable for searches.)
        """
        super(GetUnreadMessagesFromUserInputSet, self)._set_input('Name', value)
    def set_ResponseMode(self, value):
        """
        Set the value of the ResponseMode input for this Choreo. ((optional, string) Used to simplify the response. Valid values are: simple and verbose. When set to simple, only an array of messages are returned. Verbose mode returns additional metadata. Defaults to "simple".)
        """
        super(GetUnreadMessagesFromUserInputSet, self)._set_input('ResponseMode', value)

class GetUnreadMessagesFromUserResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetUnreadMessagesFromUser Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Facebook.)
        """
        return self._output.get('Response', None)

class GetUnreadMessagesFromUserChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetUnreadMessagesFromUserResultSet(response, path)
