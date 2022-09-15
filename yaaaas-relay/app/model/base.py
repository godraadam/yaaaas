from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

def todict(obj):
    excl = ("_sa_adapter", "_sa_instance_state")
    return {
        k: v
        for k, v in vars(obj).items()
        if not k.startswith("_") and not any(hasattr(v, a) for a in excl)
    }

class Base:
    id: Column(String, primary_key=True, )


Base = declarative_base(cls=Base)
