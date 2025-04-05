from simple_blogger.blogger.auto import AutoBlogger
from simple_blogger.poster.TelegramPoster import TelegramPoster
from simple_blogger.poster.VkPoster import VkPoster
from simple_blogger.poster.InstagramPoster import InstagramPoster
from simple_blogger.editor import Editor
from datetime import date, timedelta

class AnimalBlogger(AutoBlogger):
    def _system_prompt(self):
        return "Ты - специалист по животным, блоггер с 1000000 подписчиков, умеющий заинтересовать аудиторию в изучении животного мира"
    
    def _path_builder(self, task):
        return f"{task['family']},{task['genus']}/{task['species']}"
    
    def _message_prompt_builder(self, task):
        return f"Расскажи интересный факт о животном породы '{task['species']}' из рода '{task['genus']}' семейства '{task['family']}', используй не более 100 слов"
    
    def _image_prompt_builder(self, task):
        return f"Нарисуй животное породы '{task['species']}' из рода '{task['genus']}' семейства '{task['family']}'. Эстетично, красиво, реалистично, крупным планом"
        
    def _posters(self):
        return [
            TelegramPoster(chat_id='@cats_and_beasts'),
            VkPoster(group_id='229821868'),
            InstagramPoster(account_token_name='CATS_AND_BEASTS_TOKEN')
        ]

    def __init__(self, posters=None, first_post_date=date(2025, 3, 11), force_rebuild=False):
        super().__init__(posters=posters or self._posters(), first_post_date=first_post_date, force_rebuild=force_rebuild)

def review():
    day_to_review = 1
    blogger = AnimalBlogger(
        posters=[TelegramPoster()],
        first_post_date=date(2025, 3, 11)-timedelta(days=day_to_review),
        force_rebuild=True
    )
    blogger.post()

def post():
    blogger = AnimalBlogger()
    blogger.post()

def init():
    editor = Editor()
    editor.init_project()
    editor.create_auto(first_post_date=date(2025, 3, 11)+timedelta(days=131))
