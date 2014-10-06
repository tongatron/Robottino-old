# -*- coding: utf-8 -*-

###############################################################################
#
# AddListRows
# Adds one or more rows to a worksheet in a Google spreadsheet using a simple XML file you provide.
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

class AddListRows(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddListRows Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(AddListRows, self).__init__(temboo_session, '/Library/Google/Spreadsheets/AddListRows')


    def new_input_set(self):
        return AddListRowsInputSet()

    def _make_result_set(self, result, path):
        return AddListRowsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddListRowsChoreographyExecution(session, exec_id, path)

class AddListRowsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddListRows
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_RowsetXML(self, value):
        """
        Set the value of the RowsetXML input for this Choreo. ((required, xml) The rows of data that you want to add to a worksheet in XML format. Your XML needs to be in the rowset/row schema described in the Choreo documentation.)
        """
        super(AddListRowsInputSet, self)._set_input('RowsetXML', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google password.)
        """
        super(AddListRowsInputSet, self)._set_input('Password', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml (the default) and json.)
        """
        super(AddListRowsInputSet, self)._set_input('ResponseFormat', value)
    def set_SpreadsheetKey(self, value):
        """
        Set the value of the SpreadsheetKey input for this Choreo. ((required, string) The unique key of the spreadsheet that contains the worksheet you want to add rows to.)
        """
        super(AddListRowsInputSet, self)._set_input('SpreadsheetKey', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your full Google email address e.g., martha.temboo@gmail.com.)
        """
        super(AddListRowsInputSet, self)._set_input('Username', value)
    def set_WorksheetId(self, value):
        """
        Set the value of the WorksheetId input for this Choreo. ((required, string) The unique ID of the worksheet that you want to add rows to.)
        """
        super(AddListRowsInputSet, self)._set_input('WorksheetId', value)

class AddListRowsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddListRows Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Google.)
        """
        return self._output.get('Response', None)

class AddListRowsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AddListRowsResultSet(response, path)
