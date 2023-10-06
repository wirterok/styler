import configparser
from styler.config import config as project_config

def override_migration_file(*args):
    config = configparser.ConfigParser()
    config.read('alembic.ini')
    config.set('alembic', 'sqlalchemy.url', project_config.alchemy_host)

    with open('alembic.ini', 'w') as configfile:
        config.write(configfile)