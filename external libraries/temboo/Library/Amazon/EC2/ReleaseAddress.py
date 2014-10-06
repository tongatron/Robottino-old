# -*- coding: utf-8 -*-

###############################################################################
#
# ReleaseAddress
# Releases an Elastic IP address allocated to your account.
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

class ReleaseAddress(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ReleaseAddress Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ReleaseAddress, self).__init__(temboo_session, '/Library/Amazon/EC2/ReleaseAddress')


    def new_input_set(self):
        return ReleaseAddressInputSet()

    def _make_result_set(self, result, path):
        return ReleaseAddressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ReleaseAddressChoreographyExecution(session, exec_id, path)

class ReleaseAddressInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ReleaseAddress
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(ReleaseAddressInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(ReleaseAddressInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_AllocationId(self, value):
        """
        Set the value of the AllocationId input for this Choreo. ((conditional, string) [EC2-VPC] The allocation ID that AWS provided when you allocated the address for use with a VPC.)
        """
        super(ReleaseAddressInputSet, self)._set_input('AllocationId', value)
    def set_PublicIp(self, value):
        """
        Set the value of the PublicIp input for this Choreo. ((conditional, string) [EC2-Classic] The Elastic IP address.)
        """
        super(ReleaseAddressInputSet, self)._set_input('PublicIp', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(ReleaseAddressInputSet, self)._set_input('ResponseFormat', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the EC2 endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(ReleaseAddressInputSet, self)._set_input('UserRegion', value)

class ReleaseAddressResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ReleaseAddress Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class ReleaseAddressChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ReleaseAddressResultSet(response, path)
