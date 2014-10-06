# -*- coding: utf-8 -*-

###############################################################################
#
# ListInstances
# Retrieves the list of Instance resources contained within the specified Zone.
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

class ListInstances(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListInstances Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListInstances, self).__init__(temboo_session, '/Library/Google/ComputeEngine/Instances/ListInstances')


    def new_input_set(self):
        return ListInstancesInputSet()

    def _make_result_set(self, result, path):
        return ListInstancesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListInstancesChoreographyExecution(session, exec_id, path)

class ListInstancesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListInstances
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        super(ListInstancesInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        super(ListInstancesInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        super(ListInstancesInputSet, self)._set_input('ClientSecret', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) Comma-seperated list of fields you want to include in the response.)
        """
        super(ListInstancesInputSet, self)._set_input('Fields', value)
    def set_Filter(self, value):
        """
        Set the value of the Filter input for this Choreo. ((optional, string) A filter expression for narrowing results in the form: {field_name} {comparison_string} {literal_string} (e.g. name eq testinstance). Comparison strings can be eq (equals) or ne (not equals).)
        """
        super(ListInstancesInputSet, self)._set_input('Filter', value)
    def set_MaxResults(self, value):
        """
        Set the value of the MaxResults input for this Choreo. ((optional, integer) The maximum number of results to return.)
        """
        super(ListInstancesInputSet, self)._set_input('MaxResults', value)
    def set_PageToken(self, value):
        """
        Set the value of the PageToken input for this Choreo. ((optional, string) The "nextPageToken" found in the response which is used to page through results.)
        """
        super(ListInstancesInputSet, self)._set_input('PageToken', value)
    def set_Project(self, value):
        """
        Set the value of the Project input for this Choreo. ((required, string) The ID of a Google Compute project.)
        """
        super(ListInstancesInputSet, self)._set_input('Project', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(ListInstancesInputSet, self)._set_input('RefreshToken', value)
    def set_Zone(self, value):
        """
        Set the value of the Zone input for this Choreo. ((required, string) The name of the zone associated with this request.)
        """
        super(ListInstancesInputSet, self)._set_input('Zone', value)

class ListInstancesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListInstances Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Google.)
        """
        return self._output.get('Response', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)

class ListInstancesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListInstancesResultSet(response, path)
