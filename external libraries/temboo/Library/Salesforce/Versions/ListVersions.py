# -*- coding: utf-8 -*-

###############################################################################
#
# ListVersions
# Lists summary information about each Salesforce version currently available, including the version, label, and a link to each version's root.
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

class ListVersions(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListVersions Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListVersions, self).__init__(temboo_session, '/Library/Salesforce/Versions/ListVersions')


    def new_input_set(self):
        return ListVersionsInputSet()

    def _make_result_set(self, result, path):
        return ListVersionsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListVersionsChoreographyExecution(session, exec_id, path)

class ListVersionsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListVersions
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_InstanceName(self, value):
        """
        Set the value of the InstanceName input for this Choreo. ((required, string) The server url prefix that indicates which instance your Salesforce account is on (e.g. na1, na2, na3, etc).)
        """
        super(ListVersionsInputSet, self)._set_input('InstanceName', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(ListVersionsInputSet, self)._set_input('ResponseFormat', value)

class ListVersionsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListVersions Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Salesforce.)
        """
        return self._output.get('Response', None)

class ListVersionsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListVersionsResultSet(response, path)
