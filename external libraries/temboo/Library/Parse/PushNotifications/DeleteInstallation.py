# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteInstallation
# Deletes an installation object.
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

class DeleteInstallation(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteInstallation Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteInstallation, self).__init__(temboo_session, '/Library/Parse/PushNotifications/DeleteInstallation')


    def new_input_set(self):
        return DeleteInstallationInputSet()

    def _make_result_set(self, result, path):
        return DeleteInstallationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteInstallationChoreographyExecution(session, exec_id, path)

class DeleteInstallationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteInstallation
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ObjectID(self, value):
        """
        Set the value of the ObjectID input for this Choreo. ((required, string) The ID of the installation to delete.)
        """
        super(DeleteInstallationInputSet, self)._set_input('ObjectID', value)
    def set_ApplicationID(self, value):
        """
        Set the value of the ApplicationID input for this Choreo. ((required, string) The Application ID provided by Parse.)
        """
        super(DeleteInstallationInputSet, self)._set_input('ApplicationID', value)
    def set_MasterKey(self, value):
        """
        Set the value of the MasterKey input for this Choreo. ((required, string) The Master Key provided by Parse.)
        """
        super(DeleteInstallationInputSet, self)._set_input('MasterKey', value)

class DeleteInstallationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteInstallation Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Parse.)
        """
        return self._output.get('Response', None)

class DeleteInstallationChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteInstallationResultSet(response, path)
