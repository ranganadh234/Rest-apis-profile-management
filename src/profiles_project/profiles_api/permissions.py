from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    '''Allow users to edit their own profiles'''

    def has_object_permission(self,request,view,obj):
        '''Check user is trying to edit their own profile'''
        print('permissions obj.id',obj.id)
        print('permissions view',dir(view))
        if request.method in permissions.SAFE_METHODS:
            return True
        print('obj.id == request.user.id:',obj.id == request.user.id)
        return obj.id == request.user.id
class PostOwnStatus(permissions.BasePermission):
    '''Allow users to update their own status.'''

    def has_object_permission(self,request,view,obj):
        '''Check the user is trying to update his/her own status.'''
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id
