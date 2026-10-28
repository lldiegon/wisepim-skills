# WisePIM skills

Sixteen public workflows for product information management in Claude, ChatGPT and Codex. They coordinate authenticated WisePIM tools for catalog quality, product research, native enrichment and translation, commerce/SEO analysis, supplier evidence, images, taxonomy, prompts and native catalog jobs.

| Skill | Purpose |
| --- | --- |
| `analyze-commerce-performance` | Analyze available WisePIM imported-order metrics and period comparisons with explicit store, currency, date basis and source completeness. |
| `assess-product-images` | Assess stored WisePIM product-image evidence, identify missing or mismatched bindings and prepare reviewed native image improvement jobs. |
| `catalog-quality-audit` | Inspect a connected WisePIM catalog for stored quality scores, missing product fields and translation gaps, and prioritize evidence-based improvements. |
| `channel-readiness-review` | Review available WisePIM product evidence against explicit sales-channel requirements and identify gaps without claiming export, publication or channel certification. |
| `clean-catalog-data` | Prepare reviewed WisePIM bulk text cleanup such as find-and-replace, case normalization, whitespace trimming and explicitly requested field values. |
| `enrich-from-research` | Turn inspected WisePIM product research into a reviewed native enrichment operation while preserving evidence identity, source freshness and manual values. |
| `enrich-from-supplier-documents` | Inspect project-owned supplier documents, propose evidence-based field mappings and complete already imported supplier rows through reviewed WisePIM jobs. |
| `enrich-product-content` | Prepare native WisePIM enrichment of descriptions, short descriptions, titles, SEO metadata or attributes using project settings, saved prompts and reviewed selection. |
| `manage-enrichment-prompts` | Inspect and prepare reviewed updates to WisePIM saved prompts and enrichment settings while preserving prompt ownership, source hashes and unrelated settings. |
| `optimize-seo-performance` | Inspect persisted product-level GSC and GA4 evidence in WisePIM and propose targeted native SEO content improvements without claiming ranking uplift. |
| `organize-product-taxonomy` | Review WisePIM category, family and attribute vocabulary and product bindings, then prepare supported native taxonomy improvement jobs. |
| `prepare-product-translations` | Prepare and track native WisePIM product translations with explicit target locales, fields, frozen product selection and approval in WisePIM. |
| `prioritize-catalog-opportunities` | Rank selected WisePIM products for improvement using observed search or analytics evidence together with stored catalog quality gaps. |
| `remediate-channel-issues` | Inspect stored WisePIM channel issue evidence for selected products and prepare reviewed remediation without publishing products or claiming channel acceptance. |
| `research-product-facts` | Research selected WisePIM products on the web and inspect stored source-backed findings, exact identity, conflicts and missing evidence before catalog changes. |
| `run-catalog-improvement-jobs` | Prepare and monitor bounded native WisePIM catalog improvement jobs covering gap filling, supplier rows, images, category mapping and ad readiness. |

## Use and distribution

Each `skills/<name>/SKILL.md` is a standalone workflow. These instructions require the matching deployed WisePIM MCP tools and explicit account permissions. Installing instructions alone does not connect an account, deploy a service or establish a public directory listing. `tools.json` records the reviewed tool-name contract.

The [Claude package](https://github.com/lldiegon/wisepim-claude-plugin) and [ChatGPT package](https://github.com/lldiegon/wisepim-chatgpt-plugin) vendor a clean reviewed revision with source commit and file hashes. Edit canonical skills here, then rebuild those packages. The service is hosted from the private WisePIM frontend repository; Django remains authoritative for identity, permissions, approvals and native execution.

## Execution and evidence

Each connection authorizes one project. Research and catalog-job execution require their separate consent permissions; existing tokens do not acquire new scopes automatically. All consequential operations require authenticated WisePIM approval of an immutable preview. Native jobs retain their own review gates and recovery ownership. Respect explicit manual values, units, variant identity and source provenance. No automatic export or publication is implied.

Catalog-job budgets are ceilings on native estimates, not guarantees of final spend. Product-level analytics reads persisted evidence with coverage and freshness limits; measured changes do not establish causal uplift. Supplier evidence uses project-owned stored documents and supported extraction formats; new imports, unsupported PDF/OCR and arbitrary external fetches remain outside that read boundary. Native supplier jobs complete already imported rows. The runtime schema and returned capability status decide availability.

## Validation and contributing

```sh
python3 scripts/validate.py
```

`evals/scenarios.json` contains synthetic workflow behavior cases, including cross-project denial, missing tools, hostile evidence, approval, budgets, stale receipts and truthful outcomes. Static validation is not a live model/provider test. Keep credentials, customer data, internal listing strategy and private submission materials outside public source and archives. See [SECURITY.md](SECURITY.md) for reporting vulnerabilities.

MIT covers these instructions and tooling, not service access or customer data.
