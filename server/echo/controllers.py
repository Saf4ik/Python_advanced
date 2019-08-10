from protocol import make_response
from decorators import logged
from functools import wraps


@logged
@wraps
def get_echo(request):
    data = request.get('data')
    return make_response(request, 200, data)
