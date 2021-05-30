from merge_args import merge_args

from LevelMetaData_pb2 import LevelMetaData
from google.protobuf.json_format import MessageToJson

def proto_resp(f):
    @merge_args(f)
    async def wrapped(proto_resp: bool, *args, **kwargs):
        r = await f(*args, **kwargs)
        if proto_resp:
            return MessageToJson(r.to_proto())
        else:
            return r
    return wrapped