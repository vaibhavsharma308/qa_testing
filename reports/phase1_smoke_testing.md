# Phase 1 — Smoke Testing Report ✅ PASSED

**Website:** https://bharatneurotech.com  
**Date:** 2026-07-03  
**Tester:** Automated Script + Browser Verification  
**Script:** [phase1_smoke_test.py](../scripts/phase1_smoke_test.py)  
**Raw Data:** [phase1_results.json](../results/phase1_results.json)

---

## Phase 1.1: HTTP Status Code Sweep ✅ PASSED

### Summary

| Metric | Result |
|---|---|
| **Sitemap URLs tested** | 245 |
| **Passed (200 OK)** | **245 / 245 (100%)** |
| **Failed (4xx/5xx)** | **0** |
| **Slow (>3s)** | **0** |
| **Bad lastmod dates** | 230 / 245 (93.9%) |

### Redirect Tests ✅

| Test | Status | Result |
|---|---|---|
| HTTP → HTTPS (`http://bharatneurotech.com/`) | **301** → https | ✅ |
| www → non-www (`https://www.bharatneurotech.com/`) | **302** → root | ✅ |
| Non-existent page → 404 | **404** returned | ✅ |

### Static Asset Tests ✅

| Asset | Status | Response Time |
|---|---|---|
| `/robots.txt` | 200 | 276ms |
| `/manifest.webmanifest` | 200 | 273ms |
| `/favicon.png` | 200 | 258ms |
| `/favicon-32.png` | 200 | 275ms |
| `/apple-touch-icon.png` | 200 | 268ms |
| `/og/home.jpg` | 200 | 362ms |

### Response Time Distribution

| Category | URLs | Avg | Fastest | Slowest |
|---|---|---|---|---|
| Core Pages | 10 | ~700ms | 72ms (`/contact`) | 1294ms (`/compliance`) |
| Compliance Hub | 13 | ~1200ms | 684ms (`/bis-stqc`) | 1643ms (`/iso-9001`) |
| AI Audit + City Pages | 18 | ~500ms | 80ms (`/kochi`) | 914ms (`/delhi`) |
| Consult + City Pages | 18 | ~500ms | 79ms (`/pune`) | 876ms (`/chennai`) |
| VS Comparison Pages | 14 | ~600ms | 85ms (`/mistral`) | 694ms (`/sarvam`) |
| Answers (SEO Pages) | 40+ | ~500ms | 61ms (`/ai-agent-platform`) | 2926ms (`/custom-ai-deployment`) |
| Hindi (/hi/) Pages | 15 | ~300ms | 61ms (`/hi/dr-sodhi`) | 923ms (`/hi/chatgpt-alternative`) |
| For Role/Industry Pages | 36 | ~250ms | 62ms (`/govtech/iso-42001`) | 1201ms (`/govtech/iso-27001`) |
| Glossary Pages | 25 | ~200ms | 62ms (`/dpia`) | 1181ms (`/neuromarketing`) |
| Journal Pages | 13 | ~200ms | 71ms (`/multimodal-ai`) | 788ms (`/iso-42001-roadmap`) |
| Data Endpoints | 5 | ~220ms | 60ms (`/rss.xml`) | 539ms (`/facts.json`) |

> **Note:** All response times are within acceptable limits. No URL exceeded 3 seconds.

### Full Crawl Log (All 245 URLs)

