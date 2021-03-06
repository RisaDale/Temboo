# -*- coding: utf-8 -*-

###############################################################################
#
# ZipCodeLookup
# Lookup zip codes using incomplete address information.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ZipCodeLookup(Choreography):

    """
    Create a new instance of the ZipCodeLookup Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/USPS/AddressInformationAPI/ZipCodeLookup')


    def new_input_set(self):
        return ZipCodeLookupInputSet()

    def _make_result_set(self, result, path):
        return ZipCodeLookupResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ZipCodeLookupChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ZipCodeLookup
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ZipCodeLookupInputSet(InputSet):
        """
        Set the value of the ApyOrSuite input for this choreography. ((optional, string) Used to provide an apartment or suite number, if applicable. Maximum characters allowed: 38.)
        """
        def set_ApyOrSuite(self, value):
            InputSet._set_input(self, 'ApyOrSuite', value)

        """
        Set the value of the City input for this choreography. ((string) Maximum characters allowed: 15.)
        """
        def set_City(self, value):
            InputSet._set_input(self, 'City', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) If you are accessing the production server, set to 'production'. Defaults to 'testing' which indicates that you are using the sandbox.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the FirmName input for this choreography. ((optional, string) Maximum characters allowed: 38. )
        """
        def set_FirmName(self, value):
            InputSet._set_input(self, 'FirmName', value)

        """
        Set the value of the Password input for this choreography. ((string) The password assigned by USPS)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the State input for this choreography. ((string) Maximum characters allowed: 2.)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)

        """
        Set the value of the StreetAddress input for this choreography. ((string) Street address.  Maximum characters allowed: 38.)
        """
        def set_StreetAddress(self, value):
            InputSet._set_input(self, 'StreetAddress', value)

        """
        Set the value of the UserId input for this choreography. ((string) Alphanumeric ID assigned by USPS)
        """
        def set_UserId(self, value):
            InputSet._set_input(self, 'UserId', value)


"""
A ResultSet with methods tailored to the values returned by the ZipCodeLookup choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ZipCodeLookupResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from USPS Web Service)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ZipCodeLookupChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ZipCodeLookupResultSet(response, path)
