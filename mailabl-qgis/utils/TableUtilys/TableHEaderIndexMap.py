# header_index_map.py
from typing import List, Dict
from ...KeelelisedMuutujad.TableHeaders import TableHeaders_new, HeaderKeys


class HeaderIndexMap:
    """
    Maps logical header keys to column indexes in a list of actual header labels.
    """
    def __init__(self, header_labels: List[str], language: str = "et"):
        self._tbl = TableHeaders_new(language)
        self._map: Dict[str, int] = {}

        for key in HeaderKeys.ALL_HEADER_KEYS:
            label = self._tbl[key]
            if label in header_labels:
                self._map[key] = header_labels.index(label)
            #else:
            #    raise ValueError(f"Label '{label}' for key '{key}' not found in header_labels")

    def __getitem__(self, key: str) -> int:
        return self._map[key]

    def __getattr__(self, key: str) -> int:
        if key in self._map:
            return self._map[key]
        raise AttributeError(f"'HeaderIndexMap' has no attribute '{key}'")

    def keys(self) -> List[str]:
        return list(self._map.keys())
