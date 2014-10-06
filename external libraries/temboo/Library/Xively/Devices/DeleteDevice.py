# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteDevice
# Deletes the device matching the provided serial number.
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

class DeleteDevice(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteDevice Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteDevice, self).__init__(temboo_session, '/Library/Xively/Devices/DeleteDevice')


    def new_input_set(self):
        return DeleteDeviceInputSet()

    def _make_result_set(self, result, path):
        return DeleteDeviceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteDeviceChoreographyExecution(session, exec_id, path)

class DeleteDeviceInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteDevice
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Xively.)
        """
        super(DeleteDeviceInputSet, self)._set_input('APIKey', value)
    def set_ProductID(self, value):
        """
        Set the value of the ProductID input for this Choreo. ((required, string) The product ID for the device you would like to delete.)
        """
        super(DeleteDeviceInputSet, self)._set_input('ProductID', value)
    def set_SerialNumber(self, value):
        """
        Set the value of the SerialNumber input for this Choreo. ((required, string) The serial number for the device you would like to delete.)
        """
        super(DeleteDeviceInputSet, self)._set_input('SerialNumber', value)

class DeleteDeviceResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteDevice Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The response status code returned from Xively. For a successful deletion, the status code should be 200.)
        """
        return self._output.get('ResponseStatusCode', None)

class DeleteDeviceChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteDeviceResultSet(response, path)
