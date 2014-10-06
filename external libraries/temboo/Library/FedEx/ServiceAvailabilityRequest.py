# -*- coding: utf-8 -*-

###############################################################################
#
# ServiceAvailabilityRequest
# Retrieves available shipping options and delivery dates for a specified origin and destination.
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

class ServiceAvailabilityRequest(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ServiceAvailabilityRequest Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ServiceAvailabilityRequest, self).__init__(temboo_session, '/Library/FedEx/ServiceAvailabilityRequest')


    def new_input_set(self):
        return ServiceAvailabilityRequestInputSet()

    def _make_result_set(self, result, path):
        return ServiceAvailabilityRequestResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ServiceAvailabilityRequestChoreographyExecution(session, exec_id, path)

class ServiceAvailabilityRequestInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ServiceAvailabilityRequest
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountNumber(self, value):
        """
        Set the value of the AccountNumber input for this Choreo. ((required, string) Your FedEx Account Number)
        """
        super(ServiceAvailabilityRequestInputSet, self)._set_input('AccountNumber', value)
    def set_AuthenticationKey(self, value):
        """
        Set the value of the AuthenticationKey input for this Choreo. ((required, string) The Production Authentication Key provided by FedEx Web Services)
        """
        super(ServiceAvailabilityRequestInputSet, self)._set_input('AuthenticationKey', value)
    def set_DestinationCountryCode(self, value):
        """
        Set the value of the DestinationCountryCode input for this Choreo. ((required, string) The destination country code to use as an input to the service availability request)
        """
        super(ServiceAvailabilityRequestInputSet, self)._set_input('DestinationCountryCode', value)
    def set_DestinationPostalCode(self, value):
        """
        Set the value of the DestinationPostalCode input for this Choreo. ((required, string) The destination postal code to use as an input to the service availability request)
        """
        super(ServiceAvailabilityRequestInputSet, self)._set_input('DestinationPostalCode', value)
    def set_MeterNumber(self, value):
        """
        Set the value of the MeterNumber input for this Choreo. ((required, string) The Production Meter Number provided by FedEx Web Services)
        """
        super(ServiceAvailabilityRequestInputSet, self)._set_input('MeterNumber', value)
    def set_OriginCountryCode(self, value):
        """
        Set the value of the OriginCountryCode input for this Choreo. ((required, string) The origin country code to use as an input to the service availability request)
        """
        super(ServiceAvailabilityRequestInputSet, self)._set_input('OriginCountryCode', value)
    def set_OriginPostalCode(self, value):
        """
        Set the value of the OriginPostalCode input for this Choreo. ((required, string) The origin country code to use as an input to the service availability request)
        """
        super(ServiceAvailabilityRequestInputSet, self)._set_input('OriginPostalCode', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The Production Password provided by FedEx Web Services)
        """
        super(ServiceAvailabilityRequestInputSet, self)._set_input('Password', value)
    def set_ShipDate(self, value):
        """
        Set the value of the ShipDate input for this Choreo. ((required, date) The date to use for the service availability request (epoch timestamp in milliseconds or formatted like yyyy-MM-dd))
        """
        super(ServiceAvailabilityRequestInputSet, self)._set_input('ShipDate', value)

class ServiceAvailabilityRequestResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ServiceAvailabilityRequest Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from FedEx)
        """
        return self._output.get('Response', None)

class ServiceAvailabilityRequestChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ServiceAvailabilityRequestResultSet(response, path)
