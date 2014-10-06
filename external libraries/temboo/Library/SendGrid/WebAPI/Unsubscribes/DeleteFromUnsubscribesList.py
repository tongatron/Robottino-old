# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteFromUnsubscribesList
# Delete an address from the Unsubscribe list.
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

class DeleteFromUnsubscribesList(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteFromUnsubscribesList Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteFromUnsubscribesList, self).__init__(temboo_session, '/Library/SendGrid/WebAPI/Unsubscribes/DeleteFromUnsubscribesList')


    def new_input_set(self):
        return DeleteFromUnsubscribesListInputSet()

    def _make_result_set(self, result, path):
        return DeleteFromUnsubscribesListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteFromUnsubscribesListChoreographyExecution(session, exec_id, path)

class DeleteFromUnsubscribesListInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteFromUnsubscribesList
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from SendGrid.)
        """
        super(DeleteFromUnsubscribesListInputSet, self)._set_input('APIKey', value)
    def set_APIUser(self, value):
        """
        Set the value of the APIUser input for this Choreo. ((required, string) The username registered with SendGrid.)
        """
        super(DeleteFromUnsubscribesListInputSet, self)._set_input('APIUser', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((optional, string) The unsubscribed email address to be deleted from the list. If no parameters are provided, the ENTIRE list will be removed.)
        """
        super(DeleteFromUnsubscribesListInputSet, self)._set_input('Email', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((optional, string) The end of the date range for which blocks are to be retireved. The specified date must be in YYYY-MM-DD format.)
        """
        super(DeleteFromUnsubscribesListInputSet, self)._set_input('EndDate', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from SendGrid, in either json, or xml.  Default is set to json.)
        """
        super(DeleteFromUnsubscribesListInputSet, self)._set_input('ResponseFormat', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((optional, string) The start of the date range for which blocks are to be retireved. The specified date must be in YYYY-MM-DD format, and must be earlier than the EndDate variable value. Use this ,or Days.)
        """
        super(DeleteFromUnsubscribesListInputSet, self)._set_input('StartDate', value)


class DeleteFromUnsubscribesListResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteFromUnsubscribesList Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        return self._output.get('Response', None)

class DeleteFromUnsubscribesListChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteFromUnsubscribesListResultSet(response, path)
