from typing import Callable, Dict, List, Optional
from typing import Union
from pathlib import Path

Loader = Callable[[Union[Path, str]], List[Dict]]
Saver = Callable[[List[Dict]], None]
Finder = Callable[[str], Optional[Dict]]