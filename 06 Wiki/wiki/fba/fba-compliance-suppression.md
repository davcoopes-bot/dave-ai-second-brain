# Amazon FBA — Compliance & Suppression Risks

> **Category:** fba
> **Last updated:** 2026-05-03
> **Sources:** [[wiki/sources/src — Amazon Product Detail Page Rules.md]]

---

## Overview

Amazon can suppress your listing (remove it from search results), suspend your selling privileges, or permanently terminate your account for policy violations. Most first-time sellers get caught by the same set of avoidable mistakes. This page documents every compliance rule extracted from Amazon's official Product Detail Page Rules policy, plus the practical risk level of each violation.

If your listing is suppressed, you stop making money while your ranking decays. Prevention is far cheaper than reinstatement.

---

## Suppression Risk — Quick Reference

| Rule | Risk Level | Source |
|------|-----------|--------|
| ALL CAPS in title or bullets | 🔴 High — auto-suppression | Official policy |
| Title over 200 characters | 🔴 High — auto-suppression | Official policy |
| Price/availability in listing copy | 🔴 High — auto-suppression | Official policy |
| URL or contact info in any field | 🔴 High — account warning | Official policy |
| Review requests in listing copy | 🔴 High — account warning | Official policy |
| Watermarks/logos on images | 🔴 High — image removed | Official policy |
| Creating duplicate ASIN | 🔴 High — both listings removed | Official policy |
| Listing new version under old ASIN | 🔴 High | Official policy |
| Unauthorised GTIN | 🔴 High — listing blocked | Official policy |
| Inaccurate categorisation | 🟠 Medium — suppression + warning | Official policy |
| Prohibited product claims | 🟠 Medium — suppression | Official policy |
| IP infringement in listing | 🟠 Medium — DMCA takedown | Official policy |
| Keyword stuffing | 🟡 Low-Medium — slow rank decay | Policy + algorithm |
| Not complying with category style guide | 🟡 Low — suppression possible | Official policy |

---

## Section 1 — Content Prohibited in ALL Fields

The following are banned from **titles, descriptions, bullet points, AND images**. Violation in any field is grounds for suppression or account action:

- Pornographic, obscene, or offensive content
- Phone numbers, email addresses, physical addresses, or website URLs
- Pricing or availability information (e.g. "Only $29.99!", "In Stock Now", "Free Shipping")
- Links to external websites for ordering or alternative shipping
- Spoilers for books, films, or music
- Customer reviews, quotes, or testimonials from any source
- Requests for positive customer reviews (including "Please leave us a 5-star review")
- Advertising, promotional material, or watermarks on images or videos
- Time-sensitive information (tour dates, seminar dates, expiry information)
- Brand-specific IP on a "generic" product listing
- Restricted phrases such as "FSA/HSA eligible" (without authorisation)

**Practical implication for Voya:** Every piece of copy must be reviewed against this list before submission. The most common first-time seller mistake is putting the price in bullets ("Great value at $29.99!") or adding a watermark to lifestyle images.

---

## Section 2 — Title-Specific Rules

- Hard maximum: **200 characters** including spaces (auto-rejected if exceeded)
- Recommended maximum: **80 characters** (mobile truncation)
- **Title Case required** — first letter of each word capitalised; no ALL CAPS throughout
- **No emojis or symbols at the beginning of each word**
- No HTML or code of any kind

**Risk:** Titles with ALL CAPS are auto-suppressed by Amazon's automated systems. This is one of the most common reasons new listings don't appear in search.

---

## Section 3 — Listing Accuracy Requirements

Amazon requires listings to be:
- **Accurately categorised** — wrong category = suppression and potentially worse
- **Clearly written** — titles, descriptions, and bullets must help customers understand the product
- **Truthful** — no misleading claims about quality, features, or characteristics

Reference: Amazon's [Prohibited Product Claims](https://sellercentral.amazon.com/help/hub/reference/external/G202024200) policy prohibits claims like:
- Unverified health or medical claims
- "Best" or "number one" without substantiation
- Environmental claims without certification (e.g. "eco-friendly", "green", "sustainable")
- Claims that imply government endorsement

---

## Section 4 — Adding New Listings (ASIN Creation Rules)

- **No duplicate ASINs** — if a product already exists in Amazon's catalogue, you cannot create a new page for it; you join the existing listing
- **GTINs must be authorised** — UPC/EAN/ISBN must come from GS1 or an authorised prefix owner; unauthorised codes are blocked at submission. **Exception: GTIN exemption** bypasses this entirely — our approach via FBA Pro. See [[wiki/fba/fba-branding-gtin.md]].
- **No false product identification** — cannot use a UPC you don't own or that belongs to a different product
- **No cross-promotion** — cannot use a product detail page to advertise or link to other products

