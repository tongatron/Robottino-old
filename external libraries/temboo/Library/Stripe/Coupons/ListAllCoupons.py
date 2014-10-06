# -*- coding: utf-8 -*-

###############################################################################
#
# ListAllCoupons
# Retrieves a a list of your coupons.
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

class ListAllCoupons(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListAllCoupons Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListAllCoupons, self).__init__(temboo_session, '/Library/Stripe/Coupons/ListAllCoupons')


    def new_input_set(self):
        return ListAllCouponsInputSet()

    def _make_result_set(self, result, path):
        return ListAllCouponsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListAllCouponsChoreographyExecution(session, exec_id, path)

class ListAllCouponsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListAllCoupons
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        super(ListAllCouponsInputSet, self)._set_input('APIKey', value)
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) A limit on the number of coupons to be returned. Valid values are 1 through 100.)
        """
        super(ListAllCouponsInputSet, self)._set_input('Count', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) An offset into your coupons array. The API will return the requested number of coupons starting at that the specified offset.)
        """
        super(ListAllCouponsInputSet, self)._set_input('Offset', value)

class ListAllCouponsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListAllCoupons Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)

class ListAllCouponsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListAllCouponsResultSet(response, path)
