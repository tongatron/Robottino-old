# -*- coding: utf-8 -*-

###############################################################################
#
# FeatureLookup
# Searches for features by ID.
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

class FeatureLookup(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FeatureLookup Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(FeatureLookup, self).__init__(temboo_session, '/Library/UnlockPlaces/FeatureLookup')


    def new_input_set(self):
        return FeatureLookupInputSet()

    def _make_result_set(self, result, path):
        return FeatureLookupResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FeatureLookupChoreographyExecution(session, exec_id, path)

class FeatureLookupInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FeatureLookup
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Format(self, value):
        """
        Set the value of the Format input for this Choreo. ((optional, string) The format of the place search results. One of xml, kml, json, georss or txt. Defaults to "xml".)
        """
        super(FeatureLookupInputSet, self)._set_input('Format', value)
    def set_Gazetteer(self, value):
        """
        Set the value of the Gazetteer input for this Choreo. ((optional, string) The place-name source to take locations from. The options are geonames, os, naturalearth or unlock which combines all the previous. Defaults to "unlock".)
        """
        super(FeatureLookupInputSet, self)._set_input('Gazetteer', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((required, integer) The ID of the feature you want to search for. Note that this identifier is returned in the <id> response element of the NameAndFeatureSearch Choreo.)
        """
        super(FeatureLookupInputSet, self)._set_input('ID', value)
    def set_MaxRows(self, value):
        """
        Set the value of the MaxRows input for this Choreo. ((optional, integer) The maximum number of results to return. Defaults to 20. Cannot exceed 1000.)
        """
        super(FeatureLookupInputSet, self)._set_input('MaxRows', value)
    def set_StartRow(self, value):
        """
        Set the value of the StartRow input for this Choreo. ((optional, integer) The row to start results display from. Defaults to 1.)
        """
        super(FeatureLookupInputSet, self)._set_input('StartRow', value)

class FeatureLookupResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FeatureLookup Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Unlock. Defaults to XML based on the format input parameter.)
        """
        return self._output.get('Response', None)

class FeatureLookupChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return FeatureLookupResultSet(response, path)
