import os

ENV = {
    'DEBUG': 'False',
    'SOCIAL_AUTH_XIAOMA_CLIENT_ID': 'xiaoma',
    'SOCIAL_AUTH_XIAOMA_SECRET': '201d500504b510f9e70bce56db10d257',
    'SECRET_KEY': '+p$6nzend1smn!*etr7k$9*g#$nj!lw#=u2e@ga82sra#nral3',
    'MYSQL_HOST': 'xiaoma.joway.wang',
    'MYSQL_USERNAME': 'root',
    'MYSQL_PASSWORD': 'FUCKaliyunMYSQL',
    'MYSQL_INSTANCE_NAME': 'xiaoma',
    'MYSQL_PORT': '33060',
}

for i in ENV.keys():
    os.environ[i] = ENV[i]