---

## Section 5 — Editing Existing Listings

This section has serious implications for product iteration:

### New version = new ASIN (mandatory)
If you change **any** of the following, you **must create a new ASIN**:
- Colour
- Size
- Material
- Product features
- Product name

**Example from policy:** A streaming device that adds 2 buttons to its remote must be listed as a new ASIN. The same principle applies to a splatter screen that changes from silicone to stainless steel, or adds a new handle design.

**Practical implication for Voya:** Plan your product line so each variant that differs in material or features has its own ASIN from the start. Don't launch a "v1" and try to quietly update it to a materially different "v2" under the same listing.

### Re-branding requires a new ASIN
- Minor corrections (typo in brand name, capitalisation fix) can be edited
- Any real brand name change = new listing
- Never modify trademark information on an existing ASIN

### Permissible edits only
You may only edit listings to:
- Add clarifying details or additional information
- Fix grammatical errors
- Remove content that violates policy

You cannot:
- Repeatedly add and remove prohibited claims to evade detection — Amazon flags this as evasive behaviour with no reinstatement path
- Repeatedly add and remove prohibited images or content

---

## Section 6 — Brand Registry Compliance

- If multiple authorised users of a brand contribute to the same ASIN, Amazon's system weights contributions based on sales volume, refund rate, buyer feedback, and A-to-z claims
- Brand Administrators control selling roles — Voya needs a clear Brand Admin designated from day one
- Contributions by authorised brand users cannot be edited by Seller Support — incorrect info must be reported via Account Health → Report Abuse

---

## Actionable Takeaways

1. **Run every listing through the prohibited content checklist before submitting** — especially images (watermarks) and copy (prices, URLs, review requests)
2. **Get a GS1 GTIN before you create any ASIN** — do not use a third-party barcode reseller; only GS1-issued codes are accepted
3. **Plan your product variants as separate ASINs from day one** — if you think you'll ever change the material or add a significant feature, that's a new ASIN
4. **Register the Voya brand before creating listings** — Brand Registry changes the rules around your own listings in your favour
5. **Never keyword stuff** — Amazon's auto-systems penalise it and it creates suppression risk over time
6. **Title Case, always** — implement a checklist for anyone who writes Voya copy

---

## Mistakes to Avoid

- Copying a competitor's title and accidentally copying their ALL CAPS styling
- Using a cheap third-party barcode in a hurry — the listing gets blocked
- Updating an existing listing when launching a new colourway or size — create a new ASIN
- Putting promotional copy in bullets ("Buy 2 and save!")
- Adding review request language to packaging inserts or listing copy ("We'd love a 5-star review!")
- Relaunching a "v2" product under the old ASIN after making material changes

---

## How This Applies to Voya

- Voya's brand identity depends on clean, professional listings — compliance protects that
- Before any Voya ASIN goes live, it should pass a 10-point compliance check against this page
- The silicone splatter screen and cable management box are both new product categories for Voya — build them correctly from the start, don't copy competitors who may themselves be non-compliant
- Designate a Brand Admin in Brand Registry before inviting any co-sellers or contributors

---

---

## Restricted vs Prohibited Products

From LegacyX Thinkific course — Product Research module:

**Prohibited products** — completely banned on Amazon. No selling allowed:
- Guns, firearms, ammunition
- Brass knuckles and offensive weapons
- Adult/pornographic content
- Other items on Amazon's prohibited list

**Restricted products** — allowed to sell but require pre-approval or paperwork:
- Supplements (requires GMP certs, FDA compliance — one reason gummies were complex for a first product)
- Electronics with batteries (safety certs required)
- Kids' products (CPSC safety certificates required)
- Medical devices (FDA clearance)

**Advertising-restricted categories** — can sell, but cannot run Amazon ads:
- Tobacco accessories
- Adult products
- Certain medical/health products

**Critical check before ordering stock:** Always create a dummy listing to test if your product category requires category approval. Find out the hard way before you've paid for 500 units, not after. 

Amazon restricted products list: https://sellercentral.amazon.com/help/hub/reference/external/G200164330?locale=en-US

---

## Related Pages

- [[wiki/fba/fba-listing-optimisation.md]]
- [[wiki/fba/fba-ranking-factors.md]]
- [[wiki/fba/fba-research-overview.md]]
- [[wiki/sources/src — Amazon Product Detail Page Rules.md]]

---

## Revision History

- 2026-05-03: Created. Source: Amazon Seller Central Product Detail Page Rules (official policy).
