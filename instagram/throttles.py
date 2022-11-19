from rest_framework.throttling import UserRateThrottle


class ContactRateThrottle(UserRateThrottle):
    scope = 'contact'


class UploadRateThrottle(UserRateThrottle):
    scope = 'upload'
