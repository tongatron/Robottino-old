# -*- coding: utf-8 -*-

###############################################################################
#
# TerminateArrayInstances
# Terminate an array instance.

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

class TerminateArrayInstances(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the TerminateArrayInstances Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(TerminateArrayInstances, self).__init__(temboo_session, '/Library/RightScale/TerminateArrayInstances')


    def new_input_set(self):
        return TerminateArrayInstancesInputSet()

    def _make_result_set(self, result, path):
        return TerminateArrayInstancesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TerminateArrayInstancesChoreographyExecution(session, exec_id, path)

class TerminateArrayInstancesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the TerminateArrayInstances
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountID(self, value):
        """
        Set the value of the AccountID input for this Choreo. ((required, string) The RightScale Account ID.)
        """
        super(TerminateArrayInstancesInputSet, self)._set_input('AccountID', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The RightScale account password.)
        """
        super(TerminateArrayInstancesInputSet, self)._set_input('Password', value)
    def set_ServerArrayID(self, value):
        """
        Set the value of the ServerArrayID input for this Choreo. ((required, integer) The ID of a server array.)
        """
        super(TerminateArrayInstancesInputSet, self)._set_input('ServerArrayID', value)
    def set_SubDomain(self, value):
        """
        Set the value of the SubDomain input for this Choreo. ((conditional, string) The Rightscale sub-domain appropriate for your Rightscale account. Defaults to "my" for legacy accounts. Other sub-domains include: jp-8 (Legacy Cloud Platform), us-3, us-4 (Unified Cloud Platform).)
        """
        super(TerminateArrayInstancesInputSet, self)._set_input('SubDomain', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The RightScale username.)
        """
        super(TerminateArrayInstancesInputSet, self)._set_input('Username', value)

class TerminateArrayInstancesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the TerminateArrayInstances Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Rightscale in XML format.)
        """
        return self._output.get('Response', None)

class TerminateArrayInstancesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return TerminateArrayInstancesResultSet(response, path)
