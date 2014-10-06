# -*- coding: utf-8 -*-

###############################################################################
#
# AuthorizeDBSecurityGroupIngress
# Allows restricted access to your database instance by adding EC2 Security Groups to the DBSecurityGroup or by specifying an allowed IP range.
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

class AuthorizeDBSecurityGroupIngress(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AuthorizeDBSecurityGroupIngress Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(AuthorizeDBSecurityGroupIngress, self).__init__(temboo_session, '/Library/Amazon/RDS/AuthorizeDBSecurityGroupIngress')


    def new_input_set(self):
        return AuthorizeDBSecurityGroupIngressInputSet()

    def _make_result_set(self, result, path):
        return AuthorizeDBSecurityGroupIngressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AuthorizeDBSecurityGroupIngressChoreographyExecution(session, exec_id, path)

class AuthorizeDBSecurityGroupIngressInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AuthorizeDBSecurityGroupIngress
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(AuthorizeDBSecurityGroupIngressInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(AuthorizeDBSecurityGroupIngressInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_CIDRIP(self, value):
        """
        Set the value of the CIDRIP input for this Choreo. ((conditional, string) IP range that should have access. Required unless EC2SecurityGroupName and EC2SecurityGroupOwnerId are used.)
        """
        super(AuthorizeDBSecurityGroupIngressInputSet, self)._set_input('CIDRIP', value)
    def set_DBSecurityGroupName(self, value):
        """
        Set the value of the DBSecurityGroupName input for this Choreo. ((required, string) A unique name for the security group you want to authorize.)
        """
        super(AuthorizeDBSecurityGroupIngressInputSet, self)._set_input('DBSecurityGroupName', value)
    def set_EC2SecurityGroupId(self, value):
        """
        Set the value of the EC2SecurityGroupId input for this Choreo. ((conditional, string) The ID of the EC2 security group to authorize. For VPC DB security groups, this is required. Otherwise, EC2SecurityGroupOwnerId and either EC2SecurityGroupName or EC2SecurityGroupId must be provided.)
        """
        super(AuthorizeDBSecurityGroupIngressInputSet, self)._set_input('EC2SecurityGroupId', value)
    def set_EC2SecurityGroupName(self, value):
        """
        Set the value of the EC2SecurityGroupName input for this Choreo. ((conditional, string) The EC2 security group to authorize. This and EC2SecurityGroupOwnerId are required if CIDRIP is not used.)
        """
        super(AuthorizeDBSecurityGroupIngressInputSet, self)._set_input('EC2SecurityGroupName', value)
    def set_EC2SecurityGroupOwnerId(self, value):
        """
        Set the value of the EC2SecurityGroupOwnerId input for this Choreo. ((conditional, string) The AWS account number for the security group owner. This and EC2SecurityGroupName are required if CIDRIP is not used.)
        """
        super(AuthorizeDBSecurityGroupIngressInputSet, self)._set_input('EC2SecurityGroupOwnerId', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the RDS endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(AuthorizeDBSecurityGroupIngressInputSet, self)._set_input('UserRegion', value)

class AuthorizeDBSecurityGroupIngressResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AuthorizeDBSecurityGroupIngress Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class AuthorizeDBSecurityGroupIngressChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AuthorizeDBSecurityGroupIngressResultSet(response, path)
