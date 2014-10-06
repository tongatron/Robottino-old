# -*- coding: utf-8 -*-

###############################################################################
#
# SearchPeople
# Lets you search your Highrise CRM by specifying an email search criteria.
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

class SearchPeople(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchPeople Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SearchPeople, self).__init__(temboo_session, '/Library/Highrise/SearchPeople')


    def new_input_set(self):
        return SearchPeopleInputSet()

    def _make_result_set(self, result, path):
        return SearchPeopleResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchPeopleChoreographyExecution(session, exec_id, path)

class SearchPeopleInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchPeople
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountName(self, value):
        """
        Set the value of the AccountName input for this Choreo. ((required, string) A valid Highrise account name. This is the first part of the account's URL.)
        """
        super(SearchPeopleInputSet, self)._set_input('AccountName', value)
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((optional, string) Allows you to search by the city field in Highrise.)
        """
        super(SearchPeopleInputSet, self)._set_input('City', value)
    def set_Country(self, value):
        """
        Set the value of the Country input for this Choreo. ((optional, string) Allows you to search by the country field in Highrise.)
        """
        super(SearchPeopleInputSet, self)._set_input('Country', value)
    def set_EmailAddress(self, value):
        """
        Set the value of the EmailAddress input for this Choreo. ((optional, string) Allows you to search by the email address field in Highrise.)
        """
        super(SearchPeopleInputSet, self)._set_input('EmailAddress', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The Highrise account password. Use the value 'X' when specifying an API Key for the Username input.)
        """
        super(SearchPeopleInputSet, self)._set_input('Password', value)
    def set_Phone(self, value):
        """
        Set the value of the Phone input for this Choreo. ((optional, string) Allows you to search by the phone field in Highrise.)
        """
        super(SearchPeopleInputSet, self)._set_input('Phone', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) Allows you to search by the state field in Highrise.)
        """
        super(SearchPeopleInputSet, self)._set_input('State', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) A Highrise account username or API Key.)
        """
        super(SearchPeopleInputSet, self)._set_input('Username', value)
    def set_Zip(self, value):
        """
        Set the value of the Zip input for this Choreo. ((optional, string) Allows you to search by the ZIP field in Highrise.)
        """
        super(SearchPeopleInputSet, self)._set_input('Zip', value)

class SearchPeopleResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchPeople Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Highrise.)
        """
        return self._output.get('Response', None)

class SearchPeopleChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SearchPeopleResultSet(response, path)
