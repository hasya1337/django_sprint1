from django.shortcuts import render

# /app/tests/test_templates.py:41: AssertionError: Убедитесь, что в словаре контекста для страницы `posts/2/` под
# ключом `post` передаётся словарь с `"id": 2` из списка `posts`. /app/tests/test_views.py:8: AssertionError:
# Убедитесь, что список с постами `posts` из файла `blog/views.py` соответствуют списку из задания.
# не получается пройти автотесты если изменить список posts на словарь

posts = [
    {
        'id': 0,
        'location': 'Остров отчаянья',
        'date': '30 сентября 1659 года',
        'category': 'travel',
        'text': '''Наш корабль, застигнутый в открытом море 
                страшным штормом, потерпел крушение. 
                Весь экипаж, кроме меня, утонул; я же, 
                несчастный Робинзон Крузо, был выброшен 
                полумёртвым на берег этого проклятого острова, 
                который назвал островом Отчаяния.'''
    },
    {
        'id': 1,
        'location': 'Остров отчаянья',
        'date': '1 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Проснувшись поутру, я увидел, что наш корабль сняло 
                с мели приливом и пригнало гораздо ближе к берегу. 
                Это подало мне надежду, что, когда ветер стихнет, 
                мне удастся добраться до корабля и запастись едой и 
                другими необходимыми вещами. Я немного приободрился, 
                хотя печаль о погибших товарищах не покидала меня. 
                Мне всё думалось, что, останься мы на корабле, мы 
                непременно спаслись бы. Теперь из его обломков мы могли бы 
                построить баркас, на котором и выбрались бы из этого 
                гиблого места.'''
    },
    {
        'id': 2,
        'location': 'Остров отчаянья',
        'date': '25 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Всю ночь и весь день шёл дождь и дул сильный 
                порывистый ветер. 25 октября.  Корабль за ночь разбило 
                в щепки; на том месте, где он стоял, торчат какие-то 
                жалкие обломки, да и те видны только во время отлива. 
                Весь этот день я хлопотал около вещей: укрывал и 
                укутывал их, чтобы не испортились от дождя.'''
    }
]

def index(request):
    reversed_posts = posts[::-1]
    return render(request, 'blog/index.html', {'posts': reversed_posts})

def post_detail(request, id):
    post = next((post for post in posts if post['id'] == id), None)
    return render(request, 'blog/detail.html', {'post': post})

def category_posts(request, category_slug):
    filtered_posts = [post for post in posts if post['category'] == category_slug]
    return render(request, 'blog/category.html', {'posts': filtered_posts, 'category_slug': category_slug})

# Remove trailing whitespace and add a newline at the end of the file.
