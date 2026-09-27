# Token Recursion Engine (TREM)

> **Legacy LightMathematics computational research candidate — now separated into executable behavior and unverified architecture claims.**

The historical repository proposed a self-regulating recursion/memory layer for language models. The original README is preserved unchanged at [docs/LEGACY_TOKEN_RECURSION_ENGINE_SOURCE.md](docs/LEGACY_TOKEN_RECURSION_ENGINE_SOURCE.md).

## What the current code actually is

The extractable implementation is a **layered concept cache with optional HTTP persistence and explicit fallback synthesis**. It can:
- store a concept summary at a declared depth;
- retrieve the deepest matching stored concept;
- optionally POST/GET concept records through an external endpoint;
- distinguish local, external and inferred retrieval paths;
- cache an externally retrieved summary locally.

It does **not** currently inspect an LLM's hidden token activations, detect fractal attractors, measure recursion energy, automatically change model recursion depth, or prove improved reasoning.

## Constitutional/software status

| Field | State |
|---|---|
| Artifact | executable legacy prototype |
| Σ13 identity | not assigned |
| Canonical metrics | uncomputed |
| G1–G4 | open / not an admitted Sigma |
| Token-attractor detector | absent |
| Recursion-energy operator | absent |
| Adaptive depth controller | absent |
| Local layered cache | implemented |
| External HTTP persistence adapter | implemented as simple example |
| Provenance-aware fallback | implemented in reconstructed module |
| Benchmark evidence | absent |
| Production runtime authorization | NO |

## Key correction

The historical implementation calls its fallback `infer_missing_context`, but the code does not infer from embeddings or patterns. It returns a templated synthetic string. The reconstructed code therefore exposes this honestly as a fallback and attaches provenance.

Likewise, Python's built-in `hash()` is process-randomized, so the historical mock embedding is not a stable cross-process identifier. The reconstructed module uses deterministic SHA-256-derived demo vectors only for reproducible tests; they are **not semantic embeddings**.

## Repository map

- [Historical README](docs/LEGACY_TOKEN_RECURSION_ENGINE_SOURCE.md)
- [Constitutional/software status](CONSTITUTIONAL_STATUS.md)
- [Claim ledger](CLAIM_LEDGER.md)
- [Recoverable research value](RECOVERABLE_RESEARCH_VALUE.md)
- [Reconstruction dossier](RECONSTRUCTION_DOSSIER.md)
- [Executable prototype](src/token_recursion_engine.py)
- [Unit tests](tests/test_token_recursion_engine.py)

## Strongest surviving idea

The useful core is a governed retrieval ladder:

[
local state ightarrow external state ightarrow explicit synthetic fallback
]

with provenance attached to every result. This is potentially relevant to governed agent memory because retrieved evidence and generated reconstruction must never be silently conflated.

No claim of improved agent capability follows until comparative benchmarks are executed.
