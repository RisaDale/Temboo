# -*- coding: utf-8 -*-

###############################################################################
#
# CreateContact
# Creates a contact in your Constant Contact account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateContact(Choreography):

    """
    Create a new instance of the CreateContact Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/ConstantContact/CreateContact')


    def new_input_set(self):
        return CreateContactInputSet()

    def _make_result_set(self, result, path):
        return CreateContactResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateContactChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateContact
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateContactInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Constant Contact.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Addr1 input for this choreography. ((optional, string) The first line of the contact's address.)
        """
        def set_Addr1(self, value):
            InputSet._set_input(self, 'Addr1', value)

        """
        Set the value of the Addr2 input for this choreography. ((optional, string) The second line of the contact's address.)
        """
        def set_Addr2(self, value):
            InputSet._set_input(self, 'Addr2', value)

        """
        Set the value of the Addr3 input for this choreography. ((optional, string) The third line of the contact's address.)
        """
        def set_Addr3(self, value):
            InputSet._set_input(self, 'Addr3', value)

        """
        Set the value of the City input for this choreography. ((optional, string) The city portion of the contact's address.)
        """
        def set_City(self, value):
            InputSet._set_input(self, 'City', value)

        """
        Set the value of the CompanyName input for this choreography. ((optional, string) The company name for the contact.)
        """
        def set_CompanyName(self, value):
            InputSet._set_input(self, 'CompanyName', value)

        """
        Set the value of the CountryCode input for this choreography. ((optional, string) The country code associated with the contact's address.)
        """
        def set_CountryCode(self, value):
            InputSet._set_input(self, 'CountryCode', value)

        """
        Set the value of the CountryName input for this choreography. ((optional, string) Corresponds to the Country Name field in Constant Contact)
        """
        def set_CountryName(self, value):
            InputSet._set_input(self, 'CountryName', value)

        """
        Set the value of the EmailAddress input for this choreography. ((required, string) The email address for the contact.)
        """
        def set_EmailAddress(self, value):
            InputSet._set_input(self, 'EmailAddress', value)

        """
        Set the value of the EmailType input for this choreography. ((optional, string) The email type that the contact should receive.)
        """
        def set_EmailType(self, value):
            InputSet._set_input(self, 'EmailType', value)

        """
        Set the value of the FirstName input for this choreography. ((optional, string) The first name of the contact.)
        """
        def set_FirstName(self, value):
            InputSet._set_input(self, 'FirstName', value)

        """
        Set the value of the HomePhone input for this choreography. ((optional, string) The contact's home phone.)
        """
        def set_HomePhone(self, value):
            InputSet._set_input(self, 'HomePhone', value)

        """
        Set the value of the JobTitle input for this choreography. ((optional, string) The contact's job title.)
        """
        def set_JobTitle(self, value):
            InputSet._set_input(self, 'JobTitle', value)

        """
        Set the value of the LastName input for this choreography. ((optional, string) The last name of the contact.)
        """
        def set_LastName(self, value):
            InputSet._set_input(self, 'LastName', value)

        """
        Set the value of the ListId input for this choreography. ((required, integer) The ID for the list that you want to add the contact to.)
        """
        def set_ListId(self, value):
            InputSet._set_input(self, 'ListId', value)

        """
        Set the value of the MiddleName input for this choreography. ((optional, string) The middle name of the contact.)
        """
        def set_MiddleName(self, value):
            InputSet._set_input(self, 'MiddleName', value)

        """
        Set the value of the Name input for this choreography. ((optional, string) The full name of the contact.)
        """
        def set_Name(self, value):
            InputSet._set_input(self, 'Name', value)

        """
        Set the value of the Note input for this choreography. ((optional, string) A note associated with the contact.)
        """
        def set_Note(self, value):
            InputSet._set_input(self, 'Note', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your Constant Contact password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the PostalCode input for this choreography. ((optional, string) The postal code for the contact's address.)
        """
        def set_PostalCode(self, value):
            InputSet._set_input(self, 'PostalCode', value)

        """
        Set the value of the StateCode input for this choreography. ((optional, string) The state code for the contact's address.)
        """
        def set_StateCode(self, value):
            InputSet._set_input(self, 'StateCode', value)

        """
        Set the value of the StateName input for this choreography. ((optional, string) Corresponds to the State Name field in Constant Contact)
        """
        def set_StateName(self, value):
            InputSet._set_input(self, 'StateName', value)

        """
        Set the value of the Status input for this choreography. ((optional, string) The status of the contact (i.e. Active).)
        """
        def set_Status(self, value):
            InputSet._set_input(self, 'Status', value)

        """
        Set the value of the SubPostalCode input for this choreography. ((optional, string) The sub postal code for the contact.)
        """
        def set_SubPostalCode(self, value):
            InputSet._set_input(self, 'SubPostalCode', value)

        """
        Set the value of the UserName input for this choreography. ((required, string) Your Constant Contact username.)
        """
        def set_UserName(self, value):
            InputSet._set_input(self, 'UserName', value)

        """
        Set the value of the WorkPhone input for this choreography. ((optional, string) The contact's work phone.)
        """
        def set_WorkPhone(self, value):
            InputSet._set_input(self, 'WorkPhone', value)


"""
A ResultSet with methods tailored to the values returned by the CreateContact choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateContactResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Constant Contact.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateContactChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateContactResultSet(response, path)
