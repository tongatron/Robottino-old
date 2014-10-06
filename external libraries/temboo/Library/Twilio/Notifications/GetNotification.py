# -*- coding: utf-8 -*-

###############################################################################
#
# GetNotification
# Get comprehensive log information for a specified Notification SID. 
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

class GetNotification(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetNotification Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetNotification, self).__init__(temboo_session, '/Library/Twilio/Notifications/GetNotification')


    def new_input_set(self):
        return GetNotificationInputSet()

    def _make_result_set(self, result, path):
        return GetNotificationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetNotificationChoreographyExecution(session, exec_id, path)

class GetNotificationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetNotification
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountSID(self, value):
        """
        Set the value of the AccountSID input for this Choreo. ((required, string) The AccountSID provided when you signed up for a Twilio account.)
        """
        super(GetNotificationInputSet, self)._set_input('AccountSID', value)
    def set_AuthToken(self, value):
        """
        Set the value of the AuthToken input for this Choreo. ((required, string) The authorization token provided when you signed up for a Twilio account.)
        """
        super(GetNotificationInputSet, self)._set_input('AuthToken', value)
    def set_NotificationSID(self, value):
        """
        Set the value of the NotificationSID input for this Choreo. ((required, string) Enter the SID of the notification resource to be retrieved.)
        """
        super(GetNotificationInputSet, self)._set_input('NotificationSID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetNotificationInputSet, self)._set_input('ResponseFormat', value)
    def set_SubAccountSID(self, value):
        """
        Set the value of the SubAccountSID input for this Choreo. ((optional, string) The SID of the subaccount to get the notification for. If not specified, the main AccountSID used to authenticate is used in the request.)
        """
        super(GetNotificationInputSet, self)._set_input('SubAccountSID', value)

class GetNotificationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetNotification Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Twilio.)
        """
        return self._output.get('Response', None)

class GetNotificationChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetNotificationResultSet(response, path)
