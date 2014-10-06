# -*- coding: utf-8 -*-

###############################################################################
#
# ListPlans
# Returns a list of the shared plans and custom deploys.
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

class ListPlans(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListPlans Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListPlans, self).__init__(temboo_session, '/Library/MongoHQ/Plans/ListPlans')


    def new_input_set(self):
        return ListPlansInputSet()

    def _make_result_set(self, result, path):
        return ListPlansResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListPlansChoreographyExecution(session, exec_id, path)

class ListPlansInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListPlans
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIToken(self, value):
        """
        Set the value of the APIToken input for this Choreo. ((required, string) The API Token provided by MongoHQ.)
        """
        super(ListPlansInputSet, self)._set_input('APIToken', value)

class ListPlansResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListPlans Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from MongoHQ.)
        """
        return self._output.get('Response', None)

class ListPlansChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListPlansResultSet(response, path)
