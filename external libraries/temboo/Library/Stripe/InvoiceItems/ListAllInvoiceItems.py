# -*- coding: utf-8 -*-

###############################################################################
#
# ListAllInvoiceItems
# Returns a list of all invoice items or a list of invoice items for a specified customer.
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

class ListAllInvoiceItems(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListAllInvoiceItems Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListAllInvoiceItems, self).__init__(temboo_session, '/Library/Stripe/InvoiceItems/ListAllInvoiceItems')


    def new_input_set(self):
        return ListAllInvoiceItemsInputSet()

    def _make_result_set(self, result, path):
        return ListAllInvoiceItemsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListAllInvoiceItemsChoreographyExecution(session, exec_id, path)

class ListAllInvoiceItemsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListAllInvoiceItems
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        super(ListAllInvoiceItemsInputSet, self)._set_input('APIKey', value)
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) The limit of invoice items to be returned. Can range from 1 to 100. Defaults to 10.)
        """
        super(ListAllInvoiceItemsInputSet, self)._set_input('Count', value)
    def set_CustomerID(self, value):
        """
        Set the value of the CustomerID input for this Choreo. ((optional, string) The unique identifier of the customer whose invoice items to return. If not specified, all invoice items will be returned.)
        """
        super(ListAllInvoiceItemsInputSet, self)._set_input('CustomerID', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Stripe will return a list of invoice items starting at the specified offset. Defaults to 0.)
        """
        super(ListAllInvoiceItemsInputSet, self)._set_input('Offset', value)

class ListAllInvoiceItemsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListAllInvoiceItems Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)

class ListAllInvoiceItemsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListAllInvoiceItemsResultSet(response, path)
