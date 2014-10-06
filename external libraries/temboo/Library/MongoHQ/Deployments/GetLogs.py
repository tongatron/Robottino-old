# -*- coding: utf-8 -*-

###############################################################################
#
# GetLogs
# Retrieves logs from a particular deployment in your account.
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

class GetLogs(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetLogs Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetLogs, self).__init__(temboo_session, '/Library/MongoHQ/Deployments/GetLogs')


    def new_input_set(self):
        return GetLogsInputSet()

    def _make_result_set(self, result, path):
        return GetLogsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLogsChoreographyExecution(session, exec_id, path)

class GetLogsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetLogs
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIToken(self, value):
        """
        Set the value of the APIToken input for this Choreo. ((required, string) The API Token provided by MongoHQ.)
        """
        super(GetLogsInputSet, self)._set_input('APIToken', value)
    def set_DeploymentName(self, value):
        """
        Set the value of the DeploymentName input for this Choreo. ((required, string) The domain and port of the server (e.g., rose.mongohq.com:9000).)
        """
        super(GetLogsInputSet, self)._set_input('DeploymentName', value)

class GetLogsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetLogs Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from MongoHQ.)
        """
        return self._output.get('Response', None)

class GetLogsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetLogsResultSet(response, path)
