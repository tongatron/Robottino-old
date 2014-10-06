# -*- coding: utf-8 -*-

###############################################################################
#
# CreateUser
# Creates a new user.
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

class CreateUser(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateUser Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateUser, self).__init__(temboo_session, '/Library/Zendesk/Users/CreateUser')


    def new_input_set(self):
        return CreateUserInputSet()

    def _make_result_set(self, result, path):
        return CreateUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateUserChoreographyExecution(session, exec_id, path)

class CreateUserInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateUser
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email address you use to login to your Zendesk account.)
        """
        super(CreateUserInputSet, self)._set_input('Email', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Zendesk password.)
        """
        super(CreateUserInputSet, self)._set_input('Password', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((required, string) Your Zendesk domain and subdomain (e.g., temboocare.zendesk.com).)
        """
        super(CreateUserInputSet, self)._set_input('Server', value)
    def set_UserData(self, value):
        """
        Set the value of the UserData input for this Choreo. ((required, json) A JSON-formatted string containing the user properties you wish to set.)
        """
        super(CreateUserInputSet, self)._set_input('UserData', value)

class CreateUserResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateUser Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) )
        """
        return self._output.get('Response', None)

class CreateUserChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateUserResultSet(response, path)
