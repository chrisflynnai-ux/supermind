**App Name:** Pitch

**Purpose:** A SaaS tool for web designers and agencies to create stunning website redesign proposals. Users can scan any prospect's website, have AI extract and reorganize content with their branding, choose from premium templates, and share a shareable preview link to close deals faster.

**Tagline:** "Turn any website into a winning proposal"

---

## CORE FEATURES

### 1. Landing Page (/)
- Hero section with animated gradient background image
- Premium glassmorphic fixed navbar
- "How it Works" 3-step explanation (Scan ? AI Rebuilds ? Share & Close)
- Feature grid with 8 key capabilities
- Full-width testimonial section with purple gradient
- Final CTA section
- Footer with logo and links

### 2. Authentication (/auth)
- Split-screen layout (branding left, form right)
- Toggle between Sign In and Sign Up modes
- Email/password authentication
- User profiles created on signup with `full_name`
- Animated transitions between modes
- Mobile responsive (branding hidden on mobile)

### 3. Dashboard (/dashboard)
- Sidebar navigation layout with:
  - Overview (default)
  - Find Leads
  - My Pitches
  - Analytics
  - Settings
- Stats cards showing: Total Pitches, Total Views, Feedback Received, Avg Session Duration
- Recent pitches grid with thumbnail previews
- Quick actions: Open, Copy Link, Delete

### 4. Find Leads (/dashboard/leads)
- Two-tab interface: "Search" and "My Leads"
- **Search Tab:**
  - Search input for queries like "barbers in amsterdam"
  - Calls Apify Google Maps scraper API
  - Displays business cards with: name, website, phone, address, rating, category
  - Save individual leads or "Save All"
  - Create Pitch button that navigates to pitch creation with prefilled data
  - Staggered framer-motion animations on results
- **My Leads Tab:**
  - List of saved leads with filters (status, city, category)
  - Status tracking: new ? pitched ? converted
  - Bulk selection and actions
  - Send Email action (opens compose dialog)

### 5. Create New Pitch (/dashboard/new)
- 3-step wizard with progress indicator:
  - **Step 1 (Input):** Company name + Website URL form
  - **Step 2 (Scanning):** Animated loading with 3 phases (Connecting ? Extracting ? Processing)
  - **Step 3 (Template):** Choose from 5 templates with AI recommendation highlighted
- Auto-starts if coming from leads page with prefilled data
- Saves to database and navigates to previews list

### 6. My Pitches (/dashboard/previews)
- Searchable list of all created pitches
- Row-based layout with: thumbnail, company name, URL, service count, date, status
- Status indicators: draft, sent, feedback_received
- Actions: View, Copy Link, Manage, Delete

### 7. Manage Pitch (/manage/:id)
- Full-page editor with sidebar
- Sidebar contains:
  - Preview info card (thumbnail, name, status)
  - Viewport switcher (Desktop/Tablet/Mobile)
  - Template selector
  - Status dropdown
  - Actions: View Feedback, Edit Content, Send Email, Delete
- Main area: Live preview iframe with responsive frame
- Feedback panel (slide-in sheet) showing client feedback
- Quick Edit panel for modifying content JSON

