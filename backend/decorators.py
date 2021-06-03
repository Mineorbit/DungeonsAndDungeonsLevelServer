from merge_args import merge_args
from google.protobuf.json_format import MessageToJson
from fastapi import Response
def proto_resp(f):
    @merge_args(f)
    async def wrapped(proto_resp: bool, *args, **kwargs):

        r = await f(*args, **kwargs)
        if proto_resp:
            return Response(content=r.to_proto().SerializeToString(), media_type="application/octet-stream")
        else:
            return r

    wrapped.__name__ = f.__name__
    return wrapped