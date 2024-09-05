# utils/comparator.py

def compare_seo_data(staging_data, production_data):
    result = {}
    meta_title = 'title'
    meta_description = 'description'

    for key in staging_data.keys():
        if key == 'title':
            meta_title = production_data[key]
        if key == 'meta_description':
            meta_description = production_data[key]


        if key not in production_data or ( production_data[key] is None and staging_data[key] is None):
            result[key] = 'Both Null'
        elif staging_data[key] != production_data[key]:
            result[key] = 'Not Matched'
        else:
            result[key] = 'Match'


        if key == 'og_title' and production_data[key] == meta_title and result[key] == 'Not Matched' :
           result[key] = 'Match'
        if key == 'twitter_title' and production_data[key] == meta_title and result[key] == 'Not Matched' :
           result[key] = 'Match'
        if key == 'og_description' and production_data[key] == meta_description and result[key] == 'Not Matched' :
           result[key] = 'Match'
        if key == 'twitter_description' and production_data[key] == meta_description and result[key] == 'Not Matched' :
           result[key] = 'Match'


        # Check if all keys are missing in Production data to mark "No Data Found"
    if all(value == 'Not Found' for value in result.values()):
        return {key: 'No Data Found' for key in result.keys()}

    return result