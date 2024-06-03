from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAdminCustom(UserAdmin):
    # ユーザー詳細
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'email',
                'password',
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
    )
    # ユーザー追加
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'name',
                'email',
                'password1',
                'password2',
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
    )

    # ユーザー一覧
    list_display = (
        'id',
        'name',
        'email',
        'is_active',
    )

    list_filter = ()
    # 検索
    search_fields = ('email',)
    # 順番
    ordering = ('id',)


# unregister User model if it's already registered
try:
    admin.site.unregister(User)
except:
    pass
# Register User model with custom options
admin.site.register(User, UserAdminCustom)
