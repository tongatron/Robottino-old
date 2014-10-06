# -*- coding: utf-8 -*-

###############################################################################
#
# ListDetails
# Returns details about a given list. 
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

class ListDetails(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListDetails Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListDetails, self).__init__(temboo_session, '/Library/Foursquare/Lists/ListDetails')


    def new_input_set(self):
        return ListDetailsInputSet()

    def _make_result_set(self, result, path):
        return ListDetailsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListDetailsChoreographyExecution(session, exec_id, path)

class ListDetailsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListDetails
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Number of results to return, up to 500.)
        """
        super(ListDetailsInputSet, self)._set_input('Limit', value)
    def set_ListID(self, value):
        """
        Set the value of the ListID input for this Choreo. ((required, string) The id of a user-created or followed list or an id for a tip or todo in the form of USER_ID/tips or USER_ID/todos. When getting tips or todos for the acting user, the user id is not required.)
        """
        super(ListDetailsInputSet, self)._set_input('ListID', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The Foursquare API OAuth token string.)
        """
        super(ListDetailsInputSet, self)._set_input('OauthToken', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Used to page through results.)
        """
        super(ListDetailsInputSet, self)._set_input('Offset', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(ListDetailsInputSet, self)._set_input('ResponseFormat', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) Identity of the user to get lists for. Defaults to "self" to get lists of the acting user.)
        """
        super(ListDetailsInputSet, self)._set_input('UserID', value)

class ListDetailsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListDetails Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class ListDetailsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListDetailsResultSet(response, path)
