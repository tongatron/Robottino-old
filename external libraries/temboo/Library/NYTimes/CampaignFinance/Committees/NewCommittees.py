# -*- coding: utf-8 -*-

###############################################################################
#
# NewCommittees
# Retrieves 20 of the most recently added committees.
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

class NewCommittees(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the NewCommittees Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(NewCommittees, self).__init__(temboo_session, '/Library/NYTimes/CampaignFinance/Committees/NewCommittees')


    def new_input_set(self):
        return NewCommitteesInputSet()

    def _make_result_set(self, result, path):
        return NewCommitteesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return NewCommitteesChoreographyExecution(session, exec_id, path)

class NewCommitteesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the NewCommittees
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by NY Times.)
        """
        super(NewCommitteesInputSet, self)._set_input('APIKey', value)
    def set_CampaignCycle(self, value):
        """
        Set the value of the CampaignCycle input for this Choreo. ((required, integer) Enter the campaign cycle year in YYYY format.  This must be an even year. )
        """
        super(NewCommitteesInputSet, self)._set_input('CampaignCycle', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Enter json or xml.  Default is json.)
        """
        super(NewCommitteesInputSet, self)._set_input('ResponseFormat', value)

class NewCommitteesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the NewCommittees Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the NY Times API corresponds to the setting (json, or xml) entered in the ResponseFormat variable.  Default is set to json.)
        """
        return self._output.get('Response', None)

class NewCommitteesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return NewCommitteesResultSet(response, path)
