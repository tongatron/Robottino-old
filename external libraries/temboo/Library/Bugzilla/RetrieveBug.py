# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveBug
# Retrieve detailed information for a specifed Bug ID.
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

class RetrieveBug(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveBug Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RetrieveBug, self).__init__(temboo_session, '/Library/Bugzilla/RetrieveBug')


    def new_input_set(self):
        return RetrieveBugInputSet()

    def _make_result_set(self, result, path):
        return RetrieveBugResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveBugChoreographyExecution(session, exec_id, path)

class RetrieveBugInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveBug
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_BugID(self, value):
        """
        Set the value of the BugID input for this Choreo. ((required, integer) Enter a Bug ID, for which information will be retrieved.)
        """
        super(RetrieveBugInputSet, self)._set_input('BugID', value)
    def set_IncludeFields(self, value):
        """
        Set the value of the IncludeFields input for this Choreo. ((optional, string) Enter additional parameters to expand the scope of information returned.  For full bug fetch: _all; Or, a comma-separated list: _default, comments, history, attachments.data)
        """
        super(RetrieveBugInputSet, self)._set_input('IncludeFields', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((optional, password) Your Bugzilla password.)
        """
        super(RetrieveBugInputSet, self)._set_input('Password', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((optional, string) The base URL for the Bugzilla server to access. Defaults to https://api-dev.bugzilla.mozilla.org/latest. To access the test server, set to https://api-dev.bugzilla.mozilla.org/test/latest.)
        """
        super(RetrieveBugInputSet, self)._set_input('Server', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((optional, string) Your Bugzilla username.)
        """
        super(RetrieveBugInputSet, self)._set_input('Username', value)

class RetrieveBugResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveBug Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Bugzilla.)
        """
        return self._output.get('Response', None)

class RetrieveBugChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RetrieveBugResultSet(response, path)
