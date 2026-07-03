# QA Testing Plan — bharatneurotech.com (Market-Ready Launch)

A comprehensive quality assurance testing strategy for the full Bharat NeuroTech website, covering **245+ URLs** across **14 testing dimensions** to ensure market-readiness.

---

## Site Architecture Summary (from Sitemap Analysis)

| Section | Pages | Priority |
|---|---|---|
| **Core Pages** (Home, Pricing, Trust, About, Dr. Sodhi, FAQ, Contact, Support, Careers, Partnerships) | ~10 | 1.0–0.6 |
| **Product Pages** (NeuroCortex v3, CodeMaster, MCP, API, Credits, Lab) | ~6 | 0.85–0.6 |
| **Compliance Hub** (ISO 42001, 27001, 27701, SOC2, DPDP, GDPR, NIST, BIS, HIPAA, CDSCO, HITRUST, ISO 9001) | ~13 | 0.95–0.85 |
| **AI Audit** (Main + 17 city landing pages) | ~18 | 1.0–0.8 |
| **Consult** (Main + 17 city landing pages) | ~18 | 0.9–0.8 |
| **Custom Deployments** | 1 | 0.95 |
| **VS Comparison Pages** (Top AI, ChatGPT, Claude, Gemini, DeepSeek, Grok, etc.) | ~14 | 0.90–0.85 |
| **Answers (SEO)** (~40+ long-tail keyword pages) | ~40+ | 0.75 |
| **Hindi (/hi/) Localization** (~15 pages) | ~15 | 0.80 |
| **For [Role] Landing** (CTO, CISO, DPO, Founder, PM, Compliance Head) | ~6 | 0.80 |
| **For [Industry/Standard]** (BFSI, HealthTech, EdTech, E-commerce, SaaS, GovTech × 5 standards) | ~30 | 0.75 |
| **Glossary** (~25 terms) | ~25 | 0.65 |
| **Journal** (~13 articles + RSS) | ~14 | 0.70 |
| **Data Endpoints** (facts.json, citations.json, India AI Index, DPDP Tracker, State of ISO 42001) | ~5 | 0.85–0.5 |
| **Auth Pages** (login, signup, forgot-password, reset-password, auth-callback) | ~5 | Protected |
| **Protected App** (dashboard, billing, library, schedules, personas, audit-lab, lab/chat) | ~7+ | Protected |

**Total: ~245+ public URLs + 12+ protected routes**

---

## Phase 1: Smoke Testing (Day 1)

> **Goal:** Verify all pages load without errors. This is the fastest, highest-impact test.

### 1.1 HTTP Status Code Sweep

Crawl every URL in the sitemap and verify:

| Check | Expected | Severity |
|---|---|---|
| All 245+ sitemap URLs return **200 OK** | ✅ | 🔴 Critical |
| No **404** on any internal link | ✅ | 🔴 Critical |
| No **500/502/503** on any page | ✅ | 🔴 Critical |
| All redirects resolve within **2 hops** | ✅ | 🟡 Medium |
| HTTPS enforced (HTTP → HTTPS redirect) | ✅ | 🔴 Critical |
| `www` → non-www canonical redirect (or vice versa) | ✅ | 🟡 Medium |

**Tool Recommendation:** `curl -sL -o /dev/null -w "%{http_code} %{url_effective}" [URL]` for each URL, or use Screaming Frog / `linkchecker`.

### 1.2 Console Error Sweep

For each core page category (pick 1 representative URL per group), open in browser dev tools:

| Check | Expected | Severity |
|---|---|---|
| No uncaught JS errors in console | ✅ | 🔴 Critical |
| No failed network requests (404 assets, CORS errors) | ✅ | 🔴 Critical |
| No mixed-content warnings (HTTP resource on HTTPS page) | ✅ | 🔴 Critical |
| No deprecation warnings | ✅ | 🟢 Low |

---

## Phase 2: Functional Testing (Day 1–3)

### 2.1 Navigation & Routing

