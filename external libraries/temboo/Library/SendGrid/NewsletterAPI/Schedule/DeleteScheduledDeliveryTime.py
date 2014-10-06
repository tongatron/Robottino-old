# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteScheduledDeliveryTime
# Delete a scheduled Newsletter delivery time.
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

class DeleteScheduledDeliveryTime(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteScheduledDeliveryTime Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteScheduledDeliveryTime, self).__init__(temboo_session, '/Library/SendGrid/NewsletterAPI/Schedule/DeleteScheduledDeliveryTime')


    def new_input_set(self):
        return DeleteScheduledDeliveryTimeInputSet()

    def _make_result_set(self, result, path):
        return DeleteScheduledDeliveryTimeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteScheduledDeliveryTimeChoreographyExecution(session, exec_id, path)

class DeleteScheduledDeliveryTimeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteScheduledDeliveryTime
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from SendGrid.)
        """
        super(DeleteScheduledDeliveryTimeInputSet, self)._set_input('APIKey', value)
    def set_APIUser(self, value):
        """
        Set the value of the APIUser input for this Choreo. ((required, string) The username registered with SendGrid.)
        """
        super(DeleteScheduledDeliveryTimeInputSet, self)._set_input('APIUser', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) The name of the newsletter for which scheduled delievery will be removed.)
        """
        super(DeleteScheduledDeliveryTimeInputSet, self)._set_input('Name', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from SendGrid, in either json, or xml.  Default is set to json.)
        """
        super(DeleteScheduledDeliveryTimeInputSet, self)._set_input('ResponseFormat', value)


class DeleteScheduledDeliveryTimeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteScheduledDeliveryTime Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        return self._output.get('Response', None)

class DeleteScheduledDeliveryTimeChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteScheduledDeliveryTimeResultSet(response, path)
