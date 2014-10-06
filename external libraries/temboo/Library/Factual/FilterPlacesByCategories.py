# -*- coding: utf-8 -*-

###############################################################################
#
# FilterPlacesByCategories
# Filter queries by category.
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

class FilterPlacesByCategories(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FilterPlacesByCategories Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(FilterPlacesByCategories, self).__init__(temboo_session, '/Library/Factual/FilterPlacesByCategories')


    def new_input_set(self):
        return FilterPlacesByCategoriesInputSet()

    def _make_result_set(self, result, path):
        return FilterPlacesByCategoriesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FilterPlacesByCategoriesChoreographyExecution(session, exec_id, path)

class FilterPlacesByCategoriesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FilterPlacesByCategories
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) The API Key provided by Factual (AKA the OAuth Consumer Key).)
        """
        super(FilterPlacesByCategoriesInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((optional, string) The API Secret provided by Factual (AKA the OAuth Consumer Secret).)
        """
        super(FilterPlacesByCategoriesInputSet, self)._set_input('APISecret', value)
    def set_Category(self, value):
        """
        Set the value of the Category input for this Choreo. ((required, string) Enter a Factual category to narrow the search results.)
        """
        super(FilterPlacesByCategoriesInputSet, self)._set_input('Category', value)
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((required, string) Enter a city to narrow results to.)
        """
        super(FilterPlacesByCategoriesInputSet, self)._set_input('City', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((optional, string) A search string (i.e. Starbucks))
        """
        super(FilterPlacesByCategoriesInputSet, self)._set_input('Query', value)

class FilterPlacesByCategoriesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FilterPlacesByCategories Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Factual.)
        """
        return self._output.get('Response', None)

class FilterPlacesByCategoriesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return FilterPlacesByCategoriesResultSet(response, path)
