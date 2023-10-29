from werkzeug.exceptions import HTTPException

class AccessError(HTTPException):
    code = 403
    message = 'Error 403: Access cannot be granted'

class InputError(HTTPException):
    code = 400
    message = 'Error 400: Invalid Input'
