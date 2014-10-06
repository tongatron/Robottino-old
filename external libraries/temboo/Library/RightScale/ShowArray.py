# -*- coding: utf-8 -*-

###############################################################################
#
# ShowArray
# Display a comrephensive set of information about the querried array such as: server(s) state information, array templates used, array state, etc.
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

class ShowArray(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ShowArray Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ShowArray, self).__init__(temboo_session, '/Library/RightScale/ShowArray')


    def new_input_set(self):
        return ShowArrayInputSet()

    def _make_result_set(self, result, path):
        return ShowArrayResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ShowArrayChoreographyExecution(session, exec_id, path)

class ShowArrayInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ShowArray
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountID(self, value):
        """
        Set the value of the AccountID input for this Choreo. ((required, string) The RightScale Account ID.)
        """
        super(ShowArrayInputSet, self)._set_input('AccountID', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The RightScale account password.)
        """
        super(ShowArrayInputSet, self)._set_input('Password', value)
    def set_ServerArrayID(self, value):
        """
        Set the value of the ServerArrayID input for this Choreo. ((required, integer) The ID of a server array.)
        """
        super(ShowArrayInputSet, self)._set_input('ServerArrayID', value)
    def set_SubDomain(self, value):
        """
        Set the value of the SubDomain input for this Choreo. ((conditional, string) The Rightscale sub-domain appropriate for your Rightscale account. Defaults to "my" for legacy accounts. Other sub-domains include: jp-8 (Legacy Cloud Platform), us-3, us-4 (Unified Cloud Platform).)
        """
        super(ShowArrayInputSet, self)._set_input('SubDomain', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The RightScale username.)
        """
        super(ShowArrayInputSet, self)._set_input('Username', value)

class ShowArrayResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ShowArray Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Rightscale in XML format.)
        """
        return self._output.get('Response', None)

class ShowArrayChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ShowArrayResultSet(response, path)
