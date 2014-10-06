# -*- coding: utf-8 -*-

###############################################################################
#
# CreateServerXMLInput
# Creates a RightScale server instance using a given XML template.
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

class CreateServerXMLInput(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateServerXMLInput Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateServerXMLInput, self).__init__(temboo_session, '/Library/RightScale/CreateServerXMLInput')


    def new_input_set(self):
        return CreateServerXMLInputInputSet()

    def _make_result_set(self, result, path):
        return CreateServerXMLInputResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateServerXMLInputChoreographyExecution(session, exec_id, path)

class CreateServerXMLInputInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateServerXMLInput
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ServerParameters(self, value):
        """
        Set the value of the ServerParameters input for this Choreo. ((required, xml) The XML file containing the required parameters for the server creation. See documentation for XML schema.)
        """
        super(CreateServerXMLInputInputSet, self)._set_input('ServerParameters', value)
    def set_ARIImage(self, value):
        """
        Set the value of the ARIImage input for this Choreo. ((required, string) The URL to the ARI Image.)
        """
        super(CreateServerXMLInputInputSet, self)._set_input('ARIImage', value)
    def set_AccountID(self, value):
        """
        Set the value of the AccountID input for this Choreo. ((required, integer) The Account ID obtained from RightScale.)
        """
        super(CreateServerXMLInputInputSet, self)._set_input('AccountID', value)
    def set_CloudID(self, value):
        """
        Set the value of the CloudID input for this Choreo. ((required, integer) The cloud region identifier. If undefined, the default is: 1 (us-east).)
        """
        super(CreateServerXMLInputInputSet, self)._set_input('CloudID', value)
    def set_EC2AvailabilityZone(self, value):
        """
        Set the value of the EC2AvailabilityZone input for this Choreo. ((optional, any) The  EC2 availablity zone, for example: us-east-1a, or any.  Do not set, if also passing the vpc_subnet_href parameter.)
        """
        super(CreateServerXMLInputInputSet, self)._set_input('EC2AvailabilityZone', value)
    def set_EC2Image(self, value):
        """
        Set the value of the EC2Image input for this Choreo. ((required, string) The URL to AMI image.)
        """
        super(CreateServerXMLInputInputSet, self)._set_input('EC2Image', value)
    def set_EC2SSHKeyHref(self, value):
        """
        Set the value of the EC2SSHKeyHref input for this Choreo. ((optional, any) The URL to the SSH Key.)
        """
        super(CreateServerXMLInputInputSet, self)._set_input('EC2SSHKeyHref', value)
    def set_EC2SecurityGroupsHref(self, value):
        """
        Set the value of the EC2SecurityGroupsHref input for this Choreo. ((optional, any) The URL(s) to security group(s). Do not set, if also passing the vpc_subnet_href parameter.)
        """
        super(CreateServerXMLInputInputSet, self)._set_input('EC2SecurityGroupsHref', value)
    def set_InstanceType(self, value):
        """
        Set the value of the InstanceType input for this Choreo. ((optional, any) The AWS instance type: small, medium, etc.)
        """
        super(CreateServerXMLInputInputSet, self)._set_input('InstanceType', value)
    def set_MaxSpotPrice(self, value):
        """
        Set the value of the MaxSpotPrice input for this Choreo. ((required, integer) The maximum price (a dollar value) dollars) per hour for the spot server.)
        """
        super(CreateServerXMLInputInputSet, self)._set_input('MaxSpotPrice', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The RightScale account password.)
        """
        super(CreateServerXMLInputInputSet, self)._set_input('Password', value)
    def set_Pricing(self, value):
        """
        Set the value of the Pricing input for this Choreo. ((required, string) AWS pricing.  Specify on_demand, or spot.)
        """
        super(CreateServerXMLInputInputSet, self)._set_input('Pricing', value)
    def set_ServerDeployment(self, value):
        """
        Set the value of the ServerDeployment input for this Choreo. ((optional, any) The URL of the deployment that this server wil be added to.)
        """
        super(CreateServerXMLInputInputSet, self)._set_input('ServerDeployment', value)
    def set_ServerNickname(self, value):
        """
        Set the value of the ServerNickname input for this Choreo. ((optional, any) The nickname for the server being created.)
        """
        super(CreateServerXMLInputInputSet, self)._set_input('ServerNickname', value)
    def set_ServerTemplate(self, value):
        """
        Set the value of the ServerTemplate input for this Choreo. ((optional, any) The URL to a server template.)
        """
        super(CreateServerXMLInputInputSet, self)._set_input('ServerTemplate', value)
    def set_SubDomain(self, value):
        """
        Set the value of the SubDomain input for this Choreo. ((conditional, string) The Rightscale sub-domain appropriate for your Rightscale account. Defaults to "my" for legacy accounts. Other sub-domains include: jp-8 (Legacy Cloud Platform), us-3, us-4 (Unified Cloud Platform).)
        """
        super(CreateServerXMLInputInputSet, self)._set_input('SubDomain', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The RightScale username.)
        """
        super(CreateServerXMLInputInputSet, self)._set_input('Username', value)
    def set_VPCSubnet(self, value):
        """
        Set the value of the VPCSubnet input for this Choreo. ((required, string) The href to the VPC subnet)
        """
        super(CreateServerXMLInputInputSet, self)._set_input('VPCSubnet', value)

class CreateServerXMLInputResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateServerXMLInput Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Rightscale in XML format.)
        """
        return self._output.get('Response', None)

class CreateServerXMLInputChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateServerXMLInputResultSet(response, path)
