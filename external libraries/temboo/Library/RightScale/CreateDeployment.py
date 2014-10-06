# -*- coding: utf-8 -*-

###############################################################################
#
# CreateDeployment
# Create a RightScale Deployment.
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

class CreateDeployment(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateDeployment Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateDeployment, self).__init__(temboo_session, '/Library/RightScale/CreateDeployment')


    def new_input_set(self):
        return CreateDeploymentInputSet()

    def _make_result_set(self, result, path):
        return CreateDeploymentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateDeploymentChoreographyExecution(session, exec_id, path)

class CreateDeploymentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateDeployment
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountID(self, value):
        """
        Set the value of the AccountID input for this Choreo. ((required, integer) The RightScale Account ID.)
        """
        super(CreateDeploymentInputSet, self)._set_input('AccountID', value)
    def set_DeploymentDefaultEC2AvailabilityZone(self, value):
        """
        Set the value of the DeploymentDefaultEC2AvailabilityZone input for this Choreo. ((optional, string) The default EC2 availability zone for this deployment.)
        """
        super(CreateDeploymentInputSet, self)._set_input('DeploymentDefaultEC2AvailabilityZone', value)
    def set_DeploymentDefaultVPCSubnetHref(self, value):
        """
        Set the value of the DeploymentDefaultVPCSubnetHref input for this Choreo. ((optional, string) The href of the vpc subnet.)
        """
        super(CreateDeploymentInputSet, self)._set_input('DeploymentDefaultVPCSubnetHref', value)
    def set_DeploymentDescription(self, value):
        """
        Set the value of the DeploymentDescription input for this Choreo. ((optional, string) The deployment being created.)
        """
        super(CreateDeploymentInputSet, self)._set_input('DeploymentDescription', value)
    def set_DeploymentNickname(self, value):
        """
        Set the value of the DeploymentNickname input for this Choreo. ((required, string) The nickname of the deployment being created.)
        """
        super(CreateDeploymentInputSet, self)._set_input('DeploymentNickname', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The RightScale account password.)
        """
        super(CreateDeploymentInputSet, self)._set_input('Password', value)
    def set_SubDomain(self, value):
        """
        Set the value of the SubDomain input for this Choreo. ((conditional, string) The Rightscale sub-domain appropriate for your Rightscale account. Defaults to "my" for legacy accounts. Other sub-domains include: jp-8 (Legacy Cloud Platform), us-3, us-4 (Unified Cloud Platform).)
        """
        super(CreateDeploymentInputSet, self)._set_input('SubDomain', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The RightScale username.)
        """
        super(CreateDeploymentInputSet, self)._set_input('Username', value)

class CreateDeploymentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateDeployment Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Rightscale in XML format)
        """
        return self._output.get('Response', None)

class CreateDeploymentChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateDeploymentResultSet(response, path)
