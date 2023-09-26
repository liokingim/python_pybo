from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # 사용자 인증(사용자명과 비밀번호가 정확한지 검증한다.)
            user = authenticate(username=username, password=raw_password)
            # 로그인 (사용자 세션을 생성한다.)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()

    return render(request, 'common/signup.html', {'form':form})