| Test Case | Steps | Expected | Severity |
|---|---|---|---|
| **Header nav links** | Click every link in the header/nav on desktop & mobile | Navigates to correct page, active state shown | 🔴 Critical |
| **Footer nav links** | Click every link in the footer | Navigates correctly | 🔴 Critical |
| **Mobile hamburger menu** | Open, navigate, close menu | Menu opens/closes smoothly, links work | 🔴 Critical |
| **Skip to content** link | Tab into the page | Skip link focuses `#main` | 🟡 Medium |
| **Client-side routing** (SPA) | Navigate between pages | URL updates, content loads, no full-page refresh | 🔴 Critical |
| **Browser back/forward** | Navigate 3 pages deep, then back | History works correctly | 🔴 Critical |
| **Deep-link direct access** | Open `/compliance/iso-42001` directly | Page renders correctly (SSR/hydration) | 🔴 Critical |
| **404 page** | Visit `/nonexistent-page` | Custom 404 page shown | 🟡 Medium |

### 2.2 Core Feature: Chat Lab (`/lab`)

| Test Case | Steps | Expected | Severity |
|---|---|---|---|
| Lab page loads | Visit `/lab` | Chat interface renders | 🔴 Critical |
| Send a text message | Type + submit a message | AI response received, renders correctly | 🔴 Critical |
| Free messages work | As unauthenticated user, send messages | Free messages allowed as advertised | 🔴 Critical |
| Message counter | Send messages | Counter updates, limits enforced | 🟡 Medium |
| Vision/file upload | Upload an image | AI processes the image | 🟡 Medium |
| Chat history persistence | Navigate away and return | History maintained in session | 🟡 Medium |
| Loading states | Submit message | Spinner/skeleton shown during response | 🟡 Medium |
| Error handling | Simulate network failure | User-friendly error message shown | 🔴 Critical |
| Rate limiting | Exceed free tier | Clear message about topping up / pricing | 🔴 Critical |

### 2.3 Core Feature: Wallet / Payments

| Test Case | Steps | Expected | Severity |
|---|---|---|---|
| Wallet button visible | Any page with header | Wallet status shown | 🔴 Critical |
| Signup shagun credit | New user signup | ₹501 credited to wallet | 🔴 Critical |
| Top-up flow | Click wallet → add credits | Razorpay checkout opens, payment processes | 🔴 Critical |
| Razorpay integration | Complete a test payment | Credits reflect in wallet, receipt generated | 🔴 Critical |
| INR billing | View pricing/wallet | All amounts in ₹ INR | 🔴 Critical |
| ₹0.50/msg deduction | Send paid message | Wallet deducted by ₹0.50 | 🔴 Critical |

### 2.4 Core Feature: Authentication

| Test Case | Steps | Expected | Severity |
|---|---|---|---|
| Signup flow | Visit `/signup`, complete form | Account created, redirected to lab/dashboard | 🔴 Critical |
| Login flow | Visit `/login`, enter credentials | Logged in, session persists | 🔴 Critical |
| Forgot password | Visit `/forgot-password`, enter email | Reset email sent | 🔴 Critical |
| Reset password | Click reset link in email | Password updated | 🔴 Critical |
| Auth callback (OAuth) | Login via OAuth provider | Redirected correctly, session created | 🔴 Critical |
| Protected route guard | Visit `/dashboard` when logged out | Redirected to `/login` | 🔴 Critical |
| Session persistence | Close browser, reopen | Session maintained (or re-auth required) | 🟡 Medium |
| Logout | Click logout | Session cleared, redirected to home | 🔴 Critical |

### 2.5 Core Feature: Consultation Booking (`/consult`)

| Test Case | Steps | Expected | Severity |
|---|---|---|---|
| Booking form renders | Visit `/consult` | Form/CTA visible with ₹2,500 pricing | 🔴 Critical |
| Submit booking request | Fill form, submit | Confirmation shown, email sent | 🔴 Critical |
| City-specific pages | Visit `/consult/mumbai`, `/consult/delhi`, etc. | Correct city name rendered, unique content | 🟡 Medium |
| Form validation | Submit with empty required fields | Validation errors shown | 🔴 Critical |

### 2.6 Core Feature: AI Audit (`/ai-audit`)

| Test Case | Steps | Expected | Severity |
|---|---|---|---|
| Audit page renders | Visit `/ai-audit` | Page loads with ₹1,799 pricing | 🔴 Critical |
| Start audit flow | Click CTA to begin | Audit flow starts (payment or form) | 🔴 Critical |
| City-specific pages | Visit `/ai-audit/mumbai`, etc. | Correct city, consistent pricing | 🟡 Medium |
| Audit report delivery | Complete audit flow | Report generated/delivered | 🔴 Critical |

