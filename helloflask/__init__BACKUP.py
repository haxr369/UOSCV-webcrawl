#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

from flask import Flask,render_template, g,request, Response, make_response
import utility

#from forms import RegistrationForm
# g : 현재 들어오는 모든 사람에대한 설정은 g(global)를 사용한다. Application context 다룰 때 사용
# make_response : response 객체를 만들어준다. 큰 데이터를 보낼 때 서버와 클라이언트를 가볍게 만들어준다.!!

app = Flask(__name__)
app.debug =True
app.config["SECRET_KEY"] = 'd2707fea9778e085491e2dbbc73ff30e'


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


            
            
            
            
@app.route('/', methods=["GET", "POST"])
def register(username=None, imagenumb=None):
    #form = RegistrationForm()
    
    if request.method =="POST":
        username = request.form.get('username')
        imagenumb = request.form.get('imagenumb')
        
        if imagenumb=="" or username=="":
            return "필요한 모든 정보를 알려주세요"
        
        utility.download_im(username,username,int(imagenumb))
  
    return render_template('file_down.html', username=username,imagenumb= imagenumb)


#다운로드 HTML 렌더링
@app.route('/downfile')
def down_page():
    files = os.listdir("./uploads")
    return render_template('filedown.html',files=files)

#파일 다운로드 처리
@app.route('/fileDown', methods = ['GET', 'POST'])
def down_file():
    if request.method == 'POST':
        sw=0
        files = os.listdir("./uploads")
        for x in files:
            if(x==request.form['file']):
                sw=1

        path = "./uploads/" 
        return send_file(path + request.form['file'],
                attachment_filename = request.form['file'],
                as_attachment=True)



"""
    if form.validate_on_submit():
        # 알람 카테고리에 따라 부트스트랩에서 다른 스타일을 적용 (success, danger) 
        flash(f'{form.username.data} 님 가입 완료!', 'success')
        return redirect(url_for('home'))
"""





"""
@app.before_request #사용자가 request하기 전에 무조건 실행해준다. 라우터 역할 Web filter
def before_request(): #app 실행하자마자 실행
    print("before_request!!!")
    g.str = "한글" #ex 사용자가 들어올때 값을 저장++하는 용도등 Application context에 저장된다..!! 


@app.route("/gg") #가장 첫 페이지 보여주기 request 받으면 실행!! 즉 모델 역할 

def helloworld2():
    return "Hello Flask World!"+getattr(g,"str","111") #g라는 인자의 str 값을 불러와라("한글") 없으면 111을 불러와라
    
    
@app.after_request # 끝날 때 무조건 실행


"""
















@app.route('/rp') 
def rp():
    #q = request.values.get('q')  # url 다음에 ?<아무 정보>를 적으면 q에 <아무 정보가 입력된다.> #GET이나 POST으로 보내는 방법
    q = request.args.getlist('q') #q에 list 정보를 입력해준다.
    q = request.form.getlist('q') #post 정보 관할
    
    #매우 큰 데이터는 post에 body로 주고 받을 수 있다.
    return "q= %s" % str(q)

"""
#request type 커스터마이징
@app.route('/df')
def dt():
    datestr = request.values.get('date', date.today(), type = ymd('%Y-%m-%d')) #입력 포멧을 다양하게 만들 수 있
    return "현재 시간 형식: "+ str(datestr)
"""


@app.route('/test_wsgi')
def wsgi_test():
    def application(environ, start_response):
        body = 'the request method was %s' % environ['REQUEST_METHOD']
        headers = [('Content-Type','text/plain'),
                  ('Content-Length',str(len(body)))]
        start_response('200 OK',headers)
        return [body]
    return make_response(application)


@app.route('/res1')
def res1():
    custom_res = Response("Custom Response",200, {"test_json_id":"test_json_data"}) #중간에 200은 정상 출력을 나타낸다!!
    #이 response는 html header부분에 보내지고, 정보를 보낼 수 있다ㅓ.
    return make_response(custom_res)



"""

@app.route("/", methods=['GET','POST']) #가장 첫 페이지 보여주기 요청에대한
def helloworld(): #함수명은 중복되면 안됩니다!!  response!!
    if userid==None:
        return "Hello world!!"
    else:
        return "어서오세요!! " + str(userid)+"님!! 당신의 emil은 "+str(email)+" 입니다.!!"

"""




