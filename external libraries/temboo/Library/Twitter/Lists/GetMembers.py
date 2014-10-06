# -*- coding: utf-8 -*-

###############################################################################
#
# GetMembers
# Retrieves the members of a specified list.
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

class GetMembers(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetMembers Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetMembers, self).__init__(temboo_session, '/Library/Twitter/Lists/GetMembers')


    def new_input_set(self):
        return GetMembersInputSet()

    def _make_result_set(self, result, path):
        return GetMembersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetMembersChoreographyExecution(session, exec_id, path)

class GetMembersInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetMembers
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret provided by Twitter or retrieved during the OAuth process.)
        """
        super(GetMembersInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token provided by Twitter or retrieved during the OAuth process.)
        """
        super(GetMembersInputSet, self)._set_input('AccessToken', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Twitter.)
        """
        super(GetMembersInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Twitter.)
        """
        super(GetMembersInputSet, self)._set_input('ConsumerSecret', value)
    def set_Cursor(self, value):
        """
        Set the value of the Cursor input for this Choreo. ((optional, string) Allows you to pass in the previous_cursor or next_cursor in order to page through results.)
        """
        super(GetMembersInputSet, self)._set_input('Cursor', value)
    def set_IncludeEntities(self, value):
        """
        Set the value of the IncludeEntities input for this Choreo. ((optional, boolean) The "entities" node containing extra metadata will not be included when set to false.)
        """
        super(GetMembersInputSet, self)._set_input('IncludeEntities', value)
    def set_ListId(self, value):
        """
        Set the value of the ListId input for this Choreo. ((conditional, string) The numerical ID of the list. Required unless Slug is provided.)
        """
        super(GetMembersInputSet, self)._set_input('ListId', value)
    def set_OwnerId(self, value):
        """
        Set the value of the OwnerId input for this Choreo. ((optional, string) The user ID of the user who owns the list being requested by a slug.)
        """
        super(GetMembersInputSet, self)._set_input('OwnerId', value)
    def set_OwnerScreenName(self, value):
        """
        Set the value of the OwnerScreenName input for this Choreo. ((optional, string) The screen name of the user who owns the list being requested by a slug.)
        """
        super(GetMembersInputSet, self)._set_input('OwnerScreenName', value)
    def set_SkipStatus(self, value):
        """
        Set the value of the SkipStatus input for this Choreo. ((optional, boolean) When set to either true, statuses will not be included in the returned user objects.)
        """
        super(GetMembersInputSet, self)._set_input('SkipStatus', value)
    def set_Slug(self, value):
        """
        Set the value of the Slug input for this Choreo. ((optional, string) When identifying a list by a slug, either OwnerScreenName or OwnerId must be provided.)
        """
        super(GetMembersInputSet, self)._set_input('Slug', value)

class GetMembersResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetMembers Choreo.
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

class GetMembersChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetMembersResultSet(response, path)
