# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveCoupon
# Retrieves a coupon with specified coupon id.
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

class RetrieveCoupon(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveCoupon Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RetrieveCoupon, self).__init__(temboo_session, '/Library/Stripe/Coupons/RetrieveCoupon')


    def new_input_set(self):
        return RetrieveCouponInputSet()

    def _make_result_set(self, result, path):
        return RetrieveCouponResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveCouponChoreographyExecution(session, exec_id, path)

class RetrieveCouponInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveCoupon
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        super(RetrieveCouponInputSet, self)._set_input('APIKey', value)
    def set_CouponID(self, value):
        """
        Set the value of the CouponID input for this Choreo. ((required, string) The unique identifier of the coupon you want to retrieve)
        """
        super(RetrieveCouponInputSet, self)._set_input('CouponID', value)

class RetrieveCouponResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveCoupon Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)

class RetrieveCouponChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RetrieveCouponResultSet(response, path)
