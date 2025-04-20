#!/usr/bin/env python

import os
from dictorius import server

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    server.app.run(host="0.0.0.0", port=port)
