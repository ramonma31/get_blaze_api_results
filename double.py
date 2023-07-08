import requests

import settings


def round_time(date_time):

    try:

        import pendulum
        converted_ronds_time = pendulum.parse(date_time).in_timezone(
            settings.TIME_ZONE
        ).format('HH:mm')
        return converted_ronds_time

    except Exception:
        print(f'{settings.RED}ERROR AT TRYING TO FORMAT TIME{settings.RESET}')


def get_double_result(url):
    try:

        request = requests.get(url).json()
        return request
    
    except Exception:
        print(f'{settings.RED}ERROR REQUESTING THE API{settings.RESET}')


def converted_result_list(function, *args):
    try:

        request = function(*args)
        response = request['records']
        return response
    
    except Exception:
        print(f'''{settings.RED}
ERROR WHEN CONVERTING RESULT IN LIST
{settings.RESET}
''')


def get_a_specific_result(list_results, index, key=None):

    try:

        if key:
            return list_results[index][key]
        else:
            return list_results[index]
        
    except Exception:
        print('ERROR COLLECTING SPECIFIC RESULT')
    

def last_result(key):
    try:

        response = get_a_specific_result(
            converted_result_list(
                get_double_result,
                settings.URL_DOUBLE_HISTORY,
            ),
            index=0,
            key=key
        )
        return response
    
    except Exception:
        print(f'{settings.RED}ERROR AT TRYING TO GET LAST RESULT{settings.RESET}')


def time_last_result():
    date_time = round_time(
        last_result(
            'created_at',
        )
    )
    return date_time


def take_any_result(index, key):
    try:
        response = get_a_specific_result(
            converted_result_list(
                get_double_result,
                settings.URL_DOUBLE_HISTORY,
            ),
            index=index,
            key=key
        )
        return response
    except Exception:
        print(f'{settings.RED}ERROR WHEN TRYING TO GET RESULT{settings.RESET}')


print('')
