# -*- coding: utf-8 -*-

###############################################################################
#
# CreateVirtualMFADevice
# Creates a new virtual MFA device for the AWS account.
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

class CreateVirtualMFADevice(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateVirtualMFADevice Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateVirtualMFADevice, self).__init__(temboo_session, '/Library/Amazon/IAM/CreateVirtualMFADevice')


    def new_input_set(self):
        return CreateVirtualMFADeviceInputSet()

    def _make_result_set(self, result, path):
        return CreateVirtualMFADeviceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateVirtualMFADeviceChoreographyExecution(session, exec_id, path)

class CreateVirtualMFADeviceInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateVirtualMFADevice
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(CreateVirtualMFADeviceInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(CreateVirtualMFADeviceInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_Path(self, value):
        """
        Set the value of the Path input for this Choreo. ((optional, string) The path for the virtual MFA device. If it is not included, it defaults to a slash (/).)
        """
        super(CreateVirtualMFADeviceInputSet, self)._set_input('Path', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(CreateVirtualMFADeviceInputSet, self)._set_input('ResponseFormat', value)
    def set_VirtualMFADeviceName(self, value):
        """
        Set the value of the VirtualMFADeviceName input for this Choreo. ((required, string) The name of the virtual MFA device. Use with path to uniquely identify a virtual MFA device.)
        """
        super(CreateVirtualMFADeviceInputSet, self)._set_input('VirtualMFADeviceName', value)

class CreateVirtualMFADeviceResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateVirtualMFADevice Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class CreateVirtualMFADeviceChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateVirtualMFADeviceResultSet(response, path)
