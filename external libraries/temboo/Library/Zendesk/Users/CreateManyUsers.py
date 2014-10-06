# -*- coding: utf-8 -*-

###############################################################################
#
# CreateManyUsers
# Creates many new users at one time.
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

class CreateManyUsers(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateManyUsers Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateManyUsers, self).__init__(temboo_session, '/Library/Zendesk/Users/CreateManyUsers')


    def new_input_set(self):
        return CreateManyUsersInputSet()

    def _make_result_set(self, result, path):
        return CreateManyUsersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateManyUsersChoreographyExecution(session, exec_id, path)

class CreateManyUsersInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateManyUsers
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email address you use to login to your Zendesk account.)
        """
        super(CreateManyUsersInputSet, self)._set_input('Email', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Zendesk password.)
        """
        super(CreateManyUsersInputSet, self)._set_input('Password', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((required, string) Your Zendesk domain and subdomain (e.g., temboocare.zendesk.com).)
        """
        super(CreateManyUsersInputSet, self)._set_input('Server', value)
    def set_Users(self, value):
        """
        Set the value of the Users input for this Choreo. ((required, json) A JSON-formatted string containing an array of user properties you wish to set.)
        """
        super(CreateManyUsersInputSet, self)._set_input('Users', value)

class CreateManyUsersResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateManyUsers Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) )
        """
        return self._output.get('Response', None)

class CreateManyUsersChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateManyUsersResultSet(response, path)
