# Example: classifying a natural cosmetics business

## Input

- **Business:** a brand that makes natural skincare cosmetics and also sells them online
- **Mode:** general (the user described the business, not a concrete list)
- **Language:** EN

## Output

```
## Classification proposal — natural cosmetics brand (manufacture + online retail)

Identified 3 potentially relevant Nice classes:

### 🔵 PRIORITY CLASSES (very likely)

**CLASS 3 — Cosmetics and cleaning preparations**
Why it is relevant: this is the core class for skincare cosmetics — creams, lotions,
soaps, essential oils for personal use.
Suggested terms:
- Cosmetic creams
- Non-medicated skin care preparations
- Essential oils
- Cosmetic soaps

### 🟡 CLASSES TO CONSIDER (depending on protection strategy)

**CLASS 35 — Advertising and retail services**
Why it might matter: the brand sells online. Class 35 covers the retail/online-store
service itself, which is distinct from the products in class 3. Worth protecting if the
online store is a meaningful part of the business.
Suggested terms:
- Retail services connected with the sale of cosmetics
- Online retail store services featuring cosmetics

### 🔴 CLASSES THAT MIGHT BE RELEVANT (discuss with counsel)
- Class 44: if the brand later offers beauty/skin-care treatments as a service (not just products)

---
NEXT STEPS
1. Review with the client which activities they want to protect
2. Decide which classes to file in (note: each extra class adds to the EUIPO fee)
3. Use detailed mode to generate the final goods/services list for the chosen classes
4. Validate and have counsel approve the specification before filing

LEGAL NOTICE
This proposal is indicative. The final selection of classes and terms must be
approved by the attorney responsible for the matter.
```

## Notes on this example

- **Class 3 vs class 35 is the classic trap.** Making and selling a product (class 3) is not the same right as the retail service of selling it (class 35). Counsel decides whether the online store warrants its own class given the extra fee.
- **Class 44 is flagged but not pushed** — it only becomes relevant if the business adds a treatment *service*. The skill surfaces it as an option to evaluate, not a recommendation.
- The terms shown are illustrative of harmonised-database wording; in a live run they would be confirmed via `validate_classification`, and anything unconfirmed marked `[?]`.
