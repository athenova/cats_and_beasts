from simple_blogger import Journalist
from simple_blogger.generators.YandexGenerator import YandexImageGenerator
from simple_blogger.generators.YandexGenerator import YandexTextGenerator
from datetime import datetime

class Project(Journalist):
    def _system_prompt(self, _):
        return "Ты - специалист по животным, блоггер с 1000000 подписчиков, умеющий заинтересовать аудиторию в изучении животного мира"

    def _example_task_creator(self):
        return [ {"family": "Family", "genus": "Genus", "species": "Species"} ]

    def _get_category_folder(self, task):
        return f"{task['family']}/{task['genus']}"

    def _get_topic_folder(self, task):
        return task['species']

    def _task_converter(self, idea):
        return { 
                    "family": idea['family'],
                    "genus": idea['genus'],
                    "species": idea['species'],
                    "topic_image": f"Нарисуй животное породы '{idea['species']}' из рода '{idea['genus']}' семейства '{idea['family']}'. Эстетично, красиво, реалистично, крупным планом",
                    "topic_prompt": f"Расскажи интересный факт о животном породы '{idea['species']}' из рода '{idea['genus']}' семейства '{idea['family']}', используй не более {self.topic_word_limit} слов",
                }
    
    def _task_post_processor(self, tasks, *_):
        super()._task_post_processor(tasks, *_)
        tasks_len = len(tasks)
        offset_to_cat = tasks_len - 261
        for task in tasks:
            task['day'] = (task['day'] + offset_to_cat) % tasks_len

    def __init__(self, **kwargs):
        super().__init__(
            review_chat_id=-1002374309134,
            first_post_date=datetime(2025, 3, 11),
            text_generator=YandexTextGenerator(),
            image_generator=YandexImageGenerator(),
            send_text_with_image=True,
            topic_word_limit=100,
            **kwargs
        )