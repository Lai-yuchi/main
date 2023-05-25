from linebot.models import MessageEvent, TextMessage, ButtonsTemplate, MessageAction, TemplateSendMessage, \
    CarouselTemplate, CarouselColumn, URIAction, PostbackAction

from app1 import line_bot_api, handler


@handler.add(MessageEvent, message=TextMessage)
def rich_menu(event):
    text = event.message.text
    if text == "開始冒險":
        buttons_template = ButtonsTemplate(
            text="請選擇一個故事類型：",
            actions=[
                MessageAction(label="奇幻", text="奇幻"),
                MessageAction(label="童話", text="童話"),
                MessageAction(label="魔法", text="魔法")
            ])
        template_message = TemplateSendMessage(alt_text="請選擇一個故事類型", template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)
        return
    elif text == "團隊介紹":
        carousel_template = CarouselTemplate(columns=[
            CarouselColumn(
                thumbnail_image_url="https://chsinsin.files.wordpress.com/2012/10/014.jpg",
                text="游書涵",
                actions=[
                    URIAction(label="查看書涵的 GitHub", uri="https://github.com/TUNGTUNGHSU"),
                    URIAction(label="call", uri="tel:0908813215")]),
            CarouselColumn(
                thumbnail_image_url="https://ipetgroup.com/photo/50232_0_620.png",
                text="許亦彤",
                actions=[
                    URIAction(label="查看亦彤的 GitHub", uri="https://github.com/TUNGTUNGHSU"),
                    URIAction(label="call", uri="tel:0908813215")]),
            CarouselColumn(
                thumbnail_image_url="https://chsinsin.files.wordpress.com/2012/10/014.jpg",
                text="戴育柔",
                actions=[
                    URIAction(label="查看育柔的 GitHub", uri="https://github.com/estelladai"),
                    URIAction(label="call", uri="tel:0908813215")]),
            CarouselColumn(
                 thumbnail_image_url="https://chsinsin.files.wordpress.com/2012/10/014.jpg",
                 text="李佩樺",
                 actions=[
                     URIAction(label="查看佩樺的 GitHub", uri="https://github.com/DA02019"),
                     URIAction(label="call", uri="tel:0908813215")]),
            CarouselColumn(
                 thumbnail_image_url="https://chsinsin.files.wordpress.com/2012/10/014.jpg",
                 text="王御愷",
                 actions=[
                     URIAction(label="查看御愷的 GitHub", uri="https://github.com/DA02019"),
                     URIAction(label="call", uri="tel:0908813215")]),
            CarouselColumn(
                  thumbnail_image_url="https://chsinsin.files.wordpress.com/2012/10/014.jpg",
                  text="王派森",
                  actions=[
                      URIAction(label="查看派森的 GitHub", uri="https://github.com/DA02019"),
                      URIAction(label="call", uri="tel:0908813215")]),
            CarouselColumn(
                  thumbnail_image_url="https://chsinsin.files.wordpress.com/2012/10/014.jpg",
                  text="陳宗奕",
                  actions=[
                      URIAction(label="查看宗奕的 GitHub", uri="https://github.com/DA02019"),
                      URIAction(label="call", uri="tel:0908813215")]),
            CarouselColumn(
                  thumbnail_image_url="https://chsinsin.files.wordpress.com/2012/10/014.jpg",
                  text="賴禹琪",
                  actions=[
                      URIAction(label="查看禹琪的 GitHub", uri="https://github.com/DA02019"),
                      URIAction(label="call", uri="tel:0908813215")]),
            CarouselColumn(
                   thumbnail_image_url="https://chsinsin.files.wordpress.com/2012/10/014.jpg",
                   text="柏智鈞",
                   actions=[URIAction(label="查看智鈞的 GitHub", uri="https://github.com/DA02019"),
                            URIAction(label="call", uri="tel:0908813215")])
        ])
        template_message = TemplateSendMessage(alt_text="團隊介紹", template=carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)
        return


