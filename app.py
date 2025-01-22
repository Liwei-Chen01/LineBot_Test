from flask import Flask, request, abort
from linebot import (
LineBotApi, WebhookHandler
)
from linebot.exceptions import (
InvalidSignatureError
)
from linebot.models import (
MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)  
# 必須放上自己的Channel Access Token 
line_bot_api = LineBotApi('LodGL8JbFM0J1iCsH7pv+9UL/qBw+PI4vvYmm8OB/IMzoMc7bYz9yfLvhdfxTNL+aWr5DoDtQnOmyyJuQiiOA7LjLfOl1jI/OyPs5aIBr3igEUQgVExKemtu9U9WpmXqFL+s1pzXdqxJk6KaYGrrNgdB04t89/1O/w1cDnyilFU=')  
# 必須放上自己的Channel Secret
 handler = WebhookHandler('c86b8b78d1491ae7865ed28cead8272d')
 ine_bot_api.push_message('你自己的ID', TextSendMessage(text='你可以開始了'))

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


    #訊息傳遞區塊 
##### 基本上程式編輯都在這個function ##### 
@handler.add(MessageEvent, message=TextMessage) 
def handle_message(event):     
　　message = event.message.text     
　　line_bot_api.reply_message(event.reply_token,TextSendMessage(message))

#主程式 
import os if __name__ == "__main__":    
　　port = int(os.environ.get('PORT', 5000))     
　　app.run(host='0.0.0.0', port=port)