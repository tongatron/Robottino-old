# -*- coding: utf-8 -*-

###############################################################################
#
# ListNotifications
# Return a list of all notifications generated for a specified account.
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

class ListNotifications(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListNotifications Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListNotifications, self).__init__(temboo_session, '/Library/Twilio/Notifications/ListNotifications')


    def new_input_set(self):
        return ListNotificationsInputSet()

    def _make_result_set(self, result, path):
        return ListNotificationsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListNotificationsChoreographyExecution(session, exec_id, path)

class ListNotificationsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListNotifications
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountSID(self, value):
        """
        Set the value of the AccountSID input for this Choreo. ((required, string) The AccountSID provided when you signed up for a Twilio account.)
        """
        super(ListNotificationsInputSet, self)._set_input('AccountSID', value)
    def set_AuthToken(self, value):
        """
        Set the value of the AuthToken input for this Choreo. ((required, string) The authorization token provided when you signed up for a Twilio account.)
        """
        super(ListNotificationsInputSet, self)._set_input('AuthToken', value)
    def set_LogLevel(self, value):
        """
        Set the value of the LogLevel input for this Choreo. ((optional, integer) Specify the log level by entering: 0 for ERROR, 1 for WARNING.)
        """
        super(ListNotificationsInputSet, self)._set_input('LogLevel', value)
    def set_MessageDate(self, value):
        """
        Set the value of the MessageDate input for this Choreo. ((optional, string) Filter notifications by date.  Dates should be formatted as follows: YYYY-MM-DD.  Dates before, at, or after a specified date can be entered using inequality operators: >=YYYY-MM-DD)
        """
        super(ListNotificationsInputSet, self)._set_input('MessageDate', value)
    def set_PageSize(self, value):
        """
        Set the value of the PageSize input for this Choreo. ((optional, integer) The number of results per page.)
        """
        super(ListNotificationsInputSet, self)._set_input('PageSize', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page of results to retrieve. Defaults to 0.)
        """
        super(ListNotificationsInputSet, self)._set_input('Page', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(ListNotificationsInputSet, self)._set_input('ResponseFormat', value)
    def set_SubAccountSID(self, value):
        """
        Set the value of the SubAccountSID input for this Choreo. ((optional, string) The SID of the subaccount to list notifications for. If not specified, the main AccountSID used to authenticate is used in the request.)
        """
        super(ListNotificationsInputSet, self)._set_input('SubAccountSID', value)

class ListNotificationsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListNotifications Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Twilio.)
        """
        return self._output.get('Response', None)

class ListNotificationsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListNotificationsResultSet(response, path)
