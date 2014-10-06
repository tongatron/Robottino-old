# -*- coding: utf-8 -*-

###############################################################################
#
# PayInvoice
# Allows your application to attempt to collect payment on an invoice outside of the normal recurring payment schedule.
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

class PayInvoice(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PayInvoice Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(PayInvoice, self).__init__(temboo_session, '/Library/Stripe/Invoices/PayInvoice')


    def new_input_set(self):
        return PayInvoiceInputSet()

    def _make_result_set(self, result, path):
        return PayInvoiceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PayInvoiceChoreographyExecution(session, exec_id, path)

class PayInvoiceInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PayInvoice
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        super(PayInvoiceInputSet, self)._set_input('APIKey', value)
    def set_InvoiceID(self, value):
        """
        Set the value of the InvoiceID input for this Choreo. ((required, string) The id of the invoice to pay.)
        """
        super(PayInvoiceInputSet, self)._set_input('InvoiceID', value)

class PayInvoiceResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PayInvoice Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)

class PayInvoiceChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PayInvoiceResultSet(response, path)
