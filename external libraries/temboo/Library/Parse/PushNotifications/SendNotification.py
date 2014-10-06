# -*- coding: utf-8 -*-

###############################################################################
#
# SendNotification
# Sends a push notification.
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

class SendNotification(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SendNotification Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SendNotification, self).__init__(temboo_session, '/Library/Parse/PushNotifications/SendNotification')


    def new_input_set(self):
        return SendNotificationInputSet()

    def _make_result_set(self, result, path):
        return SendNotificationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SendNotificationChoreographyExecution(session, exec_id, path)

class SendNotificationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SendNotification
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Notifcation(self, value):
        """
        Set the value of the Notifcation input for this Choreo. ((required, json) Deprecated (retained for backward compatibility only).)
        """
        super(SendNotificationInputSet, self)._set_input('Notifcation', value)
    def set_Notification(self, value):
        """
        Set the value of the Notification input for this Choreo. ((required, json) A JSON string containing the push notification data. See documentation for syntax examples.)
        """
        super(SendNotificationInputSet, self)._set_input('Notification', value)
    def set_ApplicationID(self, value):
        """
        Set the value of the ApplicationID input for this Choreo. ((required, string) The Application ID provided by Parse.)
        """
        super(SendNotificationInputSet, self)._set_input('ApplicationID', value)
    def set_RESTAPIKey(self, value):
        """
        Set the value of the RESTAPIKey input for this Choreo. ((required, string) The REST API Key provided by Parse.)
        """
        super(SendNotificationInputSet, self)._set_input('RESTAPIKey', value)

class SendNotificationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SendNotification Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Parse.)
        """
        return self._output.get('Response', None)

class SendNotificationChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SendNotificationResultSet(response, path)
