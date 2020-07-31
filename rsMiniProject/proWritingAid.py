from __future__ import print_function
import ProWritingAidSDK
from ProWritingAidSDK.rest import ApiException
from pprint import pprint

configuration = ProWritingAidSDK.Configuration()
configuration.host = 'https://api.prowritingaid.com'
configuration.api_key['licenseCode'] = 'FF3F9754-AD50-46AB-A3FF-CEB32B30F9CC'

# create an instance of the API class
api_instance = ProWritingAidSDK.TextApi(ProWritingAidSDK.ApiClient('https://api.prowritingaid.com'))

try:
    api_request = ProWritingAidSDK.TextAnalysisRequest("I place my cane firmly on the ground and, slowly, with its aid, "
                                                       "I lower myself from the hammock. Now the rains have gone my joints "
                                                       "don't hurt so badly. Today won't be too bad, I think. I'm prone to "
                                                       "be over optimistic. Could this be my last day. At this time the jungle "
                                                       "is strangely subdued. She poke around in the ashes. Every day the "
                                                       "weariness is even worst than beofre. I don't know yett. \n"
                                                       "Whne? What a weka statement. Jaroslav Drabny is a Czech football goalkeeper. "
                                                       "Bhuvnehwar Kumar is a Czech football goalkeeper. I just saw Siyabonga Siyo. "
                                                       "I just saw Siyabonga Seyo. I read this article on RaelSport.",
                                                       ["grammar"],
                                                       "General",
                                                       "en")
    api_response = api_instance.post(api_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling API: %s\n" % e)
