from backend_dmdb.settings import *

DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "NAME": "dmdb-backend",
        "HOST": "mongodb+srv://bamba:Cleta@1992@dmdbcluster.5d3po.mongodb.net/test",
        'USER': "bamba",
        'PASSWORD': "Cleta@1992",
    }
}

DEBUG=True
SECRET_KEY='d&t@$o0n-+*#kzs_-!q451xx@&s0bm3@vzg&60v(su&1k1^wfm'