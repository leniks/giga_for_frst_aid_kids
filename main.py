from config import get_giga_access_token
from utils import read_access_token, read_themes, write_article
import json
import requests
from gigachat import GigaChat
from config import settings

giga = GigaChat(
    credentials=settings.AUTHORIZATION_KEY,
    verify_ssl_certs=False,
    scope="GIGACHAT_API_PERS",
)


themes = read_themes().split('\n\n')
for theme in themes:
    name = ' '.join(theme.split('\n')[0].split()[1:])
    response = giga.chat(f"Представь, что ты врач с огромным опытом работы и профессионал во всех сферах. Мне нужно, чтобы ты написал статью для детского справочника. вот тема статьи {theme}. Учти, что ты объясняешь вещи из этой статьи для детей, поэтому приводи простые и наглядные примеры, где это нужно, не используй сложную лексику и так далее. Также ты можешь украшать свою речь средствами художественной выразительности. Также НЕ пиши НИКАКОГО лишнего текста, в ответе пиши ТОЛЬКО текст статьи. НЕ используй никакое форматирование типо ** или ### и т.д., я конвертирую текст напрямую в md файлы, из-за чего эти символы видно")
    text = response.choices[0].message.content

    write_article(text, name)
