# -*- coding: utf-8 -*-

###############################################################################
#
# ByID
# Retrieves the account information about the specified transaction by Transaction ID.
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

class ByID(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ByID Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ByID, self).__init__(temboo_session, '/Library/Dwolla/Transactions/ByID')


    def new_input_set(self):
        return ByIDInputSet()

    def _make_result_set(self, result, path):
        return ByIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ByIDChoreographyExecution(session, exec_id, path)

class ByIDInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ByID
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) A valid OAuth token.)
        """
        super(ByIDInputSet, self)._set_input('AccessToken', value)
    def set_TransactionID(self, value):
        """
        Set the value of the TransactionID input for this Choreo. ((required, integer) Transaction identifier of the transaction being requested.)
        """
        super(ByIDInputSet, self)._set_input('TransactionID', value)

class ByIDResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ByID Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Dwolla.)
        """
        return self._output.get('Response', None)

class ByIDChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ByIDResultSet(response, path)
