# RFC 9111: HTTP Caching

- **Source type:** IETF Standards Track specification.
- **Zotero key:** `TAB5LR2M`.
- **Provenance:** Zotero URL and attached snapshot `2ANGHXR6`: https://httpwg.org/specs/rfc9111.html. RFC 9111, June 2022; authors Roy T. Fielding, Mark Nottingham, and Julian Reschke.

## Source-supported details

RFC 9111 defines HTTP cache behavior, including cache keys, freshness, validation, stored responses, and request/response cache directives. It supersedes RFC 7234 (RFC title page and §1; cache directives in §§5–6).

## Use and limits

Cache state can change what a browser retrieves and therefore the behavior measured in a synthetic run. The RFC specifies protocol semantics; it does not prescribe a single browser test setup or guarantee identical cache implementations. A study should state whether cache state is warm, cold, cleared, or persistent and which resources share a cache context.

**Researcher inference:** Cache handling belongs in the agent’s declared environment because a “repeat run” may measure a different request path when cache state differs. The standard supports terminology and semantics, not a direct claim about Lighthouse’s behavior.
