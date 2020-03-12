#-*- coding: utf-8 -*-
# for Keyword Extraction
import kss
import KRTextRank as tr
from krwordrank.word import KRWordRank
# load Okt() and initialize
from konlpy.tag import Okt
okt=Okt()
print("Initializing...")
dummy="안녕하세요.저는 30대 초반 여자입니다.가족들에겐 괜찮은척, 괜찮아진척하느라내 힘듦을, 내 좌절을 넋두리 하고싶은데 마땅히 어디 털어놓을 곳이 없어서요..ㅎㅎ남편이라 하기 싫어서 그냥 남자라고만 칭하겠습니다..7년 연애중에 피임을 잘 했는데도 불구하고 아이가 생겨 급하게 결혼을 진행했는데결혼을 준비하는 도중에 아이가 떠났고, 많이 힘들었지만 이미 시작한 결혼준비였기에 예정대로 결혼식을 했습니다. 시부모님은 좋으신분들이에요.그래서 아이 생기자마자 결혼을 진행할 수 있었구요.연애기간이 길었기에 서로 집에도 놀러가고, 가족들과 같이 여행도 가고 했었어요.시댁과의 문제는 전혀 없었고남자 역시 저희 집과 문제가 없었어요.둘 사이의 문제도 없었구요.처음 우리 둘의 아이를 보내고난후에 아이를 다시 갖는게 무서워서결혼후엔 오히려 연애때보다 피임을 철저히 했어요..남자쪽에서도 동의했구요.근데 아이가 다시 찾아왔습니다.남자, 시댁과 상의후에 회사도 바로 관두고 집에서 몸 조심하며 관리한다고 관리했는데또 아이가 떠났어요.다 내탓인 것 같아 첫번째 유산보다 더 힘들었습니다.정신적으로 괴로운 탓인지 성격도 예민해졌고 날카로워졌었죠.병원도 옮겨보고 노력해봤는데 특별한 이상이 없다하니 더 괴로웠어요.내가 대체 무얼 잘못한걸까내가 뭘 조심하지 못했을까나를 질책하고 채찍질하며 나 자신을 혐오할정도로 제 자신이 너무 미웠습니다.그때 시어머님께서 많이 위로해주시고 다독여주셨어요.남자도, 저희 친정도 마찬가지구요.모두에게 고마웠고 감사했고 미안했고 죄송했어요.제가 괴로워하니 온 가족이 함께 괴로워졌죠.어느순간 정신차리자, 달라지는건 없다. 이겨내고 버텨내자 싶은 생각이 들면서취미도 만들고 마음을 컨트롤하기 위해 명상도 다녔어요.시간이 지날수록 제 마음의 상처는 호전되었고점점 예전의 평범한 일상이 되었습니다.다만 저는 다시 아이를 갖는것을 죽는것보다 두려워했고남자는 그런 저를 이해해주었어요.아이없이 우리 둘이 행복하게 살자면서요.누구보다 아이들을 좋아하는 남자였기에, 그 배려가 고맙고 미안했죠..그렇게 1년이 지났는데남자에게 다른 여자가 생긴걸 알게되었고,남자는 처음엔 저에게 용서를 구했어요.실수였다 용서해달라 저랑 절대 헤어질 수 없다면서요.정리하겠다했기에 너무 괴롭지만 눈 감아주기로 했습니다.그리고 몇개월이 흘러서 남자가 만나는 여자에게 연락이 왔어요.남자의 아이를 임신했다고. 헤어질 수 없다고요.처음엔 거짓말일거라 믿었는데..남자 역시 임신이 맞다고 인정했고 내연내는 초음파 사진까지 보내왔습니다.하늘이 무너져내리는 듯 했고내연녀가 아이를 가졌단 사실에 제가 더 초라해져 괴로웠어요.남자에게 내가 이혼해주길 바라냐 물었는데아무 대답을 못하다가 울면서 그러더라구요.그여자가 자기 아이를 가졌는데 어떻게 헤어지겠냐구요.그 말에 저도 복받쳐올라 울면서 말했어요.아이없이 둘이 행복하게 살자며.너 나한테 아이없이 우리 둘이 그냥 행복하게 살쟀잖아.뭐가 부족하고 뭐가 모자라서 다른 여자를 만났니정리한다고 했잖아 우리 왜 이렇게까지 됐어?왜 그여자가 니 아이까지 가진거냐고 물었는데미안하다는 말밖에 할 수 있는 말이 없어 더 미안하데요.한참을 울다가이혼하자는거지. 다시 되물었더니벌받겠다며 이혼해달라길래알았다고 말하곤 짐 챙겨서 친정으로 왔어요.저희 집도, 시댁도 난리가 났었지만시어머님은 역시 본인 배아파 낳은 아들이 먼저더라구요.저희 엄만 억장이 무너져 내린다고 매일같이 가슴을 치며 괴로워하세요.그런 엄마를 보며 저 또한 하루에도 수십번 수백번 무너지고 무너집니다.금은 이혼준비중이고위자료대신 신혼집은 제가 갖기로 했어요.그 둘은 지금 내연녀집에서 같이 살고있고요.근데 내가 피해자인데,이건 누가봐도 분명한 사실인데나는 피해자고, 그 둘이 가해자인데.시간이 지날수록 내가 얼마나 못났으면 다른 여자를 만났을까내가 아이를 끝까지 품지 못해서 다른 여자를 만난걸까내가 두번이나 아이를 그렇게 보내지 않았으면그 남잔 지금도 내 옆에 있었을까내가 그 여자보다 도대체 나은게 뭘까 하는 생각들이 뒤엉켜서제 자존감을 갉아먹고있어요..다 내 탓인 것 같아너무 괴롭고 힘들어요.그 말도 안되는 생각들에게서 헤어나오려 발버둥쳐도더 깊은 늪에 빠져드는 것 같아요.정신병원이라도 가야할까요 뭘해야하는지 모르겠어요 너무 괴로워요"
okt.pos(dummy)
print("Done...!") 

