# -*- coding: utf-8 -*-

###############################################################################
#
# GetListsInProject
# Retrieves a list of To-do records that are in the given project.
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

class GetListsInProject(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetListsInProject Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetListsInProject, self).__init__(temboo_session, '/Library/Basecamp/GetListsInProject')


    def new_input_set(self):
        return GetListsInProjectInputSet()

    def _make_result_set(self, result, path):
        return GetListsInProjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetListsInProjectChoreographyExecution(session, exec_id, path)

class GetListsInProjectInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetListsInProject
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountName(self, value):
        """
        Set the value of the AccountName input for this Choreo. ((required, string) A valid Basecamp account name. This is the first part of the account's URL.)
        """
        super(GetListsInProjectInputSet, self)._set_input('AccountName', value)
    def set_Filter(self, value):
        """
        Set the value of the Filter input for this Choreo. ((optional, string) Specify “pending” to return To-Dos with uncompleted items, or “finished” to return To-Dos with no uncompleted items. Defaults to all lists.)
        """
        super(GetListsInProjectInputSet, self)._set_input('Filter', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The Basecamp account password. Use the value 'X' when specifying an API Key for the Username input.)
        """
        super(GetListsInProjectInputSet, self)._set_input('Password', value)
    def set_ProjectID(self, value):
        """
        Set the value of the ProjectID input for this Choreo. ((required, integer) The ID for the project that contains the To-Dos to retrieve.)
        """
        super(GetListsInProjectInputSet, self)._set_input('ProjectID', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) A Basecamp account username or API Key.)
        """
        super(GetListsInProjectInputSet, self)._set_input('Username', value)

class GetListsInProjectResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetListsInProject Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response returned from Basecamp.)
        """
        return self._output.get('Response', None)

class GetListsInProjectChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetListsInProjectResultSet(response, path)