### 2.7 Custom Deployments (`/custom-deployments`)

| Test Case | Steps | Expected | Severity |
|---|---|---|---|
| Page renders | Visit `/custom-deployments` | Content loads, CTA visible | 🔴 Critical |
| Inquiry form | Fill and submit | Confirmation shown | 🔴 Critical |

### 2.8 PWA / Install Prompt

| Test Case | Steps | Expected | Severity |
|---|---|---|---|
| Manifest loads | Check `/manifest.webmanifest` | Valid manifest JSON returned | 🟡 Medium |
| Install prompt works | Click "Install on this device" | PWA install prompt triggers | 🟡 Medium |
| PWA offline behavior | Install, go offline | Graceful offline message (not browser error) | 🟡 Medium |

---

## Phase 3: Content & Copy QA (Day 2–3)

### 3.1 Spelling, Grammar & Consistency

| Check | Scope | Severity |
|---|---|---|
| No typos or grammatical errors | All 245+ pages | 🟡 Medium |
| Consistent pricing (₹0.50/msg, ₹501 shagun, ₹1,799 audit, ₹2,500 consult, ₹24,499 engagement) | All pages where pricing is mentioned | 🔴 Critical |
| Consistent brand name: "Bharat NeuroTech" (not "Bharat Neurotech" or "BharatNeurotech") | All pages | 🟡 Medium |
| "NeuroCortex v3" (not "Neurocortex" or "NeuroCortex V3") | All pages | 🟡 Medium |
| Dr. Sodhi's title consistent | All pages mentioning him | 🟡 Medium |
| ISO standard numbers correct (42001, 27001, 27701) | All compliance pages | 🔴 Critical |

### 3.2 Hindi Localization (`/hi/`)

| Check | Expected | Severity |
|---|---|---|
| All `/hi/` pages render in Hindi | ✅ Devanagari script visible | 🔴 Critical |
| No English text leaking into Hindi pages (except brand names) | ✅ | 🟡 Medium |
| Hindi typography renders correctly (font loaded) | ✅ | 🔴 Critical |
| `lang="hi"` attribute set on HTML element | ✅ | 🟡 Medium |
| Pricing still in INR ₹ | ✅ | 🔴 Critical |

### 3.3 Legal Pages

| Check | Expected | Severity |
|---|---|---|
| Privacy Policy accessible | ✅ (required for DPDP compliance) | 🔴 Critical |
| Terms of Service accessible | ✅ | 🔴 Critical |
| Refund Policy accessible (especially for Razorpay) | ✅ | 🔴 Critical |
| Cookie consent / notice | ✅ (if applicable under DPDP/GDPR) | 🟡 Medium |

---

## Phase 4: SEO & Structured Data Testing (Day 3–4)

### 4.1 On-Page SEO

| Check | Scope | Expected | Severity |
|---|---|---|---|
| Unique `<title>` per page | All 245+ pages | ✅ No duplicates | 🔴 Critical |
| `<meta name="description">` present and unique | All pages | ✅ | 🔴 Critical |
| Single `<h1>` per page | All pages | ✅ | 🟡 Medium |
| Canonical URL (`<link rel="canonical">`) | All pages | ✅ Self-referencing or correct | 🔴 Critical |
| Open Graph tags (og:title, og:description, og:image) | All pages | ✅ | 🟡 Medium |
| Twitter card tags | All pages | ✅ | 🟢 Low |
| OG image resolves (200 OK, correct dimensions) | All pages with og:image | ✅ 1200×630 recommended | 🟡 Medium |

### 4.2 Sitemap QA

| Check | Expected | Severity |
|---|---|---|
| `sitemap.xml` accessible at root | ✅ | 🔴 Critical |
| All URLs in sitemap return 200 | ✅ | 🔴 Critical |

> [!WARNING]
> **Issue Found:** All `<lastmod>` dates in the sitemap are `1970-01-01` (Unix epoch). This should be fixed to actual last-modified dates for proper crawl prioritization.

