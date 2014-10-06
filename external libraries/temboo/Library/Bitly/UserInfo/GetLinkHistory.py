# -*- coding: utf-8 -*-

###############################################################################
#
# GetLinkHistory
# Returns entries from a user's link history in reverse chronological order.
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

class GetLinkHistory(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetLinkHistory Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetLinkHistory, self).__init__(temboo_session, '/Library/Bitly/UserInfo/GetLinkHistory')


    def new_input_set(self):
        return GetLinkHistoryInputSet()

    def _make_result_set(self, result, path):
        return GetLinkHistoryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLinkHistoryChoreographyExecution(session, exec_id, path)

class GetLinkHistoryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetLinkHistory
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The oAuth access token provided by Bitly.)
        """
        super(GetLinkHistoryInputSet, self)._set_input('AccessToken', value)
    def set_Archived(self, value):
        """
        Set the value of the Archived input for this Choreo. ((optional, string) Accepted values are: on|off|both.  Whether to include or exclude archived history entries. (on = return only archived history entries). Defaults to "off".)
        """
        super(GetLinkHistoryInputSet, self)._set_input('Archived', value)
    def set_CreatedAfter(self, value):
        """
        Set the value of the CreatedAfter input for this Choreo. ((optional, date) An epoch timestamp representing a date to filter with.)
        """
        super(GetLinkHistoryInputSet, self)._set_input('CreatedAfter', value)
    def set_CreatedBefore(self, value):
        """
        Set the value of the CreatedBefore input for this Choreo. ((optional, date) An epoch timestamp representing a date to filter with.)
        """
        super(GetLinkHistoryInputSet, self)._set_input('CreatedBefore', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) An integer in the range of 1 to 100, specifying the max number of results to return. Defaults to 50.)
        """
        super(GetLinkHistoryInputSet, self)._set_input('Limit', value)
    def set_Link(self, value):
        """
        Set the value of the Link input for this Choreo. ((optional, string) The bitly link to return metadata for (when spcified, overrides all other options).)
        """
        super(GetLinkHistoryInputSet, self)._set_input('Link', value)
    def set_ModifiedAfter(self, value):
        """
        Set the value of the ModifiedAfter input for this Choreo. ((optional, date) An epoch timestamp representing a date to filter with.)
        """
        super(GetLinkHistoryInputSet, self)._set_input('ModifiedAfter', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, string) An integer specifying the numbered result at which to start (used for pagination).)
        """
        super(GetLinkHistoryInputSet, self)._set_input('Offset', value)
    def set_Private(self, value):
        """
        Set the value of the Private input for this Choreo. ((optional, string) Accepted values are: on|off|both.  Whether to include or exclude archived history entries. (on = return only archived history entries). Defaults to "both".)
        """
        super(GetLinkHistoryInputSet, self)._set_input('Private', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in. Accepted values are "json" or "xml". Defaults to "json".)
        """
        super(GetLinkHistoryInputSet, self)._set_input('ResponseFormat', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((optional, string) The user for whom to retrieve history entries (if different from authenticated user).)
        """
        super(GetLinkHistoryInputSet, self)._set_input('User', value)

class GetLinkHistoryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetLinkHistory Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Bitly.)
        """
        return self._output.get('Response', None)

class GetLinkHistoryChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetLinkHistoryResultSet(response, path)
