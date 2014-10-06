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
        super(CreateUser, self).__init__(temboo_session, '/Library/OneLogin/Users/CreateUser')


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
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by OneLogin.)
        """
        super(CreateUserInputSet, self)._set_input('APIKey', value)
    def set_Address(self, value):
        """
        Set the value of the Address input for this Choreo. ((conditional, string) The street address for the new account.)
        """
        super(CreateUserInputSet, self)._set_input('Address', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((conditional, string) The email address for the new user.)
        """
        super(CreateUserInputSet, self)._set_input('Email', value)
    def set_FirstName(self, value):
        """
        Set the value of the FirstName input for this Choreo. ((conditional, string) The first name of the new user.)
        """
        super(CreateUserInputSet, self)._set_input('FirstName', value)
    def set_GroupID(self, value):
        """
        Set the value of the GroupID input for this Choreo. ((optional, string) The group id associated with the new user.)
        """
        super(CreateUserInputSet, self)._set_input('GroupID', value)
    def set_LastName(self, value):
        """
        Set the value of the LastName input for this Choreo. ((conditional, string) The last name of the new user.)
        """
        super(CreateUserInputSet, self)._set_input('LastName', value)
    def set_OpenIDName(self, value):
        """
        Set the value of the OpenIDName input for this Choreo. ((conditional, string) The open id name.)
        """
        super(CreateUserInputSet, self)._set_input('OpenIDName', value)
    def set_Phone(self, value):
        """
        Set the value of the Phone input for this Choreo. ((conditional, string) The phone number of the new user.)
        """
        super(CreateUserInputSet, self)._set_input('Phone', value)

class CreateUserResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateUser Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from OneLogin.)
        """
        return self._output.get('Response', None)

class CreateUserChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateUserResultSet(response, path)