| `<lastmod>` dates are realistic (not `1970-01-01`) | ❌ Needs fix | 🟡 Medium |
| No duplicate URLs | ✅ | 🟡 Medium |
| Sitemap registered in Google Search Console | ✅ | 🔴 Critical |

### 4.3 Structured Data (JSON-LD)

| Check | Expected | Severity |
|---|---|---|
| `Organization` schema on homepage | ✅ (present) | 🔴 Critical |
| `WebSite` schema with SearchAction | ✅ (present) | 🟡 Medium |
| `Service` schema with pricing | ✅ (present) | 🟡 Medium |
| All JSON-LD validates (no errors in Google Rich Results Test) | ✅ | 🔴 Critical |
| `FAQ` schema on `/faq` page | ✅ | 🟡 Medium |
| `Article` schema on `/journal/*` posts | ✅ | 🟡 Medium |
| `BreadcrumbList` on sub-pages | ✅ (nice to have) | 🟢 Low |

### 4.4 robots.txt QA

| Check | Expected | Severity |
|---|---|---|
| robots.txt accessible | ✅ (verified) | 🔴 Critical |
| Protected routes disallowed (/admin, /dashboard, /billing, etc.) | ✅ (verified) | 🔴 Critical |
| AI crawlers explicitly allowed | ✅ (verified — GPTBot, ClaudeBot, etc.) | 🟡 Medium |
| Sitemap URL referenced | ✅ (verified) | 🟡 Medium |

---

## Phase 5: Performance Testing (Day 4–5)

### 5.1 Core Web Vitals (per page category)

Run Google Lighthouse or PageSpeed Insights on **1 representative URL per category**:

| Metric | Target | Severity |
|---|---|---|
| **LCP** (Largest Contentful Paint) | ≤ 2.5s | 🔴 Critical |
| **INP** (Interaction to Next Paint) | ≤ 200ms | 🔴 Critical |
| **CLS** (Cumulative Layout Shift) | ≤ 0.1 | 🔴 Critical |
| **FCP** (First Contentful Paint) | ≤ 1.8s | 🟡 Medium |
| **TTFB** (Time to First Byte) | ≤ 800ms | 🟡 Medium |
| **Lighthouse Performance score** | ≥ 90 | 🟡 Medium |

**Pages to test:**
1. `/` (Homepage)
2. `/neurocortex-v3` (Product)
3. `/pricing` (Pricing)
4. `/lab` (Chat app — interactive)
5. `/ai-audit` (Service)
6. `/compliance/iso-42001` (Content)
7. `/journal/iso-42001-roadmap` (Article)
8. `/answers/best-indian-ai-model-2026` (SEO landing)
9. `/hi/neurocortex-v3` (Hindi localization)
10. `/glossary` (Index page)

### 5.2 Asset Optimization

| Check | Expected | Severity |
|---|---|---|
| Images served in AVIF/WebP with fallback | ✅ (verified — `<picture>` tags present) | 🟡 Medium |
| Fonts preconnected (`fonts.googleapis.com`, `fonts.gstatic.com`) | ✅ (verified) | 🟡 Medium |
| JS bundles code-split | ✅ (modulepreload hints visible) | 🟡 Medium |
| CSS minified | ✅ | 🟢 Low |
| Gzip/Brotli compression enabled | ✅ | 🟡 Medium |
| No unused CSS/JS > 50KB | ✅ | 🟢 Low |

### 5.3 Load Testing

| Test | Target | Severity |
|---|---|---|
| Homepage under 100 concurrent users | < 3s response time | 🟡 Medium |
| Chat lab under 50 concurrent active sessions | Messages delivered < 5s | 🔴 Critical |
| Razorpay checkout under 20 concurrent users | No timeouts | 🔴 Critical |

**Tool:** k6, Artillery, or Apache JMeter

---

## Phase 6: Responsive Design & Cross-Browser Testing (Day 3–5)

### 6.1 Breakpoint Testing

Test on the following viewports:

| Viewport | Device | Resolution |
|---|---|---|
| Mobile Small | iPhone SE | 375×667 |
| Mobile Large | iPhone 14 Pro Max | 430×932 |
| Tablet Portrait | iPad | 768×1024 |
| Tablet Landscape | iPad | 1024×768 |
| Desktop | Laptop | 1366×768 |
| Desktop Large | Monitor | 1920×1080 |
| Ultra-wide | 4K Monitor | 2560×1440 |

