---
last_verified: 2026-06
freshness_window: 12 months
freshness_category: stable
verified_against: WIPO Nice Classification (NCL) framework and EUIPO TMclass / harmonised database (HDB) concept
---

> **Note on freshness.** This reference describes the *structure* of the Nice Classification and the harmonised-database concept — stable background doctrine, not class-by-class term content. The live, version-specific term data is queried through the connector at run time, never bundled here; always rely on the connector's current data for actual wording.

# Nice Classification and the EUIPO harmonised database

## The Nice Classification

The Nice Classification (NCL) is the international system for classifying goods and services for trademark registration, established by the Nice Agreement (1957) and administered by WIPO. It divides all goods and services into **45 classes**:

- **Classes 1–34** — goods
- **Classes 35–45** — services

Each class has an official **class heading** that indicates, in general terms, the field to which the goods/services belong. Class headings are indicative, not exhaustive: a term not mentioned in the heading can still belong to the class, and the heading alone is generally not accepted as a full specification.

A new edition/version of the Nice Classification is published periodically; the version in force at the filing date governs. Always work against the current version exposed by the connector.

## Why classification matters

- **Scope of protection.** A trademark is protected only for the goods/services it is registered for, in the classes claimed. Mis-classification can leave the actual business activity unprotected.
- **Cost.** EUIPO fees are charged per class. The first class is included in the basic application fee; each additional class adds a fee. Class count is therefore a cost decision, not only a legal one.
- **Examination and opposition risk.** Vague or non-harmonised wording can trigger a classification deficiency (an examiner objection) and delays. Clear, harmonised wording reduces that risk.
- **Similarity analysis.** In likelihood-of-confusion assessment, similarity of goods/services is a core factor (Canon, C-39/97). Precise classification supports a cleaner conflict analysis later.

## The EUIPO harmonised database (HDB)

The EUIPO, together with national EU offices and observers, maintains a **harmonised database of goods and services** — a large set of pre-approved terms, each mapped to a Nice class, accepted across participating offices. Terms drawn from the HDB are accepted by the EUIPO without a classification objection.

The HDB is surfaced through **TMclass** (the EUIPO's classification tool) and the EUIPO Goods & Services API. Working from HDB terms is the most reliable way to build a specification that will pass examination smoothly.

Key practical points:
- A term **in** the HDB is safe to use as-is.
- A term **not** in the HDB is not necessarily wrong, but it is not pre-approved — it may be accepted, rejected, or queried by the examiner. Such terms should be flagged for attorney review, and a harmonised alternative offered where possible.
- The HDB is multilingual; the same concept has official wording in each EU language, which supports consistent multi-language specifications.

## Reference

- WIPO — Nice Classification: https://www.wipo.int/classifications/nice/en/
- EUIPO — TMclass and the harmonised database: https://euipo.europa.eu/ec2/ (TMclass)
- EUIPO Guidelines for Examination, Part B (Examination), Section 3 (Classification)
