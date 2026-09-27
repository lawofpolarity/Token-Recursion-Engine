"""Constitutionally reconstructed Token Recursion Engine prototype.

This module implements retrieval/cache behavior only. It does not inspect LLM hidden
states, detect fractal attractors, or adapt model recursion depth.
"""
from dataclasses import dataclass
from hashlib import sha256
from typing import Any, Callable, Dict, Optional

@dataclass(frozen=True)
class RetrievalResult:
    key: str
    summary: str
    provenance: str  # LOCAL, EXTERNAL, SYNTHETIC
    level: Optional[int] = None

def deterministic_demo_vector(text: str, dimensions: int = 8):
    """Reproducible demo vector; NOT a semantic embedding."""
    digest=sha256(text.encode("utf-8")).digest()
    return tuple(b/255.0 for b in digest[:dimensions])

class TokenRecursionEngine:
    def __init__(self, depth: int = 3, external_fetch: Optional[Callable[[str], Optional[Dict[str,Any]]]]=None,
                 external_store: Optional[Callable[[str,Dict[str,Any]],None]]=None):
        if depth < 1:
            raise ValueError("depth must be >= 1")
        self.depth=depth
        self.layers=[{} for _ in range(depth)]
        self.external_fetch=external_fetch
        self.external_store=external_store

    def store_local(self, level: int, key: str, summary: str, source: str="LOCAL"):
        if not 0 <= level < self.depth:
            raise IndexError("level outside configured depth")
        self.layers[level][key]={"summary":summary,"source":source,"demo_vector":deterministic_demo_vector(summary)}

    def retrieve_local(self,key: str):
        for level in range(self.depth-1,-1,-1):
            if key in self.layers[level]:
                item=self.layers[level][key]
                return RetrievalResult(key,item["summary"],item.get("source","LOCAL"),level)
        return None

    def store(self,key: str,summary: str,level: int=0):
        self.store_local(level,key,summary)
        if self.external_store:
            self.external_store(key,{"summary":summary})

    def retrieve(self,key: str,allow_synthetic: bool=True):
        local=self.retrieve_local(key)
        if local:return local
        if self.external_fetch:
            ext=self.external_fetch(key)
            if ext and "summary" in ext:
                # Preserve external provenance when cached.
                self.store_local(self.depth-1,key,ext["summary"],source="EXTERNAL")
                return RetrievalResult(key,ext["summary"],"EXTERNAL",self.depth-1)
        if allow_synthetic:
            # Explicitly templated fallback: not evidence and not automatically persisted.
            return RetrievalResult(key,f"Inferred details about {key} based on known patterns.","SYNTHETIC",None)
        return None
