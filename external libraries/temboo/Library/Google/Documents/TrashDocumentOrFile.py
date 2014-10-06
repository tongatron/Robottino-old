# -*- coding: utf-8 -*-

###############################################################################
#
# TrashDocumentOrFile
# Move the document or file you specify to the Google Documents trash.
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

class TrashDocumentOrFile(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the TrashDocumentOrFile Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(TrashDocumentOrFile, self).__init__(temboo_session, '/Library/Google/Documents/TrashDocumentOrFile')


    def new_input_set(self):
        return TrashDocumentOrFileInputSet()

    def _make_result_set(self, result, path):
        return TrashDocumentOrFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TrashDocumentOrFileChoreographyExecution(session, exec_id, path)

class TrashDocumentOrFileInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the TrashDocumentOrFile
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google account password.)
        """
        super(TrashDocumentOrFileInputSet, self)._set_input('Password', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((required, string) The title of the document or file to trash. Enclose in quotation marks for an exact, non-case-sensitive match.)
        """
        super(TrashDocumentOrFileInputSet, self)._set_input('Title', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your full Google email address e.g., martha.temboo@gmail.com.)
        """
        super(TrashDocumentOrFileInputSet, self)._set_input('Username', value)

class TrashDocumentOrFileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the TrashDocumentOrFile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from the Google Documents API.)
        """
        return self._output.get('Response', None)
    def get_ResourceID(self):
        """
        Retrieve the value for the "ResourceID" output from this Choreo execution. ((string) The resource ID for the document to trash as returned by Google.)
        """
        return self._output.get('ResourceID', None)

class TrashDocumentOrFileChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return TrashDocumentOrFileResultSet(response, path)
