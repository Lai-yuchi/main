import configparser

from debugpy import reply_token
from flask import Flask, request, abort
from linebot import WebhookHandler, LineBotApi
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TemplateSendMessage, ButtonsTemplate, CarouselTemplate, \
    CarouselColumn, URIAction, MessageAction, TextSendMessage

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))


@app.route("/callback", methods=['POST'])
def callback():
    from rich_menu import rich_menu  # 將導入移到函式內部
    handler.add(MessageEvent, message=TextMessage)(rich_menu)

    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


if __name__ == '__main__':
    app.debug = True
    app.run()

