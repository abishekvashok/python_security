# Usage:
# $ cd ~/python_security
# $ python3 -m scripts.generate_sink_list > sinks.json

import json

from code_execution.execution_base import get_exploits, ExploitEncoder

all_exploits = get_exploits(exclude_abstract=False)
exploits_with_function = [exploit for exploit in all_exploits if exploit.vulnerable_function]

print(ExploitEncoder(indent=2).encode(exploits_with_function))