# for Sentiment and Relation Analysis
import requests
import urllib3
import json
import collections
from collections import Counter

# for Python Chatbot
import random
import time
import pyjosa

from flask import Flask, request, jsonify, Response, make_response
import sys
from functools import wraps

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


def sentAnalyze(user_input):
    try:
        adamsURL = "http://api.adams.ai/datamixiApi/tms"
        accessKey = "5071738647222560661"
        text=' '.join(str(s) for s in kss.split_sentences(user_input[:800])) # AdamsAI가 877자 까지밖에 처리하지 못함 
        analysisCode='om'
        language='kor'

        params = dict(
            key=accessKey,
            query=text,
            analysis=analysisCode,
            lang=language
        )

        resp = requests.get(url=adamsURL, params=params)
        data = resp.json()

        sentiword=[]
        for i in range(len(data['return_object']['sentence'])):
            if 'sa' in data['return_object']['sentence'][i] and \
				data['return_object']['sentence'][i]['sa']['sentiword'] and \
				data['return_object']['sentence'][i]['sa']['polarity']<0:
                	print(data['return_object']['sentence'][i]['text'],'\n','\t',data['return_object']['sentence'][i]['sa'])
                	sentiword.append((data['return_object']['sentence'][i]['sa']['score'], 
                                list(filter(lambda w: '/' not in w, data['return_object']['sentence'][i]['sa']['sentiword']))))

        dup=set()
        output=[]
        for x,y in sorted(sentiword): 
            for w in y:
                if not w in dup and 'ㄹ' not in w and '다' in w:  
                    dup.add(w) 
                    output.append((x, w)) 
        print(output)
        
        if not output:
            print("empty")
            return None
        else:
            sent2print=[]
            for i in range(len(output)):
                if len(output) >= 5:
                    sent2print=[output[0][1], output[1][1], output[2][1], output[3][1]]
                else:
                    sent2print.append(output[i][1])
            return ', '.join(str(s) for s in sent2print)
            
    except KeyError:
        return None

def okt_tokenize(sent):
    words = okt.pos(sent, join=True)
    words = [w.split("/")[0] for w in words if '/Noun' in w and len(w.split("/")[0])>1]
    return words

