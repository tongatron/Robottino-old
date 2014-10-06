# -*- coding: utf-8 -*-

###############################################################################
#
# GetLists
# Retrieves all lists the authenticating or specified user subscribes to, including lists that they own.
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

class GetLists(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetLists Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetLists, self).__init__(temboo_session, '/Library/Twitter/Lists/GetLists')


    def new_input_set(self):
        return GetListsInputSet()

    def _make_result_set(self, result, path):
        return GetListsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetListsChoreographyExecution(session, exec_id, path)

class GetListsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetLists
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret provided by Twitter or retrieved during the OAuth process.)
        """
        super(GetListsInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token provided by Twitter or retrieved during the OAuth process.)
        """
        super(GetListsInputSet, self)._set_input('AccessToken', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Twitter.)
        """
        super(GetListsInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Twitter.)
        """
        super(GetListsInputSet, self)._set_input('ConsumerSecret', value)
    def set_Reverse(self, value):
        """
        Set the value of the Reverse input for this Choreo. ((optional, boolean) When set to true, owned lists will be returned first in the response.)
        """
        super(GetListsInputSet, self)._set_input('Reverse', value)
    def set_ScreenName(self, value):
        """
        Set the value of the ScreenName input for this Choreo. ((optional, string) The screen name of the user for whom to return results for. If not provided, the subscriptions for the authenticating user are returned.)
        """
        super(GetListsInputSet, self)._set_input('ScreenName', value)
    def set_UserId(self, value):
        """
        Set the value of the UserId input for this Choreo. ((optional, string) The ID of the user for whom to return results for. If not provided, the subscriptions for the authenticating user are returned.)
        """
        super(GetListsInputSet, self)._set_input('UserId', value)

class GetListsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetLists Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Twitter.)
        """
        return self._output.get('Response', None)
    def get_Limit(self):
        """
        Retrieve the value for the "Limit" output from this Choreo execution. ((integer) The rate limit ceiling for this particular request.)
        """
        return self._output.get('Limit', None)
    def get_Remaining(self):
        """
        Retrieve the value for the "Remaining" output from this Choreo execution. ((integer) The number of requests left for the 15 minute window.)
        """
        return self._output.get('Remaining', None)
    def get_Reset(self):
        """
        Retrieve the value for the "Reset" output from this Choreo execution. ((date) The remaining window before the rate limit resets in UTC epoch seconds.)
        """
        return self._output.get('Reset', None)

class GetListsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetListsResultSet(response, path)
