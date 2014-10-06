# -*- coding: utf-8 -*-

###############################################################################
#
# CreateContact
# Create a new contact.
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

class CreateContact(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateContact Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateContact, self).__init__(temboo_session, '/Library/Google/Contacts/CreateContact')


    def new_input_set(self):
        return CreateContactInputSet()

    def _make_result_set(self, result, path):
        return CreateContactResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateContactChoreographyExecution(session, exec_id, path)

class CreateContactInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateContact
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        super(CreateContactInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The OAuth client ID provided by Google when you register your application.)
        """
        super(CreateContactInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The OAuth client secret provided by Google when you registered your application.)
        """
        super(CreateContactInputSet, self)._set_input('ClientSecret', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((conditional, string) The new contact's email address.)
        """
        super(CreateContactInputSet, self)._set_input('Email', value)
    def set_FirstName(self, value):
        """
        Set the value of the FirstName input for this Choreo. ((conditional, string) The new contact's first name.)
        """
        super(CreateContactInputSet, self)._set_input('FirstName', value)
    def set_LastName(self, value):
        """
        Set the value of the LastName input for this Choreo. ((conditional, string) The new contact's last name.)
        """
        super(CreateContactInputSet, self)._set_input('LastName', value)
    def set_Phone(self, value):
        """
        Set the value of the Phone input for this Choreo. ((optional, string) The phone number for the new contact. It's best to use the "(555) 123-4567" format.)
        """
        super(CreateContactInputSet, self)._set_input('Phone', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) The refresh token retrieved in the last step of the OAuth process. This is used when an access token is expired or not provided.)
        """
        super(CreateContactInputSet, self)._set_input('RefreshToken', value)

class CreateContactResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateContact Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from the API.)
        """
        return self._output.get('Response', None)
    def get_AccessToken(self):
        """
        Retrieve the value for the "AccessToken" output from this Choreo execution. ((optional, string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        return self._output.get('AccessToken', None)
    def get_ContactID(self):
        """
        Retrieve the value for the "ContactID" output from this Choreo execution. ((string) The unique ID supplied by Google for the new user.)
        """
        return self._output.get('ContactID', None)

class CreateContactChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateContactResultSet(response, path)