def topic(user_input):
    try:
        openApiURL = "http://aiopen.etri.re.kr:8000/WiseNLU"
        accessKey = "d0831e42-86dd-484f-a5bf-0ccaaed37ae3"
        analysisCode = "NER"
        text=user_input

        requestJson = {
            "access_key": accessKey,
            "argument": {
            "text": text,
            "analysis_code": analysisCode
            }
        }

        http = urllib3.PoolManager()
        response = http.request(
            "POST",
            openApiURL,
            headers={"Content-Type": "application/json; charset=UTF-8"},
            body=json.dumps(requestJson)
        )

        dic=json.loads(response.data) 

        # create relation words list 
        relation_count=[]
        relation_list={}
        temp={}
        
        # CV_RELATION 을 우선순위로 함
        for i in range(len(dic['return_object']['sentence'])):
            for j in range(len(dic['return_object']['sentence'][i]['NE'])):
                if dic['return_object']['sentence'][i]['NE'][j]['type']=='CV_RELATION':
                    relation_count.append(dic['return_object']['sentence'][i]['NE'][j]['text']) 
                    relation_list[dic['return_object']['sentence'][i]['NE'][j]['text']]=dic['return_object']['sentence'][i]['NE'][j]['weight']
        
		# CV_RELATION이 없으면 다른 인간관계 객체명 서치 
        if not relation_count:
            for i in range(len(dic['return_object']['sentence'])):
                for j in range(len(dic['return_object']['sentence'][i]['NE'])):
                    if dic['return_object']['sentence'][i]['NE'][j]['type']=='CV_POSITION' or \
                        dic['return_object']['sentence'][i]['NE'][j]['type']=='CV_OCCUPATION':
                            relation_count.append(dic['return_object']['sentence'][i]['NE'][j]['text'])    
                            relation_list[dic['return_object']['sentence'][i]['NE'][j]['text']]=dic['return_object']['sentence'][i]['NE'][j]['weight']

        c = Counter(relation_count) # counting the number of apperances 
        #print(c)
        count=[k for k,v in c.items() if v>3]
        #print(count)

        for key in relation_list.keys():
            #print(key, relation_list[key])
            if (key in count) and (relation_list[key]>0.2): # sort out relation keywords if the weight >0.2
                temp[key]=relation_list[key]
                #print("temp: ", temp)
				#relation_list[key]=relation_list[key]
                #relation_list[key]=relation_list[key]+1.0

        ### EXCLUDE STOPWORDS
        stop=['석사','박사','대학원생','학생','대학생']
        # update and finalize relation_list 
        relation_list={k:v for k,v in sorted(temp.items(), key=lambda x:x[1], reverse=True) if not k in stop} ### STOPWORDS 
        print("Relation List=", relation_list)


        # create keywords list 
        kw=tr.textrank_keyword(sents=kss.split_sentences(text), tokenize=okt_tokenize, min_count=3, window=2, min_cooccurrence=2)
        #print(kw)
        
        if not kw:
            print("No Keyword List")
            return None
        else:
            kw={k:v for (k,v) in kw}
            print("Keyword List=", kw)
        
        # return final keyword 
        if not relation_list: # if relation does not exist, get first kw but return none
            w=list(kw.keys())[0]
            print("first keyword", w)
            return None
        else:
            # dic=collections.OrderedDict.fromkeys(x for x in relation_list if x in kw)
            #if kw: #is not None: # if relation exists and keyword also exists, get common word 
            dic=collections.OrderedDict.fromkeys(x for x in kw if x in relation_list)
            if dic:
                w=list(dic.keys())[0]
                print("something in common", w)
                return w
            else: # if relation exists but keyword does not, get first relation word 
                w=list(relation_list.keys())[0]
                print("first relation word", w)
                return w
            
    except ValueError: # just in case, handle error
        return None
    
    
        
# to test the app        
@app.route('/keyboard')
def Keyboard():
    dataSend = {
    }
    return jsonify(dataSend)
    
    
    
# create variables
session={}
user_id=''
user_response=''
i=1
j=1
word=''
res=''
val=0



# templates
ending=[
    "작성하느라 수고 많으셨어요. 오늘의 일기를 종료하겠습니다.",
    "수고 많으셨어요. 오늘의 일기작성이 끝났습니다.",
    "오늘 정말 수고 많으셨어요. 일기가 끝났습니다.",
    "기록해 주셔서 감사합니다. 일기를 종료합니다. 내일 만나요!",
    "일기를 작성해 주셔서 고맙습니다. 이제 종료합니다. 또 만나요!"
]

ask=[
    "계속하기에는 답변이 짧습니다. 천천히 생각해 보고, 다시 기록해 주세요.",
    "진행하기에 답변이 부족합니다. 다시 입력해 주세요.",
    "성찰을 계속하기에는 답변이 좀 짧네요. 다시 자세히 기록해 주세요.",
    "답변이 짧습니다. 조금더 시간을 들여 천천히 그리고 자세히 적어 주세요.",
    "계속하기에는 기록이 조금 짧네요. 다시 입력해 주세요."
]

