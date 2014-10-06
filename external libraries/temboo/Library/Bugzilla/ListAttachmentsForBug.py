# -*- coding: utf-8 -*-

###############################################################################
#
# ListAttachmentsForBug
# List attachments associated with a specifig Bug ID.
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

class ListAttachmentsForBug(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListAttachmentsForBug Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListAttachmentsForBug, self).__init__(temboo_session, '/Library/Bugzilla/ListAttachmentsForBug')


    def new_input_set(self):
        return ListAttachmentsForBugInputSet()

    def _make_result_set(self, result, path):
        return ListAttachmentsForBugResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListAttachmentsForBugChoreographyExecution(session, exec_id, path)

class ListAttachmentsForBugInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListAttachmentsForBug
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AttachmentsWithData(self, value):
        """
        Set the value of the AttachmentsWithData input for this Choreo. ((optional, integer) Enter 1 to obtain full bug attachments data.  If null, only attachments fields will be returned with no associated data.)
        """
        super(ListAttachmentsForBugInputSet, self)._set_input('AttachmentsWithData', value)
    def set_BugID(self, value):
        """
        Set the value of the BugID input for this Choreo. ((required, integer) Enter a Bug ID, for which information will be retrieved.)
        """
        super(ListAttachmentsForBugInputSet, self)._set_input('BugID', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((optional, password) Your Bugzilla password.)
        """
        super(ListAttachmentsForBugInputSet, self)._set_input('Password', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((optional, string) The base URL for the Bugzilla server to access. Defaults to https://api-dev.bugzilla.mozilla.org/latest. To access the test server, set to https://api-dev.bugzilla.mozilla.org/test/latest.)
        """
        super(ListAttachmentsForBugInputSet, self)._set_input('Server', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((optional, string) Your Bugzilla username.)
        """
        super(ListAttachmentsForBugInputSet, self)._set_input('Username', value)

class ListAttachmentsForBugResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListAttachmentsForBug Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Bugzilla.)
        """
        return self._output.get('Response', None)

class ListAttachmentsForBugChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListAttachmentsForBugResultSet(response, path)
