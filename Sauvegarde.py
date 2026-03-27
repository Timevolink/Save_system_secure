from Save import *
from Load import *
import json

data = {
    "pseudo": "Tim3volink",
    "level": 1
}

text = json.dumps(data)

sv = Save(text)
ld = Load()

sv.save()