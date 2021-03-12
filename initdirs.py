import os
import sys

for module_dir in ('pdata', ): 
    m_path = os.path.join(os.environ['CODEROOT'], module_dir)
    if m_path not in sys.path:
        sys.path.append(m_path)