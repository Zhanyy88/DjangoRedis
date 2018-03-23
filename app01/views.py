from django.http import HttpResponse
from django.shortcuts import render
from redis import StrictRedis
from django_redis import get_redis_connection

# Create your views here.
def index(request):
    '''进入首页'''
    # strict_redis = get_redis_connection()
    #
    # strict_redis.set('aa',1221)
    # strict_redis.set('bb',2333)
    #
    # #查
    # aa = strict_redis.get('aa')
    # bb = strict_redis.get('bb')
    # text = 'aa=%s   bb=%s'%(aa.decode(),bb)


    return render(request,'index.html')


def set_session(request):
    """"保存session数据"""

    request.session['username'] = 'Django'
    request.session['verify_code'] = '123456'
    return HttpResponse('保存session数据成功')


def get_session(request):
    """获取session数据"""

    username = request.session.get('username')
    verify_code = request.session.get('verify_code')
    text = 'username=%s, verify_code=%s' % (username, verify_code)
    return HttpResponse(text)
def add_num(request,good_id):
    user = request.session.get('username')
    good_1 = request.session.get('good_1')
    good_1 = request.session.get('good_1')

    return render(request,'index.html')