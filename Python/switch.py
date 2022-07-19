# after python 3.10
status = 403
match status:
    case 400: print('Bad request')
    case 401: print('Unauthorized')
    case 403: print('Forbidden')
    case 404: print('Not found')
    case _: print('Other error')



# before python 3.10
switcher = {
    400: 'Bad request',
    401: 'Unauthorized',
    403: 'Forbidden',
    404: 'Not found'
}
print(switcher.get(status, 'Other error'))