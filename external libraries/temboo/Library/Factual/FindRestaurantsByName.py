# -*- coding: utf-8 -*-

###############################################################################
#
# FindRestaurantsByName
# Search for restaurants by name. 
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

class FindRestaurantsByName(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FindRestaurantsByName Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(FindRestaurantsByName, self).__init__(temboo_session, '/Library/Factual/FindRestaurantsByName')


    def new_input_set(self):
        return FindRestaurantsByNameInputSet()

    def _make_result_set(self, result, path):
        return FindRestaurantsByNameResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FindRestaurantsByNameChoreographyExecution(session, exec_id, path)

class FindRestaurantsByNameInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FindRestaurantsByName
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) The API Key provided by Factual (AKA the OAuth Consumer Key).)
        """
        super(FindRestaurantsByNameInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((optional, string) The API Secret provided by Factual (AKA the OAuth Consumer Secret).)
        """
        super(FindRestaurantsByNameInputSet, self)._set_input('APISecret', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((required, string) A search string (i.e. Starbucks))
        """
        super(FindRestaurantsByNameInputSet, self)._set_input('Query', value)

class FindRestaurantsByNameResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FindRestaurantsByName Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Factual.)
        """
        return self._output.get('Response', None)

class FindRestaurantsByNameChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return FindRestaurantsByNameResultSet(response, path)