noEmotions=[
    "오늘의 일기를 한번 되돌아 볼게요. 내가 쓴 일기에서 나는 어떤 감정을 느끼는지 한번 적어 보세요.",
    "이제 오늘 내가 쓴 내용을 한번 되돌아 볼게요. 내가 쓴 기록 안에는 어떤 감정들이 보이는지 한번 쭉 써 보세요.",
    "자, 이제 오늘의 일기를 다시 되짚어보면서 내 안에 어떤 감정들이 있었는지 천천히 생각해보고 적어 주세요.",
    "이제 오늘 나의 기록을 돌아보면서 나는 어떤 감정을 느꼈는지, 지금은 어떤지 생각해보고 적어 주세요.",
    "이제 오늘의 일기를 다시 읽어볼게요. 내 일기 안에 보이는 나의 감정들을 관찰해보고, 어떤 감정인지 기록해 주세요."
]

final = [
    "오늘 이 생각들을 잘 간직했으면 좋겠어요. 이제 일기를 마무리할텐데, 오늘 내 자신에게 해주고 싶은 한마디를 적어 주세요.",
    "오늘 이 생각들이 도움이 되길 바래요. 이제 오늘의 일기를 마무리하며 나 스스로에게 해주고 싶은 한마디를 적어 주세요.",
    "이 생각들을 잘 기억했으면 좋겠어요. 이제 일기를 마무리하며 나 자신에게 해주고 싶은 한마디는 무엇인가요?",
    "이 질문들이 도움이 되었기를 바래요. 이제 마무리할텐데 오늘 나 스스로에게 해주고 싶은 한마디가 있다면 무엇인가요?",
    "오늘의 일기가 도움이 되기를 바래요. 마지막으로 오늘 나 자신에게 해주고 싶은 한마디는 무엇인가요?"
]


    
# for dummy chatbot
@app.route('/record_diary', methods=['POST'])
def recordDiary():
        
    global j
    global word
    global user_id, user_response 
    global ending, ask, emotions, noEmotions, final
    global val, session
    
    ### GET USER INFORMATION 
    content=request.get_json()
    user_id=content['userRequest']['user']['id']
    print("Logged in: ", user_id)
    val=j
    session['user_id']=val
     
    if j==1:
        content=request.get_json()
        user_response=content['userRequest']['utterance']
        if len(user_response.split(" "))>100: #100단어 이상 입력
            text=pyjosa.replace_josa(random.choice(ending)) # 일기 종료
            dataSend = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText":{
                                "text" : text
                            }
                        }
                    ]
                }
            }
            print("stage done=", j)
            j=1
            val=0
            time.sleep(0.8) # sleep for 0.8 sec
            return jsonify(dataSend)
        else :
            text=random.choice(ask) # 추가 답변 요청 
            dataSend = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText":{
                                "text" : text
                            }
                        }
                    ]
                }
            }
            j=1
            time.sleep(0.8) # sleep for 0.8 sec
            return jsonify(dataSend)

        
        