**For each breakpoint, verify:**
- [ ] No horizontal scrollbar appears
- [ ] Text is readable without zooming
- [ ] Touch targets are ≥ 44×44px on mobile
- [ ] Images don't overflow containers
- [ ] Navigation is accessible (hamburger menu on mobile)
- [ ] CTA buttons are visible above the fold
- [ ] Tables are scrollable or stack on mobile
- [ ] Hero section looks proportional

### 6.2 Browser Matrix

| Browser | Versions | Priority |
|---|---|---|
| Chrome | Latest + 1 previous | 🔴 Must |
| Safari | Latest (macOS + iOS) | 🔴 Must |
| Firefox | Latest | 🟡 Should |
| Edge | Latest | 🟡 Should |
| Samsung Internet | Latest | 🟢 Nice |
| Opera | Latest | 🟢 Nice |

---

## Phase 7: Accessibility Testing (Day 4–5)

### 7.1 Automated Testing

Run **axe-core** or **Lighthouse Accessibility** on every page category:

| Check | Target | Severity |
|---|---|---|
| Lighthouse Accessibility score | ≥ 90 | 🔴 Critical |
| No `axe-core` critical violations | ✅ | 🔴 Critical |
| All images have `alt` text | ✅ (verified — alt tags present) | 🔴 Critical |
| Color contrast ratio ≥ 4.5:1 (text), ≥ 3:1 (large text) | ✅ | 🔴 Critical |
| Form inputs have associated labels | ✅ | 🔴 Critical |
| ARIA attributes used correctly | ✅ | 🟡 Medium |

### 7.2 Manual Accessibility Testing

| Test | Steps | Expected | Severity |
|---|---|---|---|
| **Keyboard navigation** | Tab through entire page | All interactive elements reachable, focus visible | 🔴 Critical |
| **Screen reader** | Navigate with VoiceOver (Mac) / NVDA (Windows) | Content announced correctly, landmarks detected | 🟡 Medium |
| **Skip to content** | Press Tab on page load | Skip link appears, focuses main content | 🟡 Medium |
| **Focus traps** (modals/menus) | Open modal, Tab through | Focus stays within modal, Escape closes | 🟡 Medium |
| **prefers-reduced-motion** | Enable reduced motion in OS | Animations disabled (verified — CSS media query present) | 🟡 Medium |
| **Dark mode / High contrast** | Enable high contrast mode | Content still readable | 🟢 Low |

---

## Phase 8: Security Testing (Day 5–6)

### 8.1 HTTPS & Headers

| Check | Expected | Severity |
|---|---|---|
| HTTPS with valid SSL certificate | ✅ | 🔴 Critical |
| HSTS header present | ✅ `Strict-Transport-Security` | 🔴 Critical |
| Content-Security-Policy header | ✅ | 🟡 Medium |
| X-Content-Type-Options: nosniff | ✅ | 🟡 Medium |
| X-Frame-Options: DENY or SAMEORIGIN | ✅ | 🟡 Medium |
| Referrer-Policy header | ✅ | 🟡 Medium |
| Permissions-Policy header | ✅ | 🟢 Low |

