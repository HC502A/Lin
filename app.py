# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 22:05:00 2020

@author: peishuo
"""

import json
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
import QA_Col
import random

app = Flask(__name__)


line_bot_api = LineBotApi('4FUoMcDT4WiVAdNPASuiO7sfUaJwIJaw4r6aUsUQzqSq8lvW2355lsaDgG6yljZfcGQPACwZ7twzqJaSMmeLfyYkgKPHL+ohr2kYbI45dZ2QKW1XYS+UlrwLAmKin4iprT6KAui37XmbB6Ni9dRtRwdB04t89/1O/w1cDnyilFU=v')

handler = WebhookHandler('7ac4e03c550ab2ae027cc6b3b4359c42')

line_bot_api.push_message('U0f6483bf4b9b9e46c5138c379c3cdf3f', TextSendMessage(text='系統測試中，若您覺得訊息干擾到您，您可以將聊天室設為靜音，謝謝喔！'))

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)

    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

######################處理LINE USER 傳來得訊息 ###############################
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # get user id when reply
    
    profile = line_bot_api.get_profile(event.source.user_id)
    nameid = profile.display_name     #使用者名稱
    uid = profile.user_id             #使用者ID  
    user_message=str(event.message.text) 
    

        #user_message='圖文訊息'
    if user_message.find('圖文訊息') != -1:    
        
        res_message = TemplateSendMessage(
            alt_text='圖文訊息',
            template = CarouselTemplate(
                columns=[
#-----------------------------------------------------------------------------                    
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='圖文訊息選單',
                        text='請由下方選出您想測試的訊息格式！',
                        actions=[
                            MessageTemplateAction(
                                label='文字訊息',
                                text='文字訊息'
                            ),
                            MessageTemplateAction(
                                label='圖片訊息',
                                text='圖片訊息'
                            ),
                            MessageTemplateAction(
                                label='影片訊息',
                                text='影片訊息'
                            ),
                        ]
                    ),                                          
# =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='圖文訊息選單',
                        text='請由下方選出您想測試的訊息格式！',
                        actions=[
                            MessageTemplateAction(
                                label='音訊訊息',
                                text='音訊訊息'
                            ),
                            MessageTemplateAction(
                                label='位置訊息',
                                text='位置訊息'
                            ),
                            MessageTemplateAction(
                                label='貼圖訊息',
                                text='貼圖訊息'
                            ),
                        ]
                    ),                                          
# =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='圖文訊息選單',
                        text='請由下方選出您想測試的訊息格式！',
                        actions=[
                            MessageTemplateAction(
                                label='按鈕介面訊息',
                                text='按鈕介面訊息'
                            ),
                            MessageTemplateAction(
                                label='確認介面訊息',
                                text='確認介面訊息'
                            ),
                            MessageTemplateAction(
                                label='輪播模板訊息',
                                text='輪播模板訊息'
                            ),
                        ]
                    ),                                          
# =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='圖文訊息選單',
                        text='請由下方選出您想測試的訊息格式！',
                        actions=[
                            MessageTemplateAction(
                                label='輪播圖模板訊息',
                                text='輪播圖模板訊息'
                            ),
                            URITemplateAction(
                                label='Line官方說明文件',
                                uri='https://developers.line.biz/zh-hant/docs/messaging-api/message-types/#common-features'
                            ),
                            MessageTemplateAction(
                                label='其他',
                                text='教材尚在開發中'
                            ),
                        ]
                    ),                                          
# =============================================================================        
                 ]            
            )
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0   
        
###############################################################################
        #user_message='文字訊息'
    elif user_message.find('文字訊息') != -1:         #判斷用戶使否傳來"文字訊息"關鍵字，若為是則觸發本區段。   
        
        res_message = TextSendMessage(text='歡迎使用林家花園(台中)E點通，您選擇的是文字測試訊息，您目前看到的是【文字訊息】的回覆方式。')        
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0   
        
###############################################################################
    elif user_message.find('圖片訊息') != -1 :         #判斷用戶使否傳來"圖片訊息"關鍵字，若為是則觸發本區段。  
        
        res_message = ImageSendMessage(
            original_content_url='https://lh3.googleusercontent.com/aif8ioF_c4xQBAt0rvrF0KTnpui5V6ebrsppB-D5csuF-PsmxSTpEbqT8GV1gSpnCCcVWYGA0v683DIE874ODN_cQMn7M52H5oO_XlvijWXFkQYubb6Kik6ciInFt91Vw4ScQz_XEDWTb2WrdOSp56ou62FF9vFih7s-5dUeq7jDFZasf8gQkFYl3A9St4leZVNAMcFtSLoV7plXnQ03h9dIYkiqss9zykuxdDJ61boVxIhgqWoNC9fk_8fhBnXXndxt3AiaBQ-Bc7LeZSXtr4E6mOPPzcK4_XrZzY6xz6NMzH7TC2-px4btW5GZ3JmbX4BOi9TXCZxLLsm4aL3lfL_NVz3pql21b0TqRvQ-P3dE9Ett3FiUTVxqaPASF4SFan7TXRp2VtvoWa8jHULLFlxWI4fr9VQJTRLpx6NneW-_r3EcUAAZ5M5jBmNiaOorEBBCtYwjrKJlaPTIaEN4e0aTrbjUhbud5Khk3hsXcKfGwwkq1qeTEBlRBUsMQfh4sjr1DO9_2j1ZGwFNGG9frG8AuypwR0aFG0z5jSJUfUdpUoB2rOibqU-vUhsQWq6f3zEMCZvkGhEALaqfLLywuHpOLCus108FYOWO5k9GE0_AaqKZzRt-xGfO-j2lG2B_y4Dcq_a1EB12ZW6rTSk_YNY8YhPSyS8QiK9Lzrfbwsx_b5sNgkpsSFtJUbYRoY751MjL0FPCi4RyeOlWGbICFaI=w345-h236-no?authuser=0',
            preview_image_url='https://lh3.googleusercontent.com/aif8ioF_c4xQBAt0rvrF0KTnpui5V6ebrsppB-D5csuF-PsmxSTpEbqT8GV1gSpnCCcVWYGA0v683DIE874ODN_cQMn7M52H5oO_XlvijWXFkQYubb6Kik6ciInFt91Vw4ScQz_XEDWTb2WrdOSp56ou62FF9vFih7s-5dUeq7jDFZasf8gQkFYl3A9St4leZVNAMcFtSLoV7plXnQ03h9dIYkiqss9zykuxdDJ61boVxIhgqWoNC9fk_8fhBnXXndxt3AiaBQ-Bc7LeZSXtr4E6mOPPzcK4_XrZzY6xz6NMzH7TC2-px4btW5GZ3JmbX4BOi9TXCZxLLsm4aL3lfL_NVz3pql21b0TqRvQ-P3dE9Ett3FiUTVxqaPASF4SFan7TXRp2VtvoWa8jHULLFlxWI4fr9VQJTRLpx6NneW-_r3EcUAAZ5M5jBmNiaOorEBBCtYwjrKJlaPTIaEN4e0aTrbjUhbud5Khk3hsXcKfGwwkq1qeTEBlRBUsMQfh4sjr1DO9_2j1ZGwFNGG9frG8AuypwR0aFG0z5jSJUfUdpUoB2rOibqU-vUhsQWq6f3zEMCZvkGhEALaqfLLywuHpOLCus108FYOWO5k9GE0_AaqKZzRt-xGfO-j2lG2B_y4Dcq_a1EB12ZW6rTSk_YNY8YhPSyS8QiK9Lzrfbwsx_b5sNgkpsSFtJUbYRoY751MjL0FPCi4RyeOlWGbICFaI=w345-h236-no?authuser=0'
        )
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0  
    
###############################################################################
        #user_message='影片訊息'
    elif user_message.find('影片訊息') != -1:         #判斷用戶使否傳來"影片訊息"關鍵字，若為是則觸發本區段。 
        
        res_message = VideoSendMessage(
            original_content_url='https://rr3---sn-cvh76nes.googlevideo.com/videoplayback?expire=1641653248&ei=oE_ZYeT_JL_j3LUPvqGtiA0&ip=13.235.242.119&id=o-AKQvnS61FAthPwxryaXpEBxTpROU2bV-OxRePAXwwn0Q&itag=22&source=youtube&requiressl=yes&mh=TW&mm=31%2C29&mn=sn-cvh76nes%2Csn-cvh7knzs&ms=au%2Crdu&mv=m&mvi=3&pl=14&initcwndbps=743750&vprv=1&mime=video%2Fmp4&cnr=14&ratebypass=yes&dur=159.451&lmt=1472263586559530&mt=1641631249&fvip=3&fexp=24001373%2C24007246&c=ANDROID&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAI1D8sbyCw9M5pDfsOAU4Z4zombNwTkD0wOwZo3jCh5cAiAzUw7QReKNa64ZV8jYMqMyMaYMYxRTnZUlv6NVgurdBg%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgaSffPauS3bsp3CXzqOWXmMhD78CSV1xmCNVm8H9vR58CIB5PLELFZ58yJLKdXI9khpLJQt9PymKy2ext1uJiA2iT',
            preview_image_url='https://rr3---sn-cvh76nes.googlevideo.com/videoplayback?expire=1641653248&ei=oE_ZYeT_JL_j3LUPvqGtiA0&ip=13.235.242.119&id=o-AKQvnS61FAthPwxryaXpEBxTpROU2bV-OxRePAXwwn0Q&itag=22&source=youtube&requiressl=yes&mh=TW&mm=31%2C29&mn=sn-cvh76nes%2Csn-cvh7knzs&ms=au%2Crdu&mv=m&mvi=3&pl=14&initcwndbps=743750&vprv=1&mime=video%2Fmp4&cnr=14&ratebypass=yes&dur=159.451&lmt=1472263586559530&mt=1641631249&fvip=3&fexp=24001373%2C24007246&c=ANDROID&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAI1D8sbyCw9M5pDfsOAU4Z4zombNwTkD0wOwZo3jCh5cAiAzUw7QReKNa64ZV8jYMqMyMaYMYxRTnZUlv6NVgurdBg%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgaSffPauS3bsp3CXzqOWXmMhD78CSV1xmCNVm8H9vR58CIB5PLELFZ58yJLKdXI9khpLJQt9PymKy2ext1uJiA2iT'
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0   
        
###############################################################################
        #user_message='音訊訊息'
    elif user_message.find('音訊訊息') != -1:         #判斷用戶使否傳來"音訊訊息"關鍵字，若為是則觸發本區段。 
        
        res_message = message = AudioSendMessage(
            original_content_url='https://rr3---sn-cvh76nes.googlevideo.com/videoplayback?expire=1641653248&ei=oE_ZYeT_JL_j3LUPvqGtiA0&ip=13.235.242.119&id=o-AKQvnS61FAthPwxryaXpEBxTpROU2bV-OxRePAXwwn0Q&itag=140&source=youtube&requiressl=yes&mh=TW&mm=31%2C29&mn=sn-cvh76nes%2Csn-cvh7knzs&ms=au%2Crdu&mv=m&mvi=3&pl=14&initcwndbps=743750&vprv=1&mime=audio%2Fmp4&gir=yes&clen=2533101&dur=159.451&lmt=1467694780372260&mt=1641631249&fvip=3&keepalive=yes&fexp=24001373%2C24007246&c=ANDROID&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhANUkrrHXZHkOz-hI3aI99_iPCvlqBv0UIjS_M0nNqYe0AiEAzD1Xx5afiBYfUd1Kkfx8IkqmnVau46OlhbUbF7VABSs%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgaSffPauS3bsp3CXzqOWXmMhD78CSV1xmCNVm8H9vR58CIB5PLELFZ58yJLKdXI9khpLJQt9PymKy2ext1uJiA2iT',
            duration=328000
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0   
        
###############################################################################
        #user_message='位置訊息'
    elif user_message.find('位置訊息') != -1:         #判斷用戶使否傳來"位置訊息"關鍵字，若為是則觸發本區段。 
        
        res_message = LocationSendMessage(
            title='霧峰林家花園',
            address='413台中市霧峰區民生路26號',
            latitude=24.063123959718546,
            longitude=120.7006997669702
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0   
        
###############################################################################
        #user_message='貼圖訊息'
    elif user_message.find('貼圖訊息') != -1:         #判斷用戶使否傳來"貼圖訊息"關鍵字，若為是則觸發本區段。 
        
        res_message = StickerSendMessage(
            package_id='11539',
            sticker_id='52114116'
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0

###############################################################################
        #user_message='按鈕介面訊息'
    elif user_message.find('按鈕介面訊息') != -1:         #判斷用戶使否傳來"按鈕介面訊息"關鍵字，若為是則觸發本區段。 
        
        res_message = TemplateSendMessage(
            alt_text='按鈕介面訊息',
            template=ButtonsTemplate(
                thumbnail_image_url='https://imgs.gvm.com.tw/upload/gallery/20210126/77456_01.png',
                title='按鈕介面訊息',
                text='此種訊息可以設定1~4個按鈕選項，並可以設定一張1.51:1尺寸的圖片。',
                actions=[
                    MessageTemplateAction(
                        label='測試訊息',
                        text='您剛剛點擊了【測試訊息】'
                    ),
                    URITemplateAction(
                        label='霧峰林家花園首頁',
                        uri='https://www.wufenglins.com.tw/'
                    )
                ]
            )
        )

        line_bot_api.reply_message(event.reply_token,res_message)

        return 0
    
###############################################################################
        #user_message='確認介面訊息'
    elif user_message.find('確認介面訊息') != -1:         #判斷用戶使否傳來"確認介面訊息"關鍵字，若為是則觸發本區段。 
        
        res_message = TemplateSendMessage(
            alt_text='本訊息為【確認介面訊息】',
            template=ConfirmTemplate(
                text='您是否確認要離開本次對話？',
                actions=[
                    MessageTemplateAction(
                        label='是',
                        text='我要離開對話'
                    ),
                    MessageTemplateAction(
                        label='否',
                        text='圖文訊息'
                    )
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)

        return 0
    
###############################################################################
import os

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 27017))
    app.run(host='0.0.0.0', port=port)
if __name__ == "__main__":
    app.run()
