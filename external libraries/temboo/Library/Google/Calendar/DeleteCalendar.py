# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteCalendar
# Delete a secondary calendar.
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

class DeleteCalendar(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteCalendar Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteCalendar, self).__init__(temboo_session, '/Library/Google/Calendar/DeleteCalendar')


    def new_input_set(self):
        return DeleteCalendarInputSet()

    def _make_result_set(self, result, path):
        return DeleteCalendarResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteCalendarChoreographyExecution(session, exec_id, path)

class DeleteCalendarInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteCalendar
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        super(DeleteCalendarInputSet, self)._set_input('AccessToken', value)
    def set_CalendarID(self, value):
        """
        Set the value of the CalendarID input for this Choreo. ((required, string) The unique ID for the calendar to delete. Note that calendar IDs can be retrieved by running GetAllCalendars or SearchCalendarsByName.)
        """
        super(DeleteCalendarInputSet, self)._set_input('CalendarID', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((required, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        super(DeleteCalendarInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((required, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        super(DeleteCalendarInputSet, self)._set_input('ClientSecret', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((required, string) An OAuth Refresh Token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(DeleteCalendarInputSet, self)._set_input('RefreshToken', value)

class DeleteCalendarResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteCalendar Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (No content is returned for delete calendar operations.)
        """
        return self._output.get('Response', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)

class DeleteCalendarChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteCalendarResultSet(response, path)
