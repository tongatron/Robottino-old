# -*- coding: utf-8 -*-

###############################################################################
#
# DetachVolume
# Detaches an Amazon EBS volume from an instance.
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

class DetachVolume(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DetachVolume Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DetachVolume, self).__init__(temboo_session, '/Library/Amazon/EC2/DetachVolume')


    def new_input_set(self):
        return DetachVolumeInputSet()

    def _make_result_set(self, result, path):
        return DetachVolumeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DetachVolumeChoreographyExecution(session, exec_id, path)

class DetachVolumeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DetachVolume
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(DetachVolumeInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(DetachVolumeInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_Device(self, value):
        """
        Set the value of the Device input for this Choreo. ((optional, string) The device name.)
        """
        super(DetachVolumeInputSet, self)._set_input('Device', value)
    def set_Force(self, value):
        """
        Set the value of the Force input for this Choreo. ((required, boolean) Forces detachment if the previous detachment attempt did not occur cleanly. Use this option only as a last resort to detach a volume from a failed instance. Defaults to false.)
        """
        super(DetachVolumeInputSet, self)._set_input('Force', value)
    def set_InstanceId(self, value):
        """
        Set the value of the InstanceId input for this Choreo. ((optional, string) The ID of the instance.)
        """
        super(DetachVolumeInputSet, self)._set_input('InstanceId', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(DetachVolumeInputSet, self)._set_input('ResponseFormat', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the EC2 endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(DetachVolumeInputSet, self)._set_input('UserRegion', value)
    def set_VolumeId(self, value):
        """
        Set the value of the VolumeId input for this Choreo. ((required, string) The ID of the volume.)
        """
        super(DetachVolumeInputSet, self)._set_input('VolumeId', value)

class DetachVolumeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DetachVolume Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class DetachVolumeChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DetachVolumeResultSet(response, path)
