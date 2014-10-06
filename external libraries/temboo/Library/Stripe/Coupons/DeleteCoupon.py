# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteCoupon
# Deletes a specified coupon.
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

class DeleteCoupon(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteCoupon Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteCoupon, self).__init__(temboo_session, '/Library/Stripe/Coupons/DeleteCoupon')


    def new_input_set(self):
        return DeleteCouponInputSet()

    def _make_result_set(self, result, path):
        return DeleteCouponResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteCouponChoreographyExecution(session, exec_id, path)

class DeleteCouponInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteCoupon
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        super(DeleteCouponInputSet, self)._set_input('APIKey', value)
    def set_CouponID(self, value):
        """
        Set the value of the CouponID input for this Choreo. ((required, string) The unique identifier of the coupon you wish to delete)
        """
        super(DeleteCouponInputSet, self)._set_input('CouponID', value)

class DeleteCouponResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteCoupon Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)

class DeleteCouponChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteCouponResultSet(response, path)
