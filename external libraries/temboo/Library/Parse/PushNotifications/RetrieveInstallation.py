# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveInstallation
# Retrieves the contents of an installation object.
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

class RetrieveInstallation(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveInstallation Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RetrieveInstallation, self).__init__(temboo_session, '/Library/Parse/PushNotifications/RetrieveInstallation')


    def new_input_set(self):
        return RetrieveInstallationInputSet()

    def _make_result_set(self, result, path):
        return RetrieveInstallationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveInstallationChoreographyExecution(session, exec_id, path)

class RetrieveInstallationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveInstallation
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ObjectID(self, value):
        """
        Set the value of the ObjectID input for this Choreo. ((required, string) The ID of the installation to retrieve.)
        """
        super(RetrieveInstallationInputSet, self)._set_input('ObjectID', value)
    def set_ApplicationID(self, value):
        """
        Set the value of the ApplicationID input for this Choreo. ((required, string) The Application ID provided by Parse.)
        """
        super(RetrieveInstallationInputSet, self)._set_input('ApplicationID', value)
    def set_RESTAPIKey(self, value):
        """
        Set the value of the RESTAPIKey input for this Choreo. ((required, string) The REST API Key provided by Parse.)
        """
        super(RetrieveInstallationInputSet, self)._set_input('RESTAPIKey', value)

class RetrieveInstallationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveInstallation Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Parse.)
        """
        return self._output.get('Response', None)

class RetrieveInstallationChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RetrieveInstallationResultSet(response, path)
