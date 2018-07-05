import requests
def get_deviations(key ,transportmode, linenumber, siteid):
    loc_url = 'http://api.sl.se/api2/deviations.json'
    loc_params = {
        'key': key,
        'transportmode': transportmode,
        'linenumber': linenumber,
        'siteid': siteid,
    }
    resp = requests.get(url = loc_url, params = loc_params)
    if resp:
        data = resp.json()
        if data['StatusCode'] == 0:
            return data['ResponseData']
        else:
            raise RuntimeError('Error occured. StatusCode:', data['StatusCode'])

def find_deviations (transportmode, linenumber, siteid):
    data=get_deviations('d12038ad5e5842129dc374e796fe0b08',transportmode,linenumber,siteid)
    #return data
    array=[]
    
    for i in data:
        if 'arbete' in i['Details']:
            array.append(i)
    return array
            
            #print('nothing')

print(find_deviations('','1',''))