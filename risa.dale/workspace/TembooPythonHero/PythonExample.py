'''
Created on Aug 22, 2012

@author: risa.dale
'''
from temboo.Library.Twitter.Search.SearchFilter import SearchFilter
from temboo.core.session import TembooSession

session = TembooSession(
        "tmb-FFRelease",
        "newkey",
        "sljZPOuCYsbDa4RXDCn9"
    )

twitterSearch = SearchFilter(session)
inputs = twitterSearch.new_input_set()
inputs.set_SearchString("Elvis")
inputs.set_Filter("Costello")
inputs.set_ResultsPerPage(10)
results = twitterSearch.execute_with_results(inputs)
print results.get_Response().encode('utf-8')