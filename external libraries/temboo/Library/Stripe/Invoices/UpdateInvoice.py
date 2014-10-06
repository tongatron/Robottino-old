# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateInvoice
# Updates an existing invoice.
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

class UpdateInvoice(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateInvoice Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateInvoice, self).__init__(temboo_session, '/Library/Stripe/Invoices/UpdateInvoice')


    def new_input_set(self):
        return UpdateInvoiceInputSet()

    def _make_result_set(self, result, path):
        return UpdateInvoiceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateInvoiceChoreographyExecution(session, exec_id, path)

class UpdateInvoiceInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateInvoice
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        super(UpdateInvoiceInputSet, self)._set_input('APIKey', value)
    def set_Closed(self, value):
        """
        Set the value of the Closed input for this Choreo. ((conditional, boolean) Whether or not the invoice should be closed or not. To close an invoice, set this to "true".)
        """
        super(UpdateInvoiceInputSet, self)._set_input('Closed', value)
    def set_InvoiceID(self, value):
        """
        Set the value of the InvoiceID input for this Choreo. ((required, string) The id of the invoice to update.)
        """
        super(UpdateInvoiceInputSet, self)._set_input('InvoiceID', value)

class UpdateInvoiceResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateInvoice Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)

class UpdateInvoiceChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateInvoiceResultSet(response, path)
