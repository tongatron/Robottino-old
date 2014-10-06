# -*- coding: utf-8 -*-

###############################################################################
#
# CreateNewsletter
# Create a new newsletter.
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

class CreateNewsletter(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateNewsletter Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateNewsletter, self).__init__(temboo_session, '/Library/SendGrid/NewsletterAPI/Newsletter/CreateNewsletter')


    def new_input_set(self):
        return CreateNewsletterInputSet()

    def _make_result_set(self, result, path):
        return CreateNewsletterResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateNewsletterChoreographyExecution(session, exec_id, path)

class CreateNewsletterInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateNewsletter
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from SendGrid.)
        """
        super(CreateNewsletterInputSet, self)._set_input('APIKey', value)
    def set_APIUser(self, value):
        """
        Set the value of the APIUser input for this Choreo. ((required, string) The username registered with SendGrid.)
        """
        super(CreateNewsletterInputSet, self)._set_input('APIUser', value)
    def set_HTML(self, value):
        """
        Set the value of the HTML input for this Choreo. ((required, string) The html portion of the newsletter.)
        """
        super(CreateNewsletterInputSet, self)._set_input('HTML', value)
    def set_Identity(self, value):
        """
        Set the value of the Identity input for this Choreo. ((required, string) The Identiy that will be used for the newsletter to be created.  This must be an existing Identity.)
        """
        super(CreateNewsletterInputSet, self)._set_input('Identity', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) The name of the new newsletter.)
        """
        super(CreateNewsletterInputSet, self)._set_input('Name', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from SendGrid, in either json, or xml.  Default is set to json.)
        """
        super(CreateNewsletterInputSet, self)._set_input('ResponseFormat', value)
    def set_Subject(self, value):
        """
        Set the value of the Subject input for this Choreo. ((required, string) The subject for the new newsletter.)
        """
        super(CreateNewsletterInputSet, self)._set_input('Subject', value)
    def set_Text(self, value):
        """
        Set the value of the Text input for this Choreo. ((required, string) The text portion of the newsletter.)
        """
        super(CreateNewsletterInputSet, self)._set_input('Text', value)


class CreateNewsletterResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateNewsletter Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        return self._output.get('Response', None)

class CreateNewsletterChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateNewsletterResultSet(response, path)
