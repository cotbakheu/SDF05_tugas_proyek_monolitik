from typing import Callable, Dict, List, Optional
Loader = Callable[[], List[Dict]]
Saver = Callable[[List[Dict]], None]
Finder = Callable[[str], Optional[Dict]]