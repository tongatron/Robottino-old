# -*- coding: utf-8 -*-

###############################################################################
#
# LogBodyMeasurements
# Creates a new log entry for a user's body measurements.
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

class LogBodyMeasurements(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the LogBodyMeasurements Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(LogBodyMeasurements, self).__init__(temboo_session, '/Library/Fitbit/Body/LogBodyMeasurements')


    def new_input_set(self):
        return LogBodyMeasurementsInputSet()

    def _make_result_set(self, result, path):
        return LogBodyMeasurementsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LogBodyMeasurementsChoreographyExecution(session, exec_id, path)

class LogBodyMeasurementsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the LogBodyMeasurements
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(LogBodyMeasurementsInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(LogBodyMeasurementsInputSet, self)._set_input('AccessToken', value)
    def set_Bicep(self, value):
        """
        Set the value of the Bicep input for this Choreo. ((conditional, decimal) The user's bicep measurement.)
        """
        super(LogBodyMeasurementsInputSet, self)._set_input('Bicep', value)
    def set_Calf(self, value):
        """
        Set the value of the Calf input for this Choreo. ((conditional, decimal) The user's calf measurement.)
        """
        super(LogBodyMeasurementsInputSet, self)._set_input('Calf', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Fitbit.)
        """
        super(LogBodyMeasurementsInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Fitbit.)
        """
        super(LogBodyMeasurementsInputSet, self)._set_input('ConsumerSecret', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((required, date) The date that corresponds with the new log entry (in the format yyyy-MM-dd).)
        """
        super(LogBodyMeasurementsInputSet, self)._set_input('Date', value)
    def set_Forearm(self, value):
        """
        Set the value of the Forearm input for this Choreo. ((conditional, decimal) The user's forearm measurement.)
        """
        super(LogBodyMeasurementsInputSet, self)._set_input('Forearm', value)
    def set_Hips(self, value):
        """
        Set the value of the Hips input for this Choreo. ((conditional, decimal) The user's hips measurement.)
        """
        super(LogBodyMeasurementsInputSet, self)._set_input('Hips', value)
    def set_Neck(self, value):
        """
        Set the value of the Neck input for this Choreo. ((conditional, decimal) The user's neck measurement.)
        """
        super(LogBodyMeasurementsInputSet, self)._set_input('Neck', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in: xml or json. Defaults to json.)
        """
        super(LogBodyMeasurementsInputSet, self)._set_input('ResponseFormat', value)
    def set_Thigh(self, value):
        """
        Set the value of the Thigh input for this Choreo. ((conditional, decimal) The user's thigh measurement.)
        """
        super(LogBodyMeasurementsInputSet, self)._set_input('Thigh', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) The user's encoded id. Defaults to "-" (dash) which will return data for the user associated with the token credentials provided.)
        """
        super(LogBodyMeasurementsInputSet, self)._set_input('UserID', value)
    def set_Waist(self, value):
        """
        Set the value of the Waist input for this Choreo. ((conditional, decimal) The user's waist measurement.)
        """
        super(LogBodyMeasurementsInputSet, self)._set_input('Waist', value)
    def set_Weight(self, value):
        """
        Set the value of the Weight input for this Choreo. ((conditional, decimal) The user's weight.)
        """
        super(LogBodyMeasurementsInputSet, self)._set_input('Weight', value)

class LogBodyMeasurementsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the LogBodyMeasurements Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Fitbit.)
        """
        return self._output.get('Response', None)

class LogBodyMeasurementsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return LogBodyMeasurementsResultSet(response, path)