# main 
@app.route('/process_diary', methods=['POST'])
def processDiary():
        
    global i
    global res, word
    global user_id, user_response 
    global ending, requests, emotions, noEmotions, final
    global val, session

    ### GET USER INFORMATION 
    content=request.get_json()
    user_id=content['userRequest']['user']['id']
    print("Logged in: ", user_id)
    val=i
    session['user_id']=val
    
    ### CONVERSATION
    if 0<i<6:
        # loop through cycle for 0 < i < 6  
        if i==1: # emotional awareness stage 
            ### GET EMOTIONS
            content=request.get_json()
            user_response=content['userRequest']['utterance']
            if len(user_response.split(" "))>100: # 100단어 이상 입력할것
                res=json.dumps(sentAnalyze(user_response), ensure_ascii=False)
                print(res)
                if res is not 'null': # sentAnalyze에서 리턴하는 것이 string 
                    res=res.strip('\"')
                    emotions=[
                        f"오늘의 일기에서 '{res}'(와)과 같은 감정을 찾았어요. 이런 감정은 지금 나의 몸과 마음에 어떤 영향을 주고 있나요?",
                        f"오늘 기록한 내용에서 '{res}'(와)과 같은 감정을 찾을 수 있었어요. 이 감정은 나에게 어떤 변화를 주나요?",
                        f"오늘의 일기에는 '{res}' - 이러한 감정이 있었네요. 이런 감정을 느낄 때 나의 몸과 마음에 주는 영향을 적어 보세요.",
                        f"오늘의 기록에서 '{res}'(와)과 같은 감정을 발견했어요. 이런 감정을 느낄 때 나는 어떤가요?",
                        f"오늘 일기에는 '{res}'(와)과 같은 감정이 있네요. 이 감정을 느낄 때 나의 몸상태와 마음의 반응을 기록해 주세요."
                    ]
                    text=pyjosa.replace_josa(random.choice(emotions)) #감정 돌아보기
                    dataSend = {
                        "version": "2.0",
                        "template": {
                            "outputs": [
                                {
                                    "simpleText":{
                                        "text" : text
                                    }
                                }
                            ]
                        }
                    }
                    print("stage done=", i)
                    i+=1
                    time.sleep(0.8) # sleep for 0.8 sec
                    return jsonify(dataSend)
                else:
                    text=pyjosa.replace_josa(random.choice(noEmotions)) #감정이 없을 때
                    dataSend = {
                        "version": "2.0",
                        "template": {
                            "outputs": [
                                {
                                    "simpleText":{
                                        "text" : text
                                    }
                                }
                            ]
                        }
                    }
                    print("stage done=", i)
                    i+=1
                    time.sleep(0.8) # sleep for 0.8 sec
                    return jsonify(dataSend)

            else :
                text=random.choice(ask) # 짧으면 추가 답변 요청 
                dataSend = {
                    "version": "2.0",
                    "template": {
                        "outputs": [
                            {
                                "simpleText":{
                                    "text" : text
                                }
                            }
                        ]
                    }
                }
                i=1
                time.sleep(0.8) # sleep for 0.8 sec
                return jsonify(dataSend)

        elif i==2: # first naikan stage 
            ### GET KEYWORD
            word=json.dumps(topic(user_response), ensure_ascii=False)
            print(type(word))
            
            if word is None or word == 'null': # topic에서 리턴
                first_alt = [
                "자, 그럼 이제 이 상황에서 내가 할 수 있었던 것을 생각해서 적어 볼게요.",
                "감정을 들여다보았다면, 이제 이 상황에서 내가 할 수 있었던 것을 적어 볼게요.",
             	"이제 그럼 오늘의 일기를 잠시 성찰해볼게요. 이 상황에서 내가 할 수 있었던 것은 무엇이었을까요?",
                "자, 오늘 이야기한 것을 토대로 한번 생각해 볼게요. 나는 무엇을 할 수 있었을까요?",
                "내 감정을 들여다보았다면, 이제 내가 이 상황에서 무엇을 할 수 있었는지 생각해볼게요."
                ] 
                text=pyjosa.replace_josa(random.choice(first_alt))
            else: 
                print(word)
                word=word.strip('\"')
                first = [
                    f"감정을 들여다보았다면, 이제 오늘의 일기에 등장한 '{word}'에 대해서 좀더 생각해 보았으면 해요. 여태까지 {word}(와)과의 관계에서 내가 받은 것은 무엇일까요?",
                    f"나의 감정을 들여다보았다면, 이제 일기에 등장한 '{word}'에 대해 잠시 성찰해 볼게요. 그동안 {word}(와)과의 관계에서 내가 받은 것은 무엇이 있는지 생각해 보고 적어 주세요.",
                    f"나의 감정을 한번 살펴보았네요. 이제 일기에서 찾은 '{word}'에 대해 좀더 이야기했으면 좋겠어요. 이제까지 {word}(와)과 나의 관계에서 나는 무엇을 받았나요?",
                    f"자, 이제는 일기에 쓴 내용을 토대로 잠시 '{word}'에 대해 생각해 볼게요. 이제껏 내가 {word}(와)과의 관계에서 내가 받은 것이 있다면 무엇일까요?",
                    f"그럼 이제 오늘의 이야기를 바탕으로 '{word}'에 대해 생각해 볼게요. 이제껏 {word}(와)과 지내오면서 이 관계에서 내가 받은 것은 무엇이 있나요?"
                    ]
                text=pyjosa.replace_josa(random.choice(first)) # 첫번째 나이칸 실행 

            dataSend = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText":{
                                "text" : text
                            }
                        }
                    ]
                }
            }
            print("stage done=", i)
            i+=1
            time.sleep(0.8) # sleep for 0.8 sec
            return jsonify(dataSend)

        elif i==3: # second naikan stage 
            if word is None or word=='null':
                second_alt = [
                    "그렇다면 이제 내가 할 수 없었던 것을 적어 볼게요.",
                    "음, 그러면 내가 할 수 없었던 것은 무엇일까요?",
                    "그렇다면 내가 할 수 없었던 것은 무엇이었을까요?",
                    "그럼 나의 통제 밖이었던, 내가 할 수 없었던 것은 무엇이었나요?",
                    "그럼 이제 내가 할 수 없었던 일을 적어볼게요."
                ]
                text=pyjosa.replace_josa(random.choice(second_alt))
            else:
                print(word)
                second = [
                f"그럼 이제 내가 '{word}'에게 사소한 것이라도 주었거나 베푼 것은 무엇인지 적어 볼게요.",
                f"그렇다면 '{word}'(와)과의 관계에서 내가 준 것은 무엇인가요? 잠시 생각해 보고 적어 주세요.",
                f"이젠 '{word}'(와)과의 관계에서 내가 노력한 것을 생각해 볼게요. 내가 베풀었던 것은 무엇인지 적어 보세요.",
                f"그렇다면 나는 '{word}’(와)과의 관계를 위해 무엇을 노력했나요? 사소한 것이라도 괜찮습니다.",
                f"그럼 '{word}'(와)과의 관계를 위해 내가 헌신하거나 베푼 것은 무엇인가요? 무엇이든 상관없이 적어 주세요."
                ]
                text=pyjosa.replace_josa(random.choice(second)) #두번째 나이칸 실행 

            dataSend = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText":{
                                "text" : text
                            }
                        }
                    ]
                }
            }
            print("stage done=", i)
            i+=1
            time.sleep(0.8) # sleep for 0.8 sec
            return jsonify(dataSend)

        elif i==4: # third naikan stage 
            if word is None or word=='null':
                third_alt = [
                    "그렇다면 이 상황에서 나는 어떻게 대처하는것이 좋았을까요?",
                    "그럼 나는 어떻게 대처하는 것이 가장 현명했을까요?",
                    "다음으로, 나는 어떻게 행동하는 것이 가장 현명했을까요?",
                    "그러면 나는 어떻게 대처하는 것이 가장 현명할까요?",
                    "그렇다면 나는 어떻게 행동하는 것이 가장 현명할까요?"
                ]
                text=pyjosa.replace_josa(random.choice(third_alt))
            else:
                print(word)
                third = [
                f"그럼 다음 질문을 해 볼게요. 나는 그동안 '{word}'(와)과 지내면서 어떤 크고작은 걱정이나 근심, 또는 곤란함이나 어려움을 주었나요? 천천히 생각해 보세요.",
                f"그럼 이제 내가 그동안 어떤 것이라도 '{word}'에게 걱정을 끼쳤거나, 힘들게 했거나, 사소한 것이라도 어려움을 주었던 적이  있는지 생각해 볼게요.",
                f"그렇다면 다른 질문을 해 볼게요. 나는 이제껏 '{word}'에게 어떠한 곤란함이나 걱정, 또는 힘듦을 주었을까요?  사소한 것이라도 좋습니다.",
                f"그러면 내가 이제껏 지내면서 '{word}'에게 끼친 걱정이나 어려움, 혹은 괴로움이 조금이라도 있었는지 생각해 보고, 무엇이었는지 적어 주세요.",
                f"자, 그럼 이제 질문을 조금 바꿔 볼게요. 그동안 나는  '{word}'에게 어떤 걱정이나 어려움, 곤란함을 주었을까요? 사소한 것이라도 괜찮으니 생각해 보고 적어 주세요."
                ] 
                text=pyjosa.replace_josa(random.choice(third)) # 세번째 나이칸 실행 

            dataSend = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText":{
                                "text" : text
                            }
                        }
                    ]
                }
            }
            print("stage done=", i)
            i+=1
            time.sleep(0.8) # sleep for 0.8 sec
            return jsonify(dataSend)

        elif i==5: # finish
            text=random.choice(final) # 마지막 한마디 입력 
            dataSend = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText":{
                                "text" : text
                            }
                        }
                    ]
                }
            }
            print("stage done=", i)
            i+=1
            time.sleep(0.8) # sleep for 0.8 sec
            return jsonify(dataSend)

    else: # end
        text=random.choice(ending) # 종료 
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText":{
                            "text" : text
                        }
                    }
                ]
            }
        }
        print("stage done=", i)
        i=1
        val=0
        time.sleep(0.8) # sleep for 0.8 sec
        return jsonify(dataSend)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
    