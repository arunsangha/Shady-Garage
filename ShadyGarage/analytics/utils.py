
def get_client_ip(request):
    x_forwared_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwared_for:
        ip = x_forwared_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip
