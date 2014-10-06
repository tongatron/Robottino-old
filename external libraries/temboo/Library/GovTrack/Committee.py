# -*- coding: utf-8 -*-

###############################################################################
#
# Committee
# Returns committees and subcommittees in the United States Congress, including historical committees.
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

class Committee(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Committee Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Committee, self).__init__(temboo_session, '/Library/GovTrack/Committee')


    def new_input_set(self):
        return CommitteeInputSet()

    def _make_result_set(self, result, path):
        return CommitteeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CommitteeChoreographyExecution(session, exec_id, path)

class CommitteeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Committee
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CommitteeID(self, value):
        """
        Set the value of the CommitteeID input for this Choreo. ((optional, integer) The id of the committee resource. When using this input, all other filter parameters are ignored, and a single record is returned.)
        """
        super(CommitteeInputSet, self)._set_input('CommitteeID', value)
    def set_Committee(self, value):
        """
        Set the value of the Committee input for this Choreo. ((optional, string) Indicates if the object is a committee or a subcommittee. To filter for committees, you can pass "null". For subcommittees, pass the ID of the parent. Filter operators allowed. Sortable.)
        """
        super(CommitteeInputSet, self)._set_input('Committee', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma separated list of fields to return in the response. Use double-underscores to span relationships (e.g. person__firstname).)
        """
        super(CommitteeInputSet, self)._set_input('Fields', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Results are paged 100 per call by default. Set the limit input to a high value to get all of the results at once.)
        """
        super(CommitteeInputSet, self)._set_input('Limit', value)
    def set_Obsolete(self, value):
        """
        Set the value of the Obsolete input for this Choreo. ((optional, string) Whether or not the committee still exists. Set to "true" to return committees that are obsolete. Filter operators allowed. Sortable.)
        """
        super(CommitteeInputSet, self)._set_input('Obsolete', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Offset the results by the number given, useful for paging through results.)
        """
        super(CommitteeInputSet, self)._set_input('Offset', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(CommitteeInputSet, self)._set_input('ResponseFormat', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, string) You can order the results using fieldname (ascending) or -fieldname (descending) where "fieldname" is one of the variables that is listed as 'Sortable' in the description. Ex: '-lastname')
        """
        super(CommitteeInputSet, self)._set_input('Sort', value)

class CommitteeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Committee Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from GovTrack.)
        """
        return self._output.get('Response', None)

class CommitteeChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CommitteeResultSet(response, path)
