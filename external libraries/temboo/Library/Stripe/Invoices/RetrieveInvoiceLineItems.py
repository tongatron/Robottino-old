# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveInvoiceLineItems
# Retrieves a full list of line items contained in an invoice.
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

class RetrieveInvoiceLineItems(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveInvoiceLineItems Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RetrieveInvoiceLineItems, self).__init__(temboo_session, '/Library/Stripe/Invoices/RetrieveInvoiceLineItems')


    def new_input_set(self):
        return RetrieveInvoiceLineItemsInputSet()

    def _make_result_set(self, result, path):
        return RetrieveInvoiceLineItemsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveInvoiceLineItemsChoreographyExecution(session, exec_id, path)

class RetrieveInvoiceLineItemsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveInvoiceLineItems
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        super(RetrieveInvoiceLineItemsInputSet, self)._set_input('APIKey', value)
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) The number of line items to return)
        """
        super(RetrieveInvoiceLineItemsInputSet, self)._set_input('Count', value)
    def set_CustomerID(self, value):
        """
        Set the value of the CustomerID input for this Choreo. ((optional, string) In the case of upcoming invoices, the customer of the upcoming invoice is required. In other cases it is ignored.)
        """
        super(RetrieveInvoiceLineItemsInputSet, self)._set_input('CustomerID', value)
    def set_InvoiceID(self, value):
        """
        Set the value of the InvoiceID input for this Choreo. ((required, string) The id of the invoice containing the line items to return)
        """
        super(RetrieveInvoiceLineItemsInputSet, self)._set_input('InvoiceID', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) The offset into the list of line items to start returning from, with 0 being the most recent)
        """
        super(RetrieveInvoiceLineItemsInputSet, self)._set_input('Offset', value)

class RetrieveInvoiceLineItemsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveInvoiceLineItems Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)

class RetrieveInvoiceLineItemsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RetrieveInvoiceLineItemsResultSet(response, path)
