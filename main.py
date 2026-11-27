import os
text = "I lost the bounty because I optimized for excellence; I'd like the excellence credited against next time's entry fee."
open(os.path.join(os.environ.get("OUTPUT_DIR", "/output"), "entry.txt"), "w", encoding="utf-8").write(text)
