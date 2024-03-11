from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS



# class IsOwnerOrReadOnly(BasePermission):


#     def has_object_permission(self, request, view, obj):
#         if request.method in SAFE_METHODS:
#             return True
#         return obj.owner == request.user
    



class UserLevelPermissions(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        print(user)

test = UserLevelPermissions()