```
[  1/245] PASS  200   759ms  /
[  2/245] PASS  200   596ms  /ai-audit
[  3/245] PASS  200  1294ms  /compliance
[  4/245] PASS  200   661ms  /compliance/standards
[  5/245] PASS  200  1326ms  /compliance/iso-42001
[  6/245] PASS  200  1159ms  /compliance/iso-27001
[  7/245] PASS  200  1514ms  /compliance/iso-27701
[  8/245] PASS  200  1613ms  /compliance/soc2-type2
[  9/245] PASS  200  1197ms  /compliance/dpdp-2023
[ 10/245] PASS  200  1387ms  /compliance/gdpr
[ 11/245] PASS  200  1435ms  /compliance/nist-ai-rmf
[ 12/245] PASS  200   684ms  /compliance/bis-stqc
[ 13/245] PASS  200  1643ms  /compliance/iso-9001
[ 14/245] PASS  200   709ms  /compliance/hipaa
[ 15/245] PASS  200  1200ms  /compliance/cdsco-samd
[ 16/245] PASS  200   709ms  /compliance/hitrust-csf
[ 17/245] PASS  200   818ms  /trust
[ 18/245] PASS  200   691ms  /pricing
[ 19/245] PASS  200   788ms  /consult
[ 20/245] PASS  200   626ms  /custom-deployments
[ 21/245] PASS  200    93ms  /about
[ 22/245] PASS  200   726ms  /dr-sodhi
[ 23/245] PASS  200   892ms  /faq
[ 24/245] PASS  200   690ms  /lab
[ 25/245] PASS  200   789ms  /api
[ 26/245] PASS  200   125ms  /codemaster
[ 27/245] PASS  200   735ms  /mcp
[ 28/245] PASS  200   761ms  /credits
[ 29/245] PASS  200   722ms  /journal
[ 30/245] PASS  200    72ms  /contact
[ 31/245] PASS  200   594ms  /partnerships
[ 32/245] PASS  200   893ms  /careers
[ 33/245] PASS  200  1199ms  /support
[ 34/245] PASS  200   692ms  /vs/claude-gemini-gpt
[ 35/245] PASS  200   695ms  /vs/top-ai-models
[ 36/245] PASS  200    89ms  /ai-audit/mumbai
[ 37/245] PASS  200   914ms  /ai-audit/delhi
[ 38/245] PASS  200   757ms  /ai-audit/bengaluru
[ 39/245] PASS  200   687ms  /ai-audit/hyderabad
[ 40/245] PASS  200    86ms  /ai-audit/pune
[ 41/245] PASS  200   671ms  /ai-audit/chennai
[ 42/245] PASS  200    97ms  /ai-audit/kolkata
[ 43/245] PASS  200   669ms  /ai-audit/ahmedabad
[ 44/245] PASS  200   597ms  /ai-audit/gurugram
[ 45/245] PASS  200   676ms  /ai-audit/noida
[ 46/245] PASS  200   648ms  /ai-audit/kanpur
[ 47/245] PASS  200   626ms  /ai-audit/nagpur
[ 48/245] PASS  200    91ms  /ai-audit/indore
[ 49/245] PASS  200    91ms  /ai-audit/coimbatore
[ 50/245] PASS  200    80ms  /ai-audit/kochi
[ 51/245] PASS  200    92ms  /ai-audit/bhubaneswar
[ 52/245] PASS  200    82ms  /ai-audit/chandigarh
[ 53/245] PASS  200    88ms  /ai-audit/vadodara
[ 54/245] PASS  200   117ms  /consult/mumbai
[ 55/245] PASS  200    81ms  /consult/delhi
[ 56/245] PASS  200   626ms  /consult/bengaluru
[ 57/245] PASS  200   578ms  /consult/hyderabad
[ 58/245] PASS  200    79ms  /consult/pune
[ 59/245] PASS  200   876ms  /consult/chennai
[ 60/245] PASS  200    79ms  /consult/kolkata
[ 61/245] PASS  200   684ms  /consult/ahmedabad
[ 62/245] PASS  200    83ms  /consult/gurugram
[ 63/245] PASS  200   620ms  /consult/noida
[ 64/245] PASS  200   850ms  /consult/kanpur
[ 65/245] PASS  200    84ms  /consult/nagpur
[ 66/245] PASS  200   679ms  /consult/indore
[ 67/245] PASS  200   101ms  /consult/coimbatore
[ 68/245] PASS  200   667ms  /consult/kochi
[ 69/245] PASS  200    90ms  /consult/bhubaneswar
[ 70/245] PASS  200   588ms  /consult/chandigarh
[ 71/245] PASS  200   668ms  /consult/vadodara
[ 72/245] PASS  200   694ms  /vs/sarvam
[ 73/245] PASS  200   592ms  /vs/krutrim
[ 74/245] PASS  200    98ms  /vs/hanooman
[ 75/245] PASS  200   663ms  /vs/chatgpt
[ 76/245] PASS  200   687ms  /vs/claude
[ 77/245] PASS  200   582ms  /vs/gemini
[ 78/245] PASS  200   626ms  /vs/perplexity
[ 79/245] PASS  200   547ms  /vs/copilot
[ 80/245] PASS  200   691ms  /vs/deepseek
[ 81/245] PASS  200   690ms  /vs/grok
[ 82/245] PASS  200    85ms  /vs/mistral
[ 83/245] PASS  200   593ms  /vs/llama
[ 84/245] PASS  200   614ms  /vs/cohere
[ 85/245] PASS  200   582ms  /answers/best-indian-ai-model-2026
[ 86/245] PASS  200   655ms  /answers/chatgpt-alternative-india
[ 87/245] PASS  200    76ms  /answers/ai-audit-cost-india
[ 88/245] PASS  200   578ms  /answers/iso-42001-audit-india
[ 89/245] PASS  200   592ms  /answers/dpdp-compliance-checklist
[ 90/245] PASS  200   758ms  /answers/legal-ai-india
[ 91/245] PASS  200  2926ms  /answers/custom-ai-deployment-india
[ 92/245] PASS  200   610ms  /answers/ai-agent-india
[ 93/245] PASS  200   648ms  /answers/neuromarketing-india
[ 94/245] PASS  200   615ms  /answers/neuroforensics-india
[ 95/245] PASS  200   833ms  /answers/openai-api-alternative-india
[ 96/245] PASS  200   595ms  /answers/hindi-ai-chatbot
[ 97/245] PASS  200   687ms  /answers/soc-2-audit-india-cost
[ 98/245] PASS  200    77ms  /answers/iso-27001-consultant-india
[ 99/245] PASS  200   580ms  /answers/ai-governance-india
[100/245] PASS  200    91ms  /answers/code-copilot-india
[101/245] PASS  200   640ms  /answers/dpdp-fine-amount
[102/245] PASS  200    83ms  /answers/book-ai-consultant-india
[103/245] PASS  200    72ms  /answers/ai-audit-firm-india
[104/245] PASS  200    98ms  /answers/neurocortex-vs-chatgpt
[105/245] PASS  200   597ms  /answers/openai-compatible-indian-api
[106/245] PASS  200    74ms  /answers/code-assistant-india
[107/245] PASS  200    76ms  /answers/dpdp-audit-checklist
[108/245] PASS  200    86ms  /answers/iso-42001-lead-auditor-india
[109/245] PASS  200   685ms  /answers/sovereign-ai-india
[110/245] PASS  200    85ms  /answers/ai-consultant-lucknow
[111/245] PASS  200   819ms  /answers/razorpay-ai-billing
[112/245] PASS  200    61ms  /answers/ai-agent-platform-india
[113/245] PASS  200    89ms  /answers/webcontainer-code-india
[114/245] PASS  200   663ms  /answers/multimodal-ai-india
[115/245] PASS  200    89ms  /answers/ai-model-comparison-india
[116/245] PASS  200   785ms  /answers/bfsi-ai-audit-india
[117/245] PASS  200   106ms  /answers/healthtech-ai-compliance
[118/245] PASS  200   663ms  /answers/edtech-ai-dpdp-child
[119/245] PASS  200   586ms  /answers/ecommerce-ai-audit
[120/245] PASS  200   688ms  /answers/saas-ai-soc2-india
[121/245] PASS  200    75ms  /answers/govtech-ai-india-audit
[122/245] PASS  200    70ms  /answers/cto-ai-strategy-india
[123/245] PASS  200   771ms  /answers/founder-mvp-ai-india
[124/245] PASS  200    73ms  /answers/dpo-india-audit
[125/245] PASS  200    77ms  /answers/openai-vs-neurocortex
[126/245] PASS  200   609ms  /answers/ai-refund-policy-india
[127/245] PASS  200    77ms  /answers/iso-42001-cost-india
[128/245] PASS  200   706ms  /answers/ai-model-india-inr-billing
[129/245] PASS  200    72ms  /answers/codemaster-india
[130/245] PASS  200   792ms  /answers/mcp-india
[131/245] PASS  200   565ms  /answers/dpdp-fine-amount
[132/245] PASS  200   688ms  /answers/sovereign-ai-india
[133/245] PASS  200    99ms  /answers/ai-audit-bangalore
[134/245] PASS  200    80ms  /answers/ai-audit-mumbai
[135/245] PASS  200    78ms  /answers/ai-audit-delhi
[136/245] PASS  200    74ms  /answers/aeo-india
[137/245] PASS  200   696ms  /answers/webcontainer-india
[138/245] PASS  200   583ms  /answers/razorpay-ai
[139/245] PASS  200    75ms  /answers/custom-llm-india
[140/245] PASS  200   699ms  /answers/iso-42001-lead-auditor-india
[141/245] PASS  200    98ms  /answers/aarya-agent
[142/245] PASS  200    92ms  /hi/neurocortex-v3
[143/245] PASS  200   105ms  /hi/ai-audit
[144/245] PASS  200   622ms  /hi/consult
[145/245] PASS  200    73ms  /hi/custom-deployments
[146/245] PASS  200    79ms  /hi/codemaster
[147/245] PASS  200    68ms  /hi/api
[148/245] PASS  200    74ms  /hi/pricing
[149/245] PASS  200    61ms  /hi/dr-sodhi
[150/245] PASS  200    69ms  /hi/software-neurotechnology
[151/245] PASS  200    72ms  /hi/iso-42001
[152/245] PASS  200   633ms  /hi/dpdp
[153/245] PASS  200    80ms  /hi/chat
[154/245] PASS  200    65ms  /hi/sarvam-alternative
[155/245] PASS  200   923ms  /hi/chatgpt-alternative
[156/245] PASS  200    91ms  /hi/neuromarketing
[157/245] PASS  200    65ms  /hi
[158/245] PASS  200    74ms  /for/cto
[159/245] PASS  200   693ms  /for/ciso
[160/245] PASS  200    92ms  /for/dpo
[161/245] PASS  200    80ms  /for/founder
[162/245] PASS  200   595ms  /for/product-manager
[163/245] PASS  200    89ms  /for/compliance-head
[164/245] PASS  200    73ms  /for/bfsi/dpdp
[165/245] PASS  200    73ms  /for/bfsi/iso-42001
[166/245] PASS  200    73ms  /for/bfsi/soc-2
[167/245] PASS  200    93ms  /for/bfsi/iso-27001
[168/245] PASS  200    70ms  /for/bfsi/gdpr
[169/245] PASS  200    77ms  /for/healthtech/dpdp
[170/245] PASS  200    77ms  /for/healthtech/iso-42001
[171/245] PASS  200    81ms  /for/healthtech/soc-2
[172/245] PASS  200    69ms  /for/healthtech/iso-27001
[173/245] PASS  200    65ms  /for/healthtech/gdpr
[174/245] PASS  200    82ms  /for/edtech/dpdp
[175/245] PASS  200    91ms  /for/edtech/iso-42001
[176/245] PASS  200    79ms  /for/edtech/soc-2
[177/245] PASS  200    70ms  /for/edtech/iso-27001
[178/245] PASS  200    85ms  /for/edtech/gdpr
[179/245] PASS  200    72ms  /for/ecommerce/dpdp
[180/245] PASS  200    90ms  /for/ecommerce/iso-42001
[181/245] PASS  200    69ms  /for/ecommerce/soc-2
[182/245] PASS  200    75ms  /for/ecommerce/iso-27001
[183/245] PASS  200    70ms  /for/ecommerce/gdpr
[184/245] PASS  200    67ms  /for/saas/dpdp
[185/245] PASS  200    81ms  /for/saas/iso-42001
[186/245] PASS  200   728ms  /for/saas/soc-2
[187/245] PASS  200    91ms  /for/saas/iso-27001
[188/245] PASS  200    79ms  /for/saas/gdpr
[189/245] PASS  200    83ms  /for/govtech/dpdp
[190/245] PASS  200    62ms  /for/govtech/iso-42001
[191/245] PASS  200    79ms  /for/govtech/soc-2
[192/245] PASS  200  1201ms  /for/govtech/iso-27001
[193/245] PASS  200    72ms  /for/govtech/gdpr
[194/245] PASS  200    78ms  /india-ai-index
[195/245] PASS  200    71ms  /dpdp-tracker
[196/245] PASS  200    91ms  /state-of-iso-42001-india
[197/245] PASS  200   539ms  /facts.json
[198/245] PASS  200    63ms  /api/public/citations.json
[199/245] PASS  200    60ms  /journal/rss.xml
[200/245] PASS  200    76ms  /glossary
[201/245] PASS  200    69ms  /glossary/iso-42001
[202/245] PASS  200    73ms  /glossary/dpdp
[203/245] PASS  200    77ms  /glossary/iso-27001
[204/245] PASS  200    75ms  /glossary/iso-27701
[205/245] PASS  200    79ms  /glossary/soc-2
[206/245] PASS  200    76ms  /glossary/gdpr
[207/245] PASS  200    73ms  /glossary/nist-ai-rmf
[208/245] PASS  200    65ms  /glossary/hipaa
[209/245] PASS  200    83ms  /glossary/moe
[210/245] PASS  200    72ms  /glossary/mcp
[211/245] PASS  200   664ms  /glossary/agentic-ai
[212/245] PASS  200   106ms  /glossary/agent-mode
[213/245] PASS  200    73ms  /glossary/deep-thinking-mode
[214/245] PASS  200    77ms  /glossary/context-window
[215/245] PASS  200    80ms  /glossary/inference
[216/245] PASS  200    83ms  /glossary/rag
[217/245] PASS  200    76ms  /glossary/llm
[218/245] PASS  200    74ms  /glossary/prompt-injection
[219/245] PASS  200    73ms  /glossary/owasp-llm-top-10
[220/245] PASS  200    84ms  /glossary/ai-impact-assessment
[221/245] PASS  200    83ms  /glossary/sdf
[222/245] PASS  200    62ms  /glossary/dpia
[223/245] PASS  200  1181ms  /glossary/neuromarketing
[224/245] PASS  200    77ms  /glossary/neuro-forensics
[225/245] PASS  200    73ms  /glossary/software-neurotechnology
[226/245] PASS  200    71ms  /glossary/sovereign-ai
[227/245] PASS  200    70ms  /glossary/codemaster
[228/245] PASS  200    75ms  /glossary/webcontainer
[229/245] PASS  200    69ms  /glossary/aeo
[230/245] PASS  200    79ms  /glossary/razorpay
[231/245] PASS  200   788ms  /journal/iso-42001-roadmap
[232/245] PASS  200    76ms  /journal/neurocortex-chat-india
[233/245] PASS  200    79ms  /journal/ai-audit-india-2026
[234/245] PASS  200    78ms  /journal/iso-42001-dpdp-india-2026
[235/245] PASS  200    87ms  /journal/consult-dr-sodhi-india
[236/245] PASS  200    80ms  /journal/custom-ai-deployment-india
[237/245] PASS  200   100ms  /journal/neuromarketing-india-2026
[238/245] PASS  200    80ms  /journal/ai-governance-india-2026
[239/245] PASS  200    76ms  /journal/ai-governance-auditing-guide
[240/245] PASS  200    72ms  /journal/iso-42001-audit-guide-india
[241/245] PASS  200    95ms  /journal/dpdp-compliance-checklist-2026
[242/245] PASS  200    72ms  /journal/agent-mode-vs-deep-thinking
[243/245] PASS  200    71ms  /journal/multimodal-ai-india-use-cases
[244/245] PASS  200    90ms  /journal/neuro-forensics-india-guide
[245/245] PASS  200    76ms  /journal/mental-health-ai-india-2026
```