### 8. Public Preview (/:userPrefix/:clientSlug)
- Shareable URL structure: `{domain}/{userPrefix}/{clientSlug}`
- Tracks visits (device, country, city, referrer)
- Renders full website with sections:
  - Hero (with pattern fallback if no suitable image)
  - About
  - Services
  - Gallery
  - Testimonials
  - Contact
  - Instagram Feed (if available)
  - Creator Footer (shows designer's profile)
- Feedback button (floating) for clients to submit feedback

### 9. Analytics (/dashboard/analytics)
- Charts showing views over time
- Device breakdown (desktop/tablet/mobile)
- Top performing previews
- Recent visitors list with location/device info

### 10. Settings (/dashboard/settings)
- **Creator Profile Section:**
  - Avatar upload (to Supabase storage)
  - Full name, business name, tagline
  - Contact & social links (email, website, LinkedIn, Twitter, Instagram)
  - Toggle: Show Creator Section on pitch pages
- **Email Integrations Section:**
  - Connect Gmail via OAuth 2.0
  - Outlook marked as "Coming Soon"
  - Shows connected email with disconnect option

---

## DATABASE SCHEMA

### Tables

**profiles**
- id: uuid (primary key)
- user_id: uuid (references auth.users)
- full_name: text
- avatar_url: text
- business_name: text
- tagline: text
- website_url: text
- linkedin_url: text
- twitter_url: text
- instagram_url: text
- public_email: text
- show_branding: boolean (default true)
- created_at: timestamptz
- updated_at: timestamptz

**client_previews**
- id: uuid (primary key)
- user_id: uuid (references auth.users)
- slug: text (unique, format: userprefix/client-slug)
- client_name: text
- original_url: text
- template_id: text (default 'corporate-classic')
- scraped_content: jsonb
- processed_schema: jsonb
- brand_colors: jsonb
- status: enum (draft, sent, feedback_received)
- created_at: timestamptz
- updated_at: timestamptz

**preview_visits**
- id: uuid (primary key)
- preview_id: uuid (references client_previews)
- device_type: text (desktop, tablet, mobile)
- country: text
- city: text
- referrer: text
- user_agent: text
- ip_hash: text
- session_duration: integer
- visited_at: timestamptz

**client_feedback**
- id: uuid (primary key)
- preview_id: uuid (references client_previews)
- feedback_text: text
- client_name: text
- client_email: text
- is_read: boolean (default false)
- created_at: timestamptz

**leads**
- id: uuid (primary key)
- user_id: uuid
- business_name: text
- website_url: text
- email: text
- phone: text
- address: text
- city: text
- category: text
- rating: numeric
- source_query: text
- status: enum (new, pitched, converted)
- preview_id: uuid (nullable, references client_previews)
- created_at: timestamptz

**email_connections**
- id: uuid (primary key)
- user_id: uuid
- provider: text (gmail, outlook)
- email_address: text
- access_token: text
- refresh_token: text
- token_expires_at: timestamptz
- is_active: boolean (default true)
- created_at: timestamptz
- updated_at: timestamptz

**email_templates**
- id: uuid (primary key)
- user_id: uuid
- name: text
- subject: text
- body_html: text
- is_default: boolean (default false)
- created_at: timestamptz
- updated_at: timestamptz

**outreach_emails**
- id: uuid (primary key)
- user_id: uuid
- preview_id: uuid
- lead_id: uuid (nullable)
- recipient_email: text
- recipient_name: text
- subject: text
- status: enum (sent, delivered, opened, clicked, bounced)
- sent_at: timestamptz
- opened_at: timestamptz
- created_at: timestamptz

---

## EDGE FUNCTIONS

### firecrawl-scrape
- **Purpose:** Scrape any website URL
- **Input:** { url, options }
- **Process:** Calls Firecrawl API to extract markdown, HTML, links, branding
- **Secret:** FIRECRAWL_API_KEY

### process-content
- **Purpose:** AI-powered content processing
- **Input:** { scrapedContent, brandColors }
- **Process:** Uses Lovable AI to:
  - Classify business industry (60+ types)
  - Recommend best template
  - Extract and organize content sections
  - Classify images (hero, gallery, portrait, unusable)
  - Generate adaptive section titles
  - Extract/validate brand colors
- **Secret:** LOVABLE_API_KEY

### apify-google-maps
- **Purpose:** Search for local businesses
- **Input:** { query, maxResults }
- **Process:** Calls Apify Google Places scraper
- **Returns:** Array of business leads with name, website, phone, address, rating
- **Secret:** APIFY_API_KEY

### track-visit
- **Purpose:** Track preview page visits
- **Input:** { preview_id, referrer, session_duration }
- **Process:**
  - Hash visitor IP for privacy
  - Detect device type from user-agent
  - Geo-lookup IP for country/city
  - Insert into preview_visits table

### get-oauth-url
- **Purpose:** Generate secure OAuth authorization URLs
- **Input:** { provider, redirect_uri }
- **Returns:** OAuth consent URL for Gmail or Outlook
- **Secrets:** GOOGLE_CLIENT_ID, MICROSOFT_CLIENT_ID

### oauth-callback
- **Purpose:** Exchange OAuth code for tokens
- **Input:** { provider, code, redirect_uri }
- **Process:**
  - Exchange authorization code for access/refresh tokens
  - Fetch user email from provider
  - Store tokens in email_connections table
- **Secrets:** GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET

### send-email
- **Purpose:** Send emails via connected Gmail/Outlook
- **Input:** { to, toName, subject, bodyHtml, previewId, leadId }
- **Process:**
  - Fetch user's OAuth tokens
  - Refresh if expired
  - Call Gmail API or Microsoft Graph API
  - Log to outreach_emails table

---

## 5 TEMPLATE STYLES

| Template ID | Name | Description | Best For |
|-------------|------|-------------|----------|
| corporate-classic | Corporate Classic | Traditional, professional | Law firms, accountants, B2B |
| modern-professional | Modern Professional | Tech-forward with gradients | Tech companies, SaaS, startups |
| bold-starter | Bold Starter | Vibrant, high-impact | Creative agencies, designers |
| elegant-minimal | Elegant Minimal | Luxury with whitespace | Fashion, architecture, fine dining |
| warm-friendly | Warm Friendly | Approachable, cozy | Cafes, salons, local businesses |

Each template has:
- Unique hero section styling
- Different animation intensities
- Industry-appropriate color handling
- Specific border radius and card styles

---

## INDUSTRY DETECTION (60+ business types)

The AI detects business type in multiple languages and maps to color palettes:

- **Barber:** Charcoal (#1F2937) + Gold (#D4AF37)
- **Restaurant:** Red (#DC2626) + Orange (#F97316)
- **Law Firm:** Navy (#1E3A5F) + Slate (#64748B)
- **Dentist:** Teal (#0D9488) + Blue (#3B82F6)
- **Gym/Fitness:** Red (#DC2626) + Orange (#F97316)
- **Salon:** Purple (#7C3AED) + Pink (#EC4899)
- **Tech/SaaS:** Blue (#3B82F6) + Cyan (#06B6D4)
- ...and 50+ more

---

## KEY COMPONENTS

### Preview Sections
- HeroSection (5 variants per template)
- AboutSection (stats, value props)
- ServicesSection (grid of services)
- GallerySection (image grid)
- TestimonialsSection (carousel)
- ContactSection (contact info)
- InstagramFeed (if available)
- CreatorFooter (designer profile)
- FeedbackButton (floating action)

### Pattern Backgrounds
- Fallback patterns when no suitable hero image exists
- Industry-specific patterns (geometric, waves, dots, etc.)

### Smart Logo
- Handles logo loading errors gracefully
- Detects if logo needs background for contrast
- No ugly fallback initials

---

## UI/UX DETAILS

### Animations (Framer Motion)
- Page transitions
- Staggered card reveals on search results
- Parallax scrolling on hero images
- Smooth progress indicators
- Magnetic buttons
- Text reveal animations

### Design System
- Built on shadcn/ui components
- Tailwind CSS with custom theme
- Primary color: Purple (#7C3AED equivalent)
- Glassmorphic elements with backdrop blur
- Consistent border radius (rounded-xl, rounded-2xl)

### Mobile Responsive
- Collapsible sidebar on mobile
- Touch-friendly buttons
- Stacked layouts on small screens

---

## STORAGE BUCKETS

- **avatars**: Public bucket for user profile photos
- **generated-images**: Public bucket for AI-generated images

---

## RLS POLICIES (Security)

All tables have Row Level Security enabled with policies ensuring:
- Users can only CRUD their own data
- Public previews are viewable by anyone (for sharing)
- Feedback can be submitted by anyone (for clients)
- Visit tracking allows anonymous inserts

---

## SECRETS REQUIRED

| Secret Name | Purpose |
|-------------|---------|
| FIRECRAWL_API_KEY | Website scraping API |
| APIFY_API_KEY | Google Maps business search |
| LOVABLE_API_KEY | AI content processing |
| GOOGLE_CLIENT_ID | Gmail OAuth |
| GOOGLE_CLIENT_SECRET | Gmail OAuth |

---

## IMPLEMENTATION ORDER

1. **Setup:** Connect Supabase, create database schema with all tables
2. **Auth:** Implement authentication with email/password, profile creation
3. **Dashboard Layout:** Create sidebar navigation layout
4. **Pitch Creation Flow:** Build 3-step wizard with Firecrawl + AI processing
5. **Preview Rendering:** Implement all 5 template variants with sections
6. **Lead Discovery:** Integrate Apify Google Maps search
7. **Email Integration:** Add Gmail OAuth and email sending
8. **Analytics:** Build visit tracking and charts
9. **Settings:** Creator profile with avatar upload

---

## ADDITIONAL NOTES

- Slug format: `{userprefix}/{client-slug}` where userprefix comes from user's name or email
- Preview URLs support legacy `/preview/:slug` format with redirects
- All edge functions have proper CORS headers including `x-supabase-client-platform`
- OAuth callback handling requires state guard to prevent double-processing
- Toast notifications use sonner for success/error feedback
- All forms have loading states with Loader2 spinner
