import requests,simplejson
#def get_tripplan(originId, destid, searchForArrival, key):
originId = 9192
destid =1002
searchForArrival=0
key ='4dacb020b3cb4e8a9b2e027437c5b72b'
loc_url = 'http://api.sl.se/api2/TravelplannerV3/trip.json'
loc_params = {
    'key': key,
    'originId': originId,
    'destid': destid,
    'searchForArrival': searchForArrival,
}
resp = requests.get(url = loc_url, params = loc_params)
data = resp.json()
json_string = simplejson.dumps(data)
print(json_string)

list_ref=[]

#jddd is a dict
jddd=simplejson.loads(json_string)
trip = jddd['Trip']
# trip is a list of possible trip solutions (different routes, different schedule, etc.)
# for each trip solution, there will be one "JourneyDetailRef", get "ref" from this "JourneyDetailRef"
num_tripsolutions=len(trip)

for num in range(0,num_tripsolutions):
    # singletrip is a dict
    singletrip=trip[num]
    LegList=singletrip['LegList']
    # LegList is a dict
    # but it seems this dict only contain 'Leg' as the key
    Leg=LegList['Leg']
    # Leg is a list
    num_Leg=len(Leg)
    for num_2 in range(0,num_Leg):
        myLeg=Leg[num_2]
        # myLeg is a dict, which contains the keys "Origin", "Destination", "JourneyDetailRef", etc., what we want is the 'ref' from "JourneyDetailRef"
        JourneyDetailRef=myLeg['JourneyDetailRef']
        # JourneyDetailRef is a dict, the only key is 'ref'
        ref=JourneyDetailRef['ref']
        # ref is a string
        list_ref.append(ref)
        


loc_url_journeydetail = 'http://api.sl.se/api2/TravelplannerV3/journeydetail.json'
num_list_ref=len(list_ref)
for num_3 in range(0,num_list_ref):
    singleref=list_ref[num_3]
    loc_params_journeydetail = {
    'key': key,
    'id': singleref,
    }
    resp_journeydetail = requests.get(url = loc_url_journeydetail, params = loc_params_journeydetail)
    data_journeydetail = resp_journeydetail.json()
    print('\n');
    print(data_journeydetail)
    

    



#for key,value in myLeg.items():
#    print('\n');
#    print(key, ':',value)