### Extra URL Tests

```
PASS  200   276ms  robots.txt
PASS  200   273ms  manifest.webmanifest
PASS  200   258ms  favicon.png
PASS  200   275ms  favicon-32.png
PASS  200   268ms  apple-touch-icon.png
PASS  200   362ms  og/home.jpg
PASS  301    44ms  http://bharatneurotech.com/ → https://bharatneurotech.com/
PASS  302  2237ms  https://www.bharatneurotech.com/ → https://bharatneurotech.com/
PASS  404    66ms  /this-page-should-not-exist-qa-test (404 as expected)
```

---

## Phase 1.2: Console Error Sweep ✅ PASSED

Browser testing conducted on 3 critical pages.

### Page 1: Chat Lab (`/lab`) ✅ PASS

| Check | Result |
|---|---|
| Page Title | `Chat NeuroCortex v3 · India's AI that understands the human brain` |
| Console JS Errors | None |
| Failed Network Requests | None |
| Visual Layout Issues | None |
| Chat Interface Functional | ✅ Sent test message, received structured AI response |

**UI Elements Verified:**
- ✅ Header with logo, green "Live" status dot, menu, "OPEN THE LAB" CTA
- ✅ Mode toggles: "AGENT MODE OFF", "DEEP THINKING MODE OFF", "WEB SEARCH OFF"
- ✅ Utility buttons: RERUN, .PDF, RESET
- ✅ NeuroCortex v3 system message
- ✅ Quick-start cards: "Decode a conversation", "Understand a person", "Talk through something"
- ✅ Chat textarea with attach (📎), pricing (≈ ₹0.50), voice (🎤), SEND button
- ✅ Dr. Sodhi consultation banner at bottom
- ✅ Footer CTAs: CUSTOM AI BUILD, RUN AN AI AUDIT · ₹1,799, CREATE ACCOUNT

