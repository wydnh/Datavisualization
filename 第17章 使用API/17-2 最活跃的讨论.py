import requests
from operator import itemgetter
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('status_code:', r.status_code)

submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:5]:
    # 对于每篇文章,都执行一次API调用
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()
    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0),
    }
    submission_dicts.append(submission_dict)

# submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)
submission_dicts = sorted(submission_dicts, key=lambda a: a['comments'], reverse=True)
names, comments = [], []
for submission_dict in submission_dicts:
    print('\nTitle:', submission_dict['title'])
    print('Discussion link:', submission_dict['link'])
    print('comments:', submission_dict['comments'])
    name = submission_dict['title']
    names.append(name)
    comment = {
        'value': submission_dict['comments'],
        'label': submission_dict['title'],
        'xlink': submission_dict['link'],
    }
    comments.append(comment)

my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 700

chart = pygal.Bar(my_config, style=my_style)
chart.x_labels = names
chart.add('', comments)
chart.title = '最活跃的讨论'
chart.render_to_file('17-2 最活跃的讨论.svg')
