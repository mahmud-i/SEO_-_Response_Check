# utils/comparator.py

def compare(data_for_check, data_have_to_check, state):
    result = {}
    meta_title = 'title'
    meta_description = 'description'

    for key in data_for_check.keys():
        if key == 'title':
            meta_title = data_have_to_check[key]
        if key == 'meta description':
            meta_description = data_have_to_check[key]


        if key not in data_have_to_check :
            result[key] = 'Items Not Found'
        elif data_have_to_check[key] is None and data_for_check[key] is None:
            result[key] = 'Both Null'
        elif data_for_check[key] is None:
            result[key] = f'Only in {state}'
        elif data_for_check[key] != data_have_to_check[key]:
            result[key] = 'Not Matched'
        else:
            result[key] = 'Match'


        if key == 'og:title' and data_have_to_check[key] == meta_title and result[key] == 'Not Matched' :
           result[key] = 'Match'
        if key == 'twitter:title' and data_have_to_check[key] == meta_title and result[key] == 'Not Matched' :
           result[key] = 'Match'
        if key == 'og:description' and data_have_to_check[key] == meta_description and result[key] == 'Not Matched' :
           result[key] = 'Match'
        if key == 'twitter:description' and data_have_to_check[key] == meta_description and result[key] == 'Not Matched' :
           result[key] = 'Match'



        # Check if all keys are missing in Production data to mark "No Data Found"
    if all(value == 'Not Found' for value in result.values()):
        return {key: 'No Data Found' for key in result.keys()}

    return result

def compare_seo_data_stage(production_data, stage_data):
    return compare(production_data, stage_data,"Stage")

def compare_seo_data_prod(stage_data, production_data):
    return compare(stage_data, production_data, "Prod")