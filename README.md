# WISEPIM skills

Seventeen public workflows for product information management in Claude, ChatGPT and Codex. They coordinate authenticated WISEPIM tools for catalog quality, product research, native enrichment and translation, commerce/SEO analysis, supplier evidence, images, taxonomy, prompts and native catalog jobs.

| Skill | Purpose |
| --- | --- |
| `start-with-wisepim` | Create or resume an account, finish setup, and connect an agent with or without an installed plugin. |
| `analyze-commerce-performance` | Analyze available WISEPIM imported-order metrics and period comparisons with explicit store, currency, date basis and source completeness. |
| `assess-product-images` | Assess stored WISEPIM product-image evidence, identify missing or mismatched bindings and prepare bounded native image improvement jobs. |
| `catalog-quality-audit` | Inspect a connected WISEPIM catalog for stored quality scores, missing product fields and translation gaps, and prioritize evidence-based improvements. |
| `channel-readiness-review` | Review available WISEPIM product evidence against explicit sales-channel requirements and identify gaps without claiming export, publication or channel certification. |
| `clean-catalog-data` | Prepare bounded WISEPIM bulk text cleanup such as find-and-replace, case normalization, whitespace trimming and explicitly requested field values. |
| `enrich-from-research` | Turn inspected WISEPIM product research into a native enrichment operation while preserving evidence identity, source freshness and manual values. |
| `enrich-from-supplier-documents` | Inspect project-owned supplier documents, propose evidence-based field mappings and complete already imported supplier rows through bounded WISEPIM jobs. |
| `enrich-product-content` | Prepare native WISEPIM enrichment of descriptions, short descriptions, titles, SEO metadata or attributes using project settings, saved prompts and explicit selection. |
| `manage-enrichment-prompts` | Inspect and prepare bounded updates to WISEPIM saved prompts and enrichment settings while preserving prompt ownership, source hashes and unrelated settings. |
| `optimize-seo-performance` | Inspect persisted product-level GSC and GA4 evidence in WISEPIM and propose targeted native SEO content improvements without claiming ranking uplift. |
| `organize-product-taxonomy` | Review WISEPIM category, family and attribute vocabulary and product bindings, then prepare supported native taxonomy improvement jobs. |
| `prepare-product-translations` | Prepare and track native WISEPIM product translations with explicit target locales, fields, frozen product selection and the configured approval policy. |
| `prioritize-catalog-opportunities` | Rank selected WISEPIM products for improvement using observed search or analytics evidence together with stored catalog quality gaps. |
| `remediate-channel-issues` | Inspect stored WISEPIM channel issue evidence for selected products and prepare bounded remediation without publishing products or claiming channel acceptance. |
| `research-product-facts` | Research selected WISEPIM products on the web and inspect stored source-backed findings, exact identity, conflicts and missing evidence before catalog changes. |
| `run-catalog-improvement-jobs` | Prepare and monitor bounded native WISEPIM catalog improvement jobs covering gap filling, supplier rows, images, category mapping and ad readiness. |

## Use and distribution

Each `skills/<name>/SKILL.md` is a standalone workflow. These instructions require the matching deployed WISEPIM MCP tools and explicit account permissions. Installing instructions alone does not connect an account, deploy a service or establish a public directory listing. `tools.json` records the reviewed 53-tool contract. Catalog jobs use five separate typed estimate/preview/start families, and consequential execution uses twelve operation-specific tools. No generic execution dispatcher or runtime job-schema discovery is required.

The [Claude package](https://github.com/lldiegon/wisepim-claude-plugin) and [ChatGPT package](https://github.com/lldiegon/wisepim-chatgpt-plugin) vendor a clean reviewed revision with source commit and file hashes. Edit canonical skills here, then rebuild those packages. The service is hosted from the private WISEPIM frontend repository; Django remains authoritative for identity, permissions, approvals and native execution.

## Execution and evidence

Each connection authorizes one project. Research and catalog-job execution require their separate consent permissions; existing tokens do not acquire new scopes automatically. Consequential operations use immutable previews and the connection's configured approval policy. New connections default to approval off, allowing requested execution after preview without a browser confirmation. The account owner can enable required approval in WISEPIM connected apps settings; enabled gates require authenticated browser approval. Missing policy, stale sources or denied permissions never authorize a bypass. Native jobs retain their own review gates and recovery ownership. Respect explicit manual values, units, variant identity and source provenance. No automatic export or publication is implied.

Catalog-job budgets are ceilings on native estimates, not guarantees of final spend. Product-level analytics reads persisted evidence with coverage and freshness limits; measured changes do not establish causal uplift. Supplier evidence uses project-owned stored documents and supported extraction formats; new imports, unsupported PDF/OCR and arbitrary external fetches remain outside that read boundary. Native supplier jobs complete already imported rows. The runtime schema and returned capability status decide availability.

## Validation and contributing

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

`evals/scenarios.json` contains synthetic workflow behavior cases, including cross-project denial, missing tools, hostile evidence, approval, budgets, stale receipts and truthful outcomes. Static validation is not a live model/provider test. Keep credentials, customer data, internal listing strategy and private submission materials outside public source and archives. See [SECURITY.md](SECURITY.md) for reporting vulnerabilities.

MIT covers these instructions and tooling, not service access or customer data.

New here? Use `start-with-wisepim` before connecting any tools. It links native signup and standalone agent discovery, then uses authenticated setup evidence after connection. Product branding is always WISEPIM.
