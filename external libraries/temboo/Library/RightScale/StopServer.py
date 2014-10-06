# -*- coding: utf-8 -*-

###############################################################################
#
# StopServer
# Stop a RightScale server instance. Optionally, this Choreo can also poll the stop process and verify server termination.
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

class StopServer(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the StopServer Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(StopServer, self).__init__(temboo_session, '/Library/RightScale/StopServer')


    def new_input_set(self):
        return StopServerInputSet()

    def _make_result_set(self, result, path):
        return StopServerResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return StopServerChoreographyExecution(session, exec_id, path)

class StopServerInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the StopServer
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountID(self, value):
        """
        Set the value of the AccountID input for this Choreo. ((required, integer) The RightScale Account ID.)
        """
        super(StopServerInputSet, self)._set_input('AccountID', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The RightScale account password.)
        """
        super(StopServerInputSet, self)._set_input('Password', value)
    def set_PollingTimeLimit(self, value):
        """
        Set the value of the PollingTimeLimit input for this Choreo. ((optional, integer) Server status polling.  Enable by specifying a time limit - in minutes - for the duration of the server state polling.)
        """
        super(StopServerInputSet, self)._set_input('PollingTimeLimit', value)
    def set_ServerID(self, value):
        """
        Set the value of the ServerID input for this Choreo. ((required, integer) The RightScale Server ID that is to be stopped.)
        """
        super(StopServerInputSet, self)._set_input('ServerID', value)
    def set_SubDomain(self, value):
        """
        Set the value of the SubDomain input for this Choreo. ((conditional, string) The Rightscale sub-domain appropriate for your Rightscale account. Defaults to "my" for legacy accounts. Other sub-domains include: jp-8 (Legacy Cloud Platform), us-3, us-4 (Unified Cloud Platform).)
        """
        super(StopServerInputSet, self)._set_input('SubDomain', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The RightScale username.)
        """
        super(StopServerInputSet, self)._set_input('Username', value)

class StopServerResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the StopServer Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Rightscale in XML format.)
        """
        return self._output.get('Response', None)
    def get_State(self):
        """
        Retrieve the value for the "State" output from this Choreo execution. ((string) The server 'state' parsed from the Rightscale response.)
        """
        return self._output.get('State', None)

class StopServerChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return StopServerResultSet(response, path)
