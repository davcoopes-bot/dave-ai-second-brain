# FBA — Branding, GTIN Exemption & Dummy Listing

> **Category:** fba
> **Last updated:** 2026-05-28
> **Sources:** [[wiki/sources/src — LegacyX FBA Full Course (Thinkific).md]], [[wiki/sources/src — LegacyX FBA FAQ.md]]

## Summary

The full flow from choosing a brand name to having a ready-to-launch FNSKU barcode. This is the mandatory pre-launch setup sequence. Get it right once — you don't revisit it.

---

## Why We Don't Use Barcodes (UPC/EAN)

Amazon normally requires a GTIN (UPC or EAN barcode) to create a listing. We avoid this because:

- UPC barcodes are recycled — if someone previously owned your code, their old data can **overwrite your listing**
- If someone holds the barcode certificate for your code, they can **take over your listing entirely**
- GS1-issued barcodes are better but still create ownership complexity
- GTIN exemption removes this risk entirely — no barcode needed

**GTIN exemption = you can create Amazon listings without any barcode.** The service also unlocks your brand name on Amazon.

---

## Branding Decision: Why Not "Generic"

Every listing needs a brand. Listings marked "Generic" convert badly — buyers assume they're cheap, untrustworthy, or low quality. Even a nonsense brand name beats Generic.

**This does not mean you need Brand Registry.** Brand approval (what FBA Pro provides) just unlocks your brand name field in Amazon's catalogue. Brand Registry (which requires a trademark) is a separate, higher tier that gives you A+ Content and hijacker protection.

---

## Brand Name Selection

**Rules — do NOT use:**
- Common words or dictionary terms
- Simple misspellings of real words
- Category-specific terms (e.g. "Coffee Pro" for a coffee product)
- Anything trademarked by someone else
- Anything that exists on Amazon, Google, or GS1

**What works:**
- Random invented words ("Schmerley") — unique, passes all checks, no legal issues
- Pet name with vowels removed — quick, personal, passes checks
- Short made-up words that sound brandable

