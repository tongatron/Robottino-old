# -*- coding: utf-8 -*-

###############################################################################
#
# ListTrashedSpreadsheets
# Lists all the spreadsheets that have been "trashed" from a user's Zoho Sheet Account.
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

class ListTrashedSpreadsheets(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListTrashedSpreadsheets Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListTrashedSpreadsheets, self).__init__(temboo_session, '/Library/Zoho/Sheet/ListTrashedSpreadsheets')


    def new_input_set(self):
        return ListTrashedSpreadsheetsInputSet()

    def _make_result_set(self, result, path):
        return ListTrashedSpreadsheetsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListTrashedSpreadsheetsChoreographyExecution(session, exec_id, path)

class ListTrashedSpreadsheetsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListTrashedSpreadsheets
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Zoho)
        """
        super(ListTrashedSpreadsheetsInputSet, self)._set_input('APIKey', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Sets the number of documents to be listed.)
        """
        super(ListTrashedSpreadsheetsInputSet, self)._set_input('Limit', value)
    def set_LoginID(self, value):
        """
        Set the value of the LoginID input for this Choreo. ((required, string) Your Zoho username (or login id))
        """
        super(ListTrashedSpreadsheetsInputSet, self)._set_input('LoginID', value)
    def set_OrderBy(self, value):
        """
        Set the value of the OrderBy input for this Choreo. ((optional, string) Order documents by createdTime, lastModifiedTime or name.)
        """
        super(ListTrashedSpreadsheetsInputSet, self)._set_input('OrderBy', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Zoho password)
        """
        super(ListTrashedSpreadsheetsInputSet, self)._set_input('Password', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to xml.)
        """
        super(ListTrashedSpreadsheetsInputSet, self)._set_input('ResponseFormat', value)
    def set_SortOrder(self, value):
        """
        Set the value of the SortOrder input for this Choreo. ((optional, string) Sorting order: asc or desc. Default sort order is set to ascending.)
        """
        super(ListTrashedSpreadsheetsInputSet, self)._set_input('SortOrder', value)
    def set_StartFrom(self, value):
        """
        Set the value of the StartFrom input for this Choreo. ((optional, integer) Sets the initial document number from which the documents will be listed.)
        """
        super(ListTrashedSpreadsheetsInputSet, self)._set_input('StartFrom', value)

class ListTrashedSpreadsheetsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListTrashedSpreadsheets Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Zoho. Corresponds to the ResponseFormat input. Defaults to XML.)
        """
        return self._output.get('Response', None)

class ListTrashedSpreadsheetsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListTrashedSpreadsheetsResultSet(response, path)
