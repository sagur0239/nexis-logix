from django.utils.cache import add_never_cache_headers

class DisableBackButtonMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # ইউজার লগআউট থাকা অবস্থায় ব্রাউজারকে কোনো পেজ ক্যাশ (মেমরি) করতে দেবে না
        if not request.user.is_authenticated:
            add_never_cache_headers(response)
            response['Cache-Control'] = 'no-cache, no-store, must-revalidate, max-age=0'
            response['Pragma'] = 'no-cache'
            response['Expires'] = '0'
            
        return response