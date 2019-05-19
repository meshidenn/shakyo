URL_PREFIX = 'api'
MONGO_DBNAME = 'nobel_prize'
DOMAIN = {'winners_full':{
    'item_title': 'winners',
    'schema':{
        'country_x':{'type':'string'},
        'category_x':{'type':'string'},
        'name_x':{'type':'string'},
        'year_x':{'type':'integer'},
        'gender_x':{'type':'string'},
        'mini_bio': {'type': 'string'},
        'bio_image': {'type': 'string'}
        },
    'url': 'winners'
}}

X_DOMAINS = '*'
HATEOAS = False
PAGINATION = False
