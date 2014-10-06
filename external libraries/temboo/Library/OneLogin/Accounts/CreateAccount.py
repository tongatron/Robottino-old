# -*- coding: utf-8 -*-

###############################################################################
#
# CreateAccount
# Creates a new account.
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

class CreateAccount(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateAccount Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateAccount, self).__init__(temboo_session, '/Library/OneLogin/Accounts/CreateAccount')


    def new_input_set(self):
        return CreateAccountInputSet()

    def _make_result_set(self, result, path):
        return CreateAccountResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateAccountChoreographyExecution(session, exec_id, path)

class CreateAccountInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateAccount
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by OneLogin.)
        """
        super(CreateAccountInputSet, self)._set_input('APIKey', value)
    def set_AccountName(self, value):
        """
        Set the value of the AccountName input for this Choreo. ((required, string) The account name.)
        """
        super(CreateAccountInputSet, self)._set_input('AccountName', value)
    def set_Address(self, value):
        """
        Set the value of the Address input for this Choreo. ((optional, string) The street address for the new account.)
        """
        super(CreateAccountInputSet, self)._set_input('Address', value)
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((optional, string) The city associated with the address.)
        """
        super(CreateAccountInputSet, self)._set_input('City', value)
    def set_Country(self, value):
        """
        Set the value of the Country input for this Choreo. ((optional, string) The country associated with the address of the new account.)
        """
        super(CreateAccountInputSet, self)._set_input('Country', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email address for the new account.)
        """
        super(CreateAccountInputSet, self)._set_input('Email', value)
    def set_FirstName(self, value):
        """
        Set the value of the FirstName input for this Choreo. ((required, string) The first name on the new account.)
        """
        super(CreateAccountInputSet, self)._set_input('FirstName', value)
    def set_LastName(self, value):
        """
        Set the value of the LastName input for this Choreo. ((required, string) The last name on the new account.)
        """
        super(CreateAccountInputSet, self)._set_input('LastName', value)
    def set_Phone(self, value):
        """
        Set the value of the Phone input for this Choreo. ((optional, string) The phone number for the new account.)
        """
        super(CreateAccountInputSet, self)._set_input('Phone', value)
    def set_Plan(self, value):
        """
        Set the value of the Plan input for this Choreo. ((required, string) Indicates which plan the new account has (i.e. enterprise).)
        """
        super(CreateAccountInputSet, self)._set_input('Plan', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) The state associated with the address of the new account.)
        """
        super(CreateAccountInputSet, self)._set_input('State', value)
    def set_Zip(self, value):
        """
        Set the value of the Zip input for this Choreo. ((optional, string) The postal code associated with the address of the new account.)
        """
        super(CreateAccountInputSet, self)._set_input('Zip', value)

class CreateAccountResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateAccount Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from OneLogin.)
        """
        return self._output.get('Response', None)

class CreateAccountChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateAccountResultSet(response, path)
