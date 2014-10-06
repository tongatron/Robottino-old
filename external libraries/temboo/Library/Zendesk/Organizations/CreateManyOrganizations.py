# -*- coding: utf-8 -*-

###############################################################################
#
# CreateManyOrganizations
# Create multiple organizations with a single request. 
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

class CreateManyOrganizations(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateManyOrganizations Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateManyOrganizations, self).__init__(temboo_session, '/Library/Zendesk/Organizations/CreateManyOrganizations')


    def new_input_set(self):
        return CreateManyOrganizationsInputSet()

    def _make_result_set(self, result, path):
        return CreateManyOrganizationsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateManyOrganizationsChoreographyExecution(session, exec_id, path)

class CreateManyOrganizationsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateManyOrganizations
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_OrganizationData(self, value):
        """
        Set the value of the OrganizationData input for this Choreo. ((optional, json) A JSON-formatted string containing an array of organization properties you wish to set. This can used when you need to set multiple properties.)
        """
        super(CreateManyOrganizationsInputSet, self)._set_input('OrganizationData', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email address you use to login to your Zendesk account.)
        """
        super(CreateManyOrganizationsInputSet, self)._set_input('Email', value)
    def set_Names(self, value):
        """
        Set the value of the Names input for this Choreo. ((conditional, string) Comma-seperated list of up to 10  organization names to create.)
        """
        super(CreateManyOrganizationsInputSet, self)._set_input('Names', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Zendesk password.)
        """
        super(CreateManyOrganizationsInputSet, self)._set_input('Password', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((required, string) Your Zendesk domain and subdomain (e.g., temboocare.zendesk.com).)
        """
        super(CreateManyOrganizationsInputSet, self)._set_input('Server', value)

class CreateManyOrganizationsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateManyOrganizations Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Zendesk.)
        """
        return self._output.get('Response', None)

class CreateManyOrganizationsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateManyOrganizationsResultSet(response, path)
