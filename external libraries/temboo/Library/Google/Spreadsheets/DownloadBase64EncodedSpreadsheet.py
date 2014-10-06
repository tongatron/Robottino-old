# -*- coding: utf-8 -*-

###############################################################################
#
# DownloadBase64EncodedSpreadsheet
# Downloads a document with the title you specify, and returns the content as Base64 encoded data.
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

class DownloadBase64EncodedSpreadsheet(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DownloadBase64EncodedSpreadsheet Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DownloadBase64EncodedSpreadsheet, self).__init__(temboo_session, '/Library/Google/Spreadsheets/DownloadBase64EncodedSpreadsheet')


    def new_input_set(self):
        return DownloadBase64EncodedSpreadsheetInputSet()

    def _make_result_set(self, result, path):
        return DownloadBase64EncodedSpreadsheetResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DownloadBase64EncodedSpreadsheetChoreographyExecution(session, exec_id, path)

class DownloadBase64EncodedSpreadsheetInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DownloadBase64EncodedSpreadsheet
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Format(self, value):
        """
        Set the value of the Format input for this Choreo. ((optional, string) The format you want to export the spreadsheet to, such as "txt" or "pdf". The default download format is "txt".)
        """
        super(DownloadBase64EncodedSpreadsheetInputSet, self)._set_input('Format', value)
    def set_Link(self, value):
        """
        Set the value of the Link input for this Choreo. ((optional, string) The entry's resource URL found in the link element of the entry. Required if Title is not specified.)
        """
        super(DownloadBase64EncodedSpreadsheetInputSet, self)._set_input('Link', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google account password.)
        """
        super(DownloadBase64EncodedSpreadsheetInputSet, self)._set_input('Password', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((conditional, string) The title of the document to download. Required if the source Link is not specifed.)
        """
        super(DownloadBase64EncodedSpreadsheetInputSet, self)._set_input('Title', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your full Google email address e.g., martha.temboo@gmail.com.)
        """
        super(DownloadBase64EncodedSpreadsheetInputSet, self)._set_input('Username', value)

class DownloadBase64EncodedSpreadsheetResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DownloadBase64EncodedSpreadsheet Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_FileContents(self):
        """
        Retrieve the value for the "FileContents" output from this Choreo execution. ((string) The Base64 encoded file content of the downloaded file.)
        """
        return self._output.get('FileContents', None)

class DownloadBase64EncodedSpreadsheetChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DownloadBase64EncodedSpreadsheetResultSet(response, path)