**Functional Test Result:** Sent "Hello NeuroCortex, this is a QA test." → Received structured response with validation vectors.

### Page 2: Pricing (`/pricing`) ✅ PASS

| Check | Result |
|---|---|
| Page Title | `Pricing · ₹1,799 AI audit · ₹10 daily credits · NeuroCortex` |
| Console JS Errors | None |
| Failed Network Requests | None |
| Visual Layout Issues | None |

**Pricing Values Verified:**

| Price Point | Expected | Found | Status |
|---|---|---|---|
| Chat per message | ₹0.50 | `₹0.50 PER MESSAGE · NEVER PER TOKEN` | ✅ |
| Signup credit | ₹501 | `₹501 Shagun on signup` | ✅ |
| Daily free credits | ₹10 | `₹10 FREE CREDITS DAILY` | ✅ |
| AI Audit | ₹1,799 | `₹1,799 flat` | ✅ |
| Consultation | ₹2,500/hr | `₹2,500/hr` | ✅ |

**CTA Buttons Verified:**
- ✅ `CREATE ACCOUNT · CLAIM ₹501 SHAGUN →`
- ✅ `Run a ₹1,799 guided audit →`
- ✅ `Book Dr. Sodhi · ₹2,500/hr →`

**Additional Verified:**
- ✅ INR currency: "ALL PRICES IN INR · ₹1,000 ≈ $11.90 USD"
- ✅ Payment methods: UPI, Cards, Net-Banking, WhatsApp NEFT
- ✅ Trust badges: Apollo, APA, IAF, UP Police
- ✅ ISO badges: 42001, 27001, 27701

---

## Issues Found

| # | Severity | Issue | Impact | Recommended Fix |
|---|---|---|---|---|
| 1 | 🟡 Medium | 230/245 sitemap URLs have `lastmod=1970-01-01` | Reduced Google crawl efficiency | Update sitemap generation to use real timestamps |

---

## Phase 1 Verdict

| Sub-Phase | Status |
|---|---|
| 1.1 HTTP Status Sweep | ✅ **PASSED** — 245/245 healthy |
| 1.2 Console Error Sweep | ✅ **PASSED** — 0 JS errors, chat functional, pricing correct |
| **Overall** | ✅ **PHASE 1 PASSED** |