**Tool:** `curl -I https://bharatneurotech.com/` or [securityheaders.com](https://securityheaders.com)

### 8.2 Authentication & Authorization

| Test | Steps | Expected | Severity |
|---|---|---|---|
| SQL injection on login/signup forms | Enter `' OR 1=1 --` | Rejected, no data leak | 🔴 Critical |
| XSS on chat input | Enter `<script>alert('xss')</script>` | Sanitized, no script execution | 🔴 Critical |
| CSRF protection on forms | Inspect form tokens | Anti-CSRF tokens present | 🔴 Critical |
| Session fixation | Log in, check session ID changes | New session ID after login | 🟡 Medium |
| Sensitive data in URL | Check for tokens/passwords in URLs | None | 🔴 Critical |
| API rate limiting | Hammer `/api/` endpoints | 429 Too Many Requests returned | 🟡 Medium |
| Protected routes without auth | Visit `/dashboard`, `/billing`, `/admin` without login | Redirected to login | 🔴 Critical |

### 8.3 Payment Security

| Check | Expected | Severity |
|---|---|---|
| Razorpay checkout over HTTPS | ✅ | 🔴 Critical |
| No PCI data stored server-side | ✅ (Razorpay handles card data) | 🔴 Critical |
| Payment confirmation webhook validated | ✅ | 🔴 Critical |
| Duplicate payment prevention | ✅ | 🔴 Critical |

---

## Phase 9: API & Integration Testing (Day 5–6)

### 9.1 Public API Endpoints

| Endpoint | Check | Severity |
|---|---|---|
| `/facts.json` | Returns valid JSON, 200 OK | 🟡 Medium |
| `/api/public/citations.json` | Returns valid JSON, 200 OK | 🟡 Medium |
| `/journal/rss.xml` | Returns valid RSS XML | 🟡 Medium |
| `/manifest.webmanifest` | Returns valid JSON manifest | 🟡 Medium |
| `/sitemap.xml` | Returns valid XML | 🟡 Medium |

### 9.2 NeuroCortex API (`/api`)

| Check | Expected | Severity |
|---|---|---|
| API docs page renders | ✅ | 🔴 Critical |
| OpenAI-compatible endpoint format | ✅ (as advertised) | 🔴 Critical |
| API key authentication works | ✅ | 🔴 Critical |
| Rate limiting enforced | ✅ | 🟡 Medium |
| Error responses have proper format | ✅ JSON with error codes | 🟡 Medium |

### 9.3 Third-Party Integrations

| Integration | Check | Severity |
|---|---|---|
| **Razorpay** | Test payment completes | 🔴 Critical |
| **Plausible Analytics** | Script loads, events fire | 🟡 Medium |
| **Google Fonts** | Fonts load (Inter Tight, JetBrains Mono) | 🟡 Medium |
| **Google Search Console** | Site verified (verification meta tag present) | 🟡 Medium |

---

## Phase 10: Edge Cases & Error Handling (Day 6)

| Test | Steps | Expected | Severity |
|---|---|---|---|
| Empty chat submission | Press send with no text | Prevented or error shown | 🟡 Medium |
| Very long message (10,000+ chars) | Paste and send | Handled gracefully (truncated or error) | 🟡 Medium |
| Special characters in chat | Send emojis, Unicode, RTL text | Renders correctly | 🟡 Medium |
| Wallet at ₹0 | Use all credits | Clear "out of credits" message with top-up CTA | 🔴 Critical |
| Concurrent tab sessions | Open lab in 2 tabs | No conflicts, wallet synced | 🟡 Medium |
| Network interruption mid-chat | Disconnect Wi-Fi during response | Retry option or error message | 🟡 Medium |
| Rapid page navigation | Click links very fast | No crashes, router handles gracefully | 🟡 Medium |
| URL parameter injection | Add `?foo=<script>` to URLs | No XSS, parameter ignored | 🔴 Critical |

---

## Phase 11: Internationalization & Localization (Day 6)

| Check | Expected | Severity |
|---|---|---|
| Hindi pages (`/hi/*`) render correctly on all browsers | ✅ | 🔴 Critical |
| Hindi pages have correct `hreflang` tags linking to English equivalents | ✅ | 🟡 Medium |
| Currency symbol ₹ renders on all browsers/devices | ✅ | 🔴 Critical |
| Indian phone number format (+919235344444) clickable on mobile | ✅ `tel:` link | 🟡 Medium |
| Date/time formats appropriate for Indian audience | ✅ | 🟢 Low |

---

## Phase 12: Analytics & Tracking Verification (Day 7)

| Check | Expected | Severity |
|---|---|---|
| Plausible script loads on all pages | ✅ | 🟡 Medium |
| Custom events fire (`ConvertBar+Custom`, `ConvertBar+Audit` found in HTML) | ✅ | 🟡 Medium |
| Outbound link tracking works | ✅ (script: `script.outbound-links.tagged-events.js`) | 🟢 Low |
| No analytics on protected/auth pages (privacy) | ✅ | 🟡 Medium |

---

## Phase 13: Pre-Launch Checklist (Day 7)

| # | Item | Status |
|---|---|---|
| 1 | All 245+ sitemap URLs return 200 | ⬜ |
| 2 | Zero JS console errors on core pages | ⬜ |
| 3 | Chat lab works end-to-end (free tier) | ⬜ |
| 4 | Razorpay payment flow works (test mode) | ⬜ |
| 5 | Signup + Login + Logout works | ⬜ |
| 6 | All pricing consistent across pages | ⬜ |
| 7 | Sitemap `lastmod` dates fixed (not 1970-01-01) | ⬜ |
| 8 | Google Search Console verified + sitemap submitted | ⬜ |
| 9 | JSON-LD validates (Google Rich Results Test) | ⬜ |
| 10 | Lighthouse scores ≥ 90 (Performance, Accessibility, SEO) | ⬜ |
| 11 | Core Web Vitals pass (LCP < 2.5s, CLS < 0.1) | ⬜ |
| 12 | Security headers present (HSTS, CSP, X-Frame-Options) | ⬜ |
| 13 | Hindi localization renders correctly | ⬜ |
| 14 | PWA manifest valid + install works | ⬜ |
| 15 | RSS feed valid | ⬜ |
| 16 | robots.txt correct (verified ✅) | ⬜ |
| 17 | Legal pages accessible (Privacy, Terms, Refund) | ⬜ |
| 18 | Mobile responsiveness on iPhone SE → 4K | ⬜ |
| 19 | Cross-browser tested (Chrome, Safari, Firefox, Edge) | ⬜ |
| 20 | Error pages (404, 500) are branded | ⬜ |

---

## Phase 14: Regression & Monitoring (Post-Launch)

| Activity | Frequency | Tool |
|---|---|---|
| Uptime monitoring | Continuous | UptimeRobot / BetterStack |
| Core Web Vitals tracking | Weekly | Google Search Console |
| Broken link detection | Weekly | Screaming Frog / linkchecker |
| Security header scan | Monthly | securityheaders.com |
| SSL certificate expiry check | Monthly | Automated alert |
| Sitemap re-crawl | After each deploy | Automated CI/CD |
| Lighthouse CI | Every PR/deploy | Lighthouse CI |

---

## Open Questions

> [!IMPORTANT]
> These questions will affect the scope and depth of testing. Please clarify:

1. **Do you have access to the source code / repo?** If yes, I can write automated test scripts (Playwright/Cypress) that you can run in CI/CD. If not, testing will be manual + CLI-based.

2. **Is there a staging/testing environment?** Payment testing (Razorpay) should ideally be done on a staging environment with test keys. Do you have one?

3. **Scope of "protected app" testing:** Do you want me to include testing of the authenticated features (dashboard, billing, library, personas, schedules, audit-lab)? This requires test credentials.

4. **Who will execute the tests?** Should I:
   - (a) Create executable test scripts (Playwright/Cypress) that automate most of this?
   - (b) Provide this as a manual test plan your team executes?
   - (c) I execute the tests myself using browser tools and report findings?

5. **Performance baseline targets:** The plan targets Lighthouse ≥ 90. Do you have different targets or SLAs?

6. **Priority of Hindi testing:** Should Hindi pages be tested as thoroughly as English pages, or is it a secondary priority?

---

## Recommended Execution Timeline

| Day | Phase | Effort |
|---|---|---|
| **Day 1** | Phase 1 (Smoke) + Phase 2.1 (Navigation) | 4–6 hrs |
| **Day 2** | Phase 2.2–2.8 (All Functional) | 6–8 hrs |
| **Day 3** | Phase 3 (Content QA) + Phase 6 (Responsive) | 6–8 hrs |
| **Day 4** | Phase 4 (SEO) + Phase 7 (Accessibility) | 6–8 hrs |
| **Day 5** | Phase 5 (Performance) + Phase 8 (Security) | 6–8 hrs |
| **Day 6** | Phase 9 (API) + Phase 10 (Edge Cases) + Phase 11 (i18n) | 6–8 hrs |
| **Day 7** | Phase 12 (Analytics) + Phase 13 (Pre-launch checklist) | 4–6 hrs |
| **Total** | | **~40–52 hours** |

> [!TIP]
> If you approve this plan, I can immediately start executing Phase 1 (Smoke Testing) by crawling all 245+ URLs and reporting the results. I can also begin writing Playwright automation scripts for the repeatable test cases.
