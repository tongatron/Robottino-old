# -*- coding: utf-8 -*-

###############################################################################
#
# AllCategories
# Retrieves all the badge categories in Khan Academy.
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

class AllCategories(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AllCategories Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(AllCategories, self).__init__(temboo_session, '/Library/KhanAcademy/Badges/AllCategories')


    def new_input_set(self):
        return AllCategoriesInputSet()

    def _make_result_set(self, result, path):
        return AllCategoriesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AllCategoriesChoreographyExecution(session, exec_id, path)

class AllCategoriesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AllCategories
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    pass

class AllCategoriesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AllCategories Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Khan Academy.)
        """
        return self._output.get('Response', None)

class AllCategoriesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AllCategoriesResultSet(response, path)