**4-step check before submitting:**
1. Google — search the name, look for existing brands or businesses
2. Amazon — search the name, confirm it's not registered
3. USPTO (https://www.uspto.gov/) — check for trademarks
4. GS1 — confirm no barcode ownership conflicts

---

## The FBA Pro Service

**URL:** www.agency-studios.com (formerly www.fba-pro.com)

FBA Pro provides a **combined GTIN exemption + brand approval service**. They use laser-etched product images to satisfy Amazon's brand approval requirement. This is the LegacyX-recommended path — mandatory for students.

**What the service does:**
1. Gets you a GTIN exemption on Amazon (no barcode needed for your listings)
2. Unlocks your brand name in Amazon's catalogue via laser-etched product images

**Cost & timing:** Managed through inhouse.legacyxfba.com — check there for current pricing. Allow ~5–7 days after brand approval for the dummy listing to settle.

---

## Dummy Listing Process

This is a 3-stage process. Follow it exactly.

### Stage 1 — Test Listing (FBA Pro handles this)
FBA Pro creates a test listing to get brand approval. This listing is for approval only — **delete it immediately after approval is confirmed.**

### Stage 2 — FNSKU Barcode Setting Fix ✅ DONE (2026-05-28)

Before creating any listing, change the default FBA barcode setting:

1. Go to **Settings → Fulfillment by Amazon → FBA Barcode Preference**
2. Change from "Manufacturer barcode" (default) to **"Amazon barcode"**
3. Click **Update**

**Why this matters:** The default "Manufacturer barcode" setting lets anyone with the same barcode sell against your listing — including hijackers. Amazon barcode means only your FNSKU controls the listing. Do this once and it's set for all future listings.

### Stage 3 — New Dummy Listing (2025 Interface — you create this)

After approval is confirmed and the FNSKU setting is fixed:

1. Go to **Add Products → Blank Form** (do not use AI tools or suggested products — manual setup avoids errors)
2. Enter your **approved brand name** with GTIN exemption (no UPC)
3. Choose the **same category as your competitors** — this is critical for ads and keyword indexing
4. Fill with placeholder data if final product specs are unknown
5. **Skip images** so the listing stays inactive while Amazon surfaces any compliance flags
6. Let the listing sit **5–7 days** before making any edits or creating a shipping plan

**Why the wait:** Amazon sometimes raises compliance issues in the first week. Better to catch them on a dummy listing with no inventory attached.

### Stage 4 — Get Your FNSKU Barcode
After the dummy listing is live and the 5–7 day window has passed, Amazon generates an **FNSKU barcode** for your product. This is what goes on every individual unit.

**Where to find it:** Manage Inventory → select your listing → Print Item Labels

The text on the FNSKU label doesn't matter. Only the **barcode and number** matter. This goes on every physical unit before it ships to Amazon.

---

## Variations — Launch Strategy

When creating a product with variations (sizes, colours, etc.):

- **Launch 2–3 variations maximum** — most revenue comes from the top 1–3 SKUs; more than 3 splits reviews and inventory inefficiently
- Variations use a **parent + child listing** structure:
  - Parent ASIN groups the children together but holds no sales data of its own
  - Child ASINs are the actual individual SKUs
- **Always create child listings first** → let them sit 5–7 days → then merge under a parent

**To create variations:**
1. Add Products → Blank Form → tick **"Has Variations"**
2. Set up child listings individually
3. After the 5–7 day wait, merge into parent

**Review stacking with variations:**
- Reviews accumulate at ~0.4–1% of sales per child listing
- The variation with the highest review % of total gets the highest revenue share
- This compounds — put your best seller as the easiest-to-find variation

---

## Brand Registry (Separate From Brand Approval)

Brand Registry requires a trademark application number and gives substantially more power than basic brand approval.

| Feature | Brand Approval | Brand Registry |
|---------|---------------|----------------|
| What it unlocks | Brand name in Amazon catalogue | A+ Content, Vine reviews, anti-hijack tools |
| Requirement | FBA Pro laser-etched images | USPTO trademark application number |
| Timing | Before listing creation | After launch — once revenue justifies it |
| Cost | Included in FBA Pro service | Trademark ~$500–2,000 + legal fees |

**Key rules for Brand Registry application:**
- Trademark must **exactly match** your brand name — case-sensitive (e.g. "MsWLL" not "mswll")
- Photos submitted must show branding on the **actual product or printed packaging** — NO stickers
- Avoid Fiverr trademark attorneys — use a real lawyer or file yourself carefully
- **Not required early** — prioritise after launch once you have consistent revenue to justify it

---

## Verifying GTIN Exemption & Brand Approval

**Do not trust Amazon's email.** Amazon's emails and catalog authorization notifications regularly show incorrect approval status.

**The only reliable way to verify:** Attempt to create a dummy listing with your brand name + GTIN exemption.
- If an **"Apply" button** appears → approval is missing. Reapply via FBA Pro.
- If it **proceeds to full listing creation** → approvals are active, regardless of what Amazon's email said.

For any GTIN or brand approval issues → contact FBA Pro support directly. For general questions → Facebook group.

---

## Barcode Types — Reference

| Barcode | What it is | Who creates it | Goes on |
|---------|-----------|----------------|---------|
| **UPC/GTIN** | Standard product identifier — Amazon normally requires this | GS1 or FBA Pro exemption | Replaced by exemption — not used |
| **FNSKU** | Amazon's internal per-unit identifier | Amazon generates after listing created | Every individual product unit |
| **Shipping label** | Identifies your box to Amazon's warehouse | Amazon generates when you create a shipping plan | Each carton/box |
| **Pallet label** | Rare — only needed if palletising shipments | Amazon generates | Pallet outer — rarely needed |

---

## Brand Approval vs Brand Registry

| | Brand Approval | Brand Registry |
|--|----------------|----------------|
| **What it does** | Unlocks your brand name field in Amazon catalogue | Gives A+ Content, hijacker protection, Vine reviews, enhanced brand tools |
| **How to get it** | FBA Pro service (laser-etched images) | USPTO trademark application number — apply separately |
| **When you need it** | Before creating any listing | After launch, once you have consistent revenue |
| **Cost** | Included in FBA Pro service | Trademark ~$500–2,000 + IP Accelerator law firm |
| **Photo requirement** | Laser-etched product images (FBA Pro handles) | Product or printed packaging with branding — no stickers |
| **MsWLL status** | ✅ APPROVED — all stores/countries (2026-05-27) | Not yet — post-launch priority |

---

## Status (MsWLL)

- ✅ Brand name selected: **MsWLL** (placeholder — nonsensical, passes all naming criteria)
- ✅ GTIN exemption files downloaded — Order **#GTIN-001134**, Agency Studios
- ✅ **GTIN exemption CONFIRMED** — submitted to Amazon under "Disposable Plates" and returned confirmed (2026-05-28)
- ✅ **Brand Qualification APPROVED** — MsWLL accepted across all stores/countries (2026-05-27)
- ✅ FBA barcode preference switched to Amazon barcode (2026-05-28)
- ⬜ **BLOCKED: Dummy listing** — course provides product + category at ~90% completion (currently 52%). Watch remaining modules first, then create dummy in correct category.
- ⬜ FNSKU barcode to be generated after dummy listing sits 5–7 days

**Revised sequence:** Watch course → hit 90% → get course-recommended product + category → create dummy listing → wait 5–7 days → generate FNSKU.

---

## Related Pages

- [[wiki/fba/fba-account-setup-legal.md]]
- [[wiki/fba/fba-launch-and-reviews.md]]
- [[wiki/fba/fba-compliance-suppression.md]]
- [[wiki/fba/fba-hijackers.md]]

## Open Questions

- What is the current FBA Pro pricing via inhouse.legacyxfba.com?
- When do we switch from MsWLL placeholder to the actual brand name?

## Revision History

- 2026-05-28 Major expansion from LegacyX Thinkific course (Creating Your First Listing module). Added: FNSKU barcode preference fix (Settings > FBA > FBA Barcode Preference → Amazon barcode), 2025 dummy listing creation steps (Blank Form, no AI tools, correct category, skip images, 5–7 day wait), variations launch strategy (2–3 max, child first then merge, review stacking at 0.4–1%), Brand Registry section (trademark requirements, photo rules, Fiverr warning, post-launch timing). Brand Approval vs Brand Registry table updated with photo requirements and MsWLL status.
- 2026-05-28 Brand Qualification approved for MsWLL across all stores/countries (2026-05-27 email from merch.service05@amazon.com). GTIN files confirmed ready for download. Status updated.
- 2026-05-24 Created. Source: LegacyX FBA Full Course (Thinkific) — Branding On Amazon module (all 8 lessons).
