import sys 
from pathlib import Path 
 
# Add src directory to path 
src_path = Path(__file__) / "src" 
sys.path.insert(0, str(src_path)) 