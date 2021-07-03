import mongoengine
import os
# from dotenv import load_dotenv

# load_dotenv()
srv_uri = os.getenv('MONGODB_SRV')


def mongo_init_():
    # mongoengine.register_connection(alias='NetData', name='NetData')
    db_uri = str(srv_uri)
    mongoengine.connect(host=db_uri, alias='NetData')
