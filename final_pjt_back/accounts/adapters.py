from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        # 기본 저장 필드: first_name, last_name, username, email
        user = super().save_user(request, user, form, False)
        # 추가 저장 필드: profile_image
        nickname = data.get('nickname')
        if nickname:
            user.nickname = nickname
        finance_goal = data.get('finance_goal')
        if finance_goal:
            user.finance_goal = finance_goal
        age = data.get('age')
        if age:
            user.age = age
        assets = data.get('assets')
        if assets:
            user.assets = assets
        salary = data.get('salary')
        if salary:
            user.salary = salary

        user.save()
        return user