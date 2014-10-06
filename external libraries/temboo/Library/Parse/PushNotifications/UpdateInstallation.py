# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateInstallation
# Updates an existing installation object on Parse.
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

class UpdateInstallation(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateInstallation Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateInstallation, self).__init__(temboo_session, '/Library/Parse/PushNotifications/UpdateInstallation')


    def new_input_set(self):
        return UpdateInstallationInputSet()

    def _make_result_set(self, result, path):
        return UpdateInstallationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateInstallationChoreographyExecution(session, exec_id, path)

class UpdateInstallationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateInstallation
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Installation(self, value):
        """
        Set the value of the Installation input for this Choreo. ((required, json) A JSON string containing the installation data. See documentation for syntax examples.)
        """
        super(UpdateInstallationInputSet, self)._set_input('Installation', value)
    def set_ApplicationID(self, value):
        """
        Set the value of the ApplicationID input for this Choreo. ((required, string) The Application ID provided by Parse.)
        """
        super(UpdateInstallationInputSet, self)._set_input('ApplicationID', value)
    def set_ObjectID(self, value):
        """
        Set the value of the ObjectID input for this Choreo. ((required, string) The ID of the installation to update.)
        """
        super(UpdateInstallationInputSet, self)._set_input('ObjectID', value)
    def set_RESTAPIKey(self, value):
        """
        Set the value of the RESTAPIKey input for this Choreo. ((required, string) The REST API Key provided by Parse.)
        """
        super(UpdateInstallationInputSet, self)._set_input('RESTAPIKey', value)

class UpdateInstallationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateInstallation Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Parse.)
        """
        return self._output.get('Response', None)

class UpdateInstallationChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateInstallationResultSet(response, path)
