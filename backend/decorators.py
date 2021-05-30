from merge_args import merge_args
from google.protobuf.json_format import MessageToJson

def proto_resp(f):
    @merge_args(f)
    async def wrapped(proto_resp: bool, *args, **kwargs):
        r = await f(*args, **kwargs)
        if proto_resp:
            return r.to_proto().SerializeToString()
        else:
            return r
    return wrapped