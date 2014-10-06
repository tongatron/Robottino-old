# -*- coding: utf-8 -*-

###############################################################################
#
# GetTopicExercises
# Retrieves a list of all exercises for a given topic.
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

class GetTopicExercises(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTopicExercises Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetTopicExercises, self).__init__(temboo_session, '/Library/KhanAcademy/Topics/GetTopicExercises')


    def new_input_set(self):
        return GetTopicExercisesInputSet()

    def _make_result_set(self, result, path):
        return GetTopicExercisesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTopicExercisesChoreographyExecution(session, exec_id, path)

class GetTopicExercisesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTopicExercises
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_TopicID(self, value):
        """
        Set the value of the TopicID input for this Choreo. ((required, string) The ID of the topic.)
        """
        super(GetTopicExercisesInputSet, self)._set_input('TopicID', value)

class GetTopicExercisesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTopicExercises Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Khan Academy.)
        """
        return self._output.get('Response', None)

class GetTopicExercisesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetTopicExercisesResultSet(response, path)
