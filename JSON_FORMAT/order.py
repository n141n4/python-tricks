# sérialsation dans le même ordre que celui q'on a indiqué
from collections import OrderedDict
dct = OrderedDict()
dct[".__class__"] = "Playlist"
dct["name"] = "MeshowRandom"
dct["description"] = "Cool stuff."

import json
print(json.dumps(dct, indent=4))