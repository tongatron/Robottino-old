# -*- coding: utf-8 -*-

###############################################################################
#
# SearchContactsByUpdatedSince
# Searches your Constant Contact list by last updated date.  Use this Choreo for synchronizing your lists with other systems. 
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

class SearchContactsByUpdatedSince(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchContactsByUpdatedSince Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SearchContactsByUpdatedSince, self).__init__(temboo_session, '/Library/ConstantContact/SearchContactsByUpdatedSince')


    def new_input_set(self):
        return SearchContactsByUpdatedSinceInputSet()

    def _make_result_set(self, result, path):
        return SearchContactsByUpdatedSinceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchContactsByUpdatedSinceChoreographyExecution(session, exec_id, path)

class SearchContactsByUpdatedSinceInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchContactsByUpdatedSince
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Constant Contact.)
        """
        super(SearchContactsByUpdatedSinceInputSet, self)._set_input('APIKey', value)
    def set_ListType(self, value):
        """
        Set the value of the ListType input for this Choreo. ((optional, string) The list type to query.  Supported values for this parameter are: active, removed and do-not-mail. Defaults to 'active'.)
        """
        super(SearchContactsByUpdatedSinceInputSet, self)._set_input('ListType', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Constant Contact password.)
        """
        super(SearchContactsByUpdatedSinceInputSet, self)._set_input('Password', value)
    def set_UpdatedSince(self, value):
        """
        Set the value of the UpdatedSince input for this Choreo. ((required, date) Epoch timestamp in milliseconds or formatted like 2009-12-01T01:00:00.000Z. Used to query for modified records.)
        """
        super(SearchContactsByUpdatedSinceInputSet, self)._set_input('UpdatedSince', value)
    def set_UserName(self, value):
        """
        Set the value of the UserName input for this Choreo. ((required, string) Your Constant Contact username.)
        """
        super(SearchContactsByUpdatedSinceInputSet, self)._set_input('UserName', value)

class SearchContactsByUpdatedSinceResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchContactsByUpdatedSince Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Constant Contact.)
        """
        return self._output.get('Response', None)

class SearchContactsByUpdatedSinceChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SearchContactsByUpdatedSinceResultSet(response, path)
