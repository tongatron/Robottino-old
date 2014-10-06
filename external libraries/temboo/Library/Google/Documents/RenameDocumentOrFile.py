# -*- coding: utf-8 -*-

###############################################################################
#
# RenameDocumentOrFile
# Rename a document or file with the new title you specify.
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

class RenameDocumentOrFile(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RenameDocumentOrFile Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RenameDocumentOrFile, self).__init__(temboo_session, '/Library/Google/Documents/RenameDocumentOrFile')


    def new_input_set(self):
        return RenameDocumentOrFileInputSet()

    def _make_result_set(self, result, path):
        return RenameDocumentOrFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RenameDocumentOrFileChoreographyExecution(session, exec_id, path)

class RenameDocumentOrFileInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RenameDocumentOrFile
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_NewTitle(self, value):
        """
        Set the value of the NewTitle input for this Choreo. ((required, string) The new title for the document. It will appear exactly as you type it, so be sure to use the proper capitalization.)
        """
        super(RenameDocumentOrFileInputSet, self)._set_input('NewTitle', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google account password.)
        """
        super(RenameDocumentOrFileInputSet, self)._set_input('Password', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((required, string) The title of the document to rename.)
        """
        super(RenameDocumentOrFileInputSet, self)._set_input('Title', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your full Google email address e.g., martha.temboo@gmail.com.)
        """
        super(RenameDocumentOrFileInputSet, self)._set_input('Username', value)

class RenameDocumentOrFileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RenameDocumentOrFile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from the Google Documents API.)
        """
        return self._output.get('Response', None)
    def get_EditLink(self):
        """
        Retrieve the value for the "EditLink" output from this Choreo execution. ((string) The edit link URL for the document to rename, parsed from the Google response.)
        """
        return self._output.get('EditLink', None)

class RenameDocumentOrFileChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RenameDocumentOrFileResultSet(response, path)
