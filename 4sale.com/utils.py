def generate_property_dict(data,lat,long):
    d = { 'title':'Property for '+data['type']+' at ' + data['address'],
         'type':data['type'],
         'locality':data['locality'],
         'city':data['city'],
         'pincode':data['pincode'], 
         'address':data['address'],
         'short_description':data['short_description'],
         'bedrooms':int(data['bedrooms']),
         'bathrooms':int(data['bathrooms']), 
         'patio':int(data['patio']),
         'area':float(data['area']),
         'cost':float(data['cost']),
         'latitude':float(lat),
         'longitude':float(long) }
    return d

def generate_property_analytics_dict(dict1,dict2):
    d = {}
    for place in dict1:
        d[place+'1'] = dict1[place][place+'1']['name']
        d[place+'2'] = dict1[place][place+'2']['name']
    for place in dict2:
        d['distance_'+place+'1'] = dict2[place][place+'1']['distance']
        d['distance_'+place+'2'] = dict2[place][place+'2']['distance']
        d['time_'+place+'1'] = dict2[place][place+'1']['time']
        d['time_'+place+'1'] = dict2[place][place+'2']['time']
        d['message_'+place+'1'] = dict2[place][place+'1']['message']
        d['message_'+place+'2'] = dict2[place][place+'2']['message']
    return d