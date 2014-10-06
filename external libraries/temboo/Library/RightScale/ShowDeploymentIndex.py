# -*- coding: utf-8 -*-

###############################################################################
#
# ShowDeploymentIndex
# Retrieve a list of server assets grouped within a particular RightScale Deployment ID. 
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

class ShowDeploymentIndex(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ShowDeploymentIndex Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ShowDeploymentIndex, self).__init__(temboo_session, '/Library/RightScale/ShowDeploymentIndex')


    def new_input_set(self):
        return ShowDeploymentIndexInputSet()

    def _make_result_set(self, result, path):
        return ShowDeploymentIndexResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ShowDeploymentIndexChoreographyExecution(session, exec_id, path)

class ShowDeploymentIndexInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ShowDeploymentIndex
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountID(self, value):
        """
        Set the value of the AccountID input for this Choreo. ((required, string) The RightScale Account ID.)
        """
        super(ShowDeploymentIndexInputSet, self)._set_input('AccountID', value)
    def set_DeploymentID(self, value):
        """
        Set the value of the DeploymentID input for this Choreo. ((required, integer) The DeploymentID to only list servers in this particular RightScale deployment.)
        """
        super(ShowDeploymentIndexInputSet, self)._set_input('DeploymentID', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The RightScale account password.)
        """
        super(ShowDeploymentIndexInputSet, self)._set_input('Password', value)
    def set_ServerSettings(self, value):
        """
        Set the value of the ServerSettings input for this Choreo. ((optional, string) Display additional information about this RightScale deployment. Set True to enable.)
        """
        super(ShowDeploymentIndexInputSet, self)._set_input('ServerSettings', value)
    def set_SubDomain(self, value):
        """
        Set the value of the SubDomain input for this Choreo. ((conditional, string) The Rightscale sub-domain appropriate for your Rightscale account. Defaults to "my" for legacy accounts. Other sub-domains include: jp-8 (Legacy Cloud Platform), us-3, us-4 (Unified Cloud Platform).)
        """
        super(ShowDeploymentIndexInputSet, self)._set_input('SubDomain', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The RightScale username.)
        """
        super(ShowDeploymentIndexInputSet, self)._set_input('Username', value)

class ShowDeploymentIndexResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ShowDeploymentIndex Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Rightscale in XML format.)
        """
        return self._output.get('Response', None)

class ShowDeploymentIndexChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ShowDeploymentIndexResultSet(response, path)
