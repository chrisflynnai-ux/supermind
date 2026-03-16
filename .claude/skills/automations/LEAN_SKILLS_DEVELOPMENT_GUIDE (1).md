# LEAN SKILLS DEVELOPMENT GUIDE
## Replacing MCPs with Smart Scripts & Direct Package Integration

**Doctrine:** Skills + Scripts > MCPs  
**Principle:** Minimal context at Zero-Point, capability on-demand

---

## THE PROBLEM WITH MCPs

MCPs (Model Context Protocol servers) introduce:
- Always-loaded parameter schemas (token bloat)
- External process dependencies (fragility)
- CLI call overhead (latency)
- Context competition with your SSOT objects

**The Alternative:** Encode tool logic directly into Skills as smart scripts that load on-demand and unload after execution.

---

## SKILL ARCHITECTURE PATTERN

### Zero-Point State (Always Loaded)
```yaml
# Only the capability index lives in default context (~50 tokens)
tool_capabilities:
  - image_processing: "resize, convert, optimize"
  - payment: "charge, refund, subscription"
  - infrastructure: "deploy, scale, monitor"
  - database: "query, insert, migrate"
```

### Activated State (On-Demand)
```
ZERO_POINT → ACTIVATE SKILL → LOAD SCRIPT → EXECUTE → RETURN RESULT → UNLOAD → ZERO_POINT
```

---

## SKILL STRUCTURE TEMPLATE

```xml
<?xml version="1.0" encoding="UTF-8"?>
<skill id="[SKILL_ID]" version="1.0.0">
  <metadata>
    <name>[Human Readable Name]</name>
    <description>[What this skill does - keep under 50 words]</description>
    <category>[image|payment|infra|data|api]</category>
    <load_cost>low|medium|high</load_cost>
  </metadata>
  
  <dependencies>
    <!-- NPM packages this skill requires -->
    <npm>sharp</npm>
    <npm>stripe</npm>
    <!-- PIP packages if Python -->
    <pip>pillow</pip>
  </dependencies>
  
  <capabilities>
    <!-- What the agent can decide to use -->
    <capability id="resize_image">
      <trigger>image needs resizing</trigger>
      <accepts>jpeg, png, webp, gif</accepts>
      <returns>processed image buffer</returns>
    </capability>
  </capabilities>
  
  <scripts>
    <!-- The actual implementation -->
    <script lang="javascript" capability="resize_image">
      <![CDATA[
        // Script body here
      ]]>
    </script>
  </scripts>
  
  <error_handling>
    <on_error action="fallback|retry|escalate"/>
    <fallback_capability>alternative_tool_id</fallback_capability>
  </error_handling>
</skill>
```

---

## EXAMPLE: IMAGE PROCESSING SKILL

### Skill Definition
```xml
<?xml version="1.0" encoding="UTF-8"?>
<skill id="image_processor" version="1.0.0">
  <metadata>
    <name>Image Processor</name>
    <description>Resize, convert, and optimize images using Sharp</description>
    <category>image</category>
    <load_cost>medium</load_cost>
  </metadata>
  
  <dependencies>
    <npm>sharp</npm>
  </dependencies>
  
  <capabilities>
    <capability id="convert_format">
      <trigger>convert image to different format</trigger>
      <accepts>jpeg, png, webp, gif, avif, tiff</accepts>
      <returns>converted image buffer</returns>
    </capability>
    <capability id="resize">
      <trigger>resize image to dimensions</trigger>
      <params>width, height, fit</params>
      <returns>resized image buffer</returns>
    </capability>
    <capability id="optimize">
      <trigger>reduce image file size</trigger>
      <params>quality (1-100)</params>
      <returns>optimized image buffer</returns>
    </capability>
  </capabilities>
  
  <scripts>
    <script lang="javascript" capability="convert_format">
      <![CDATA[
const sharp = require('sharp');

async function convertImage(inputBuffer, targetFormat) {
  const formatMap = {
    'jpeg': 'jpeg',
    'jpg': 'jpeg', 
    'png': 'png',
    'webp': 'webp',
    'gif': 'gif',
    'avif': 'avif'
  };
  
  const format = formatMap[targetFormat.toLowerCase()];
  if (!format) {
    throw new Error(`Unsupported format: ${targetFormat}`);
  }
  
  return await sharp(inputBuffer)
    .toFormat(format)
    .toBuffer();
}

module.exports = { convertImage };
      ]]>
    </script>
    
    <script lang="javascript" capability="resize">
      <![CDATA[
const sharp = require('sharp');

async function resizeImage(inputBuffer, width, height, fit = 'cover') {
  return await sharp(inputBuffer)
    .resize(width, height, { fit })
    .toBuffer();
}

module.exports = { resizeImage };
      ]]>
    </script>
  </scripts>
  
  <error_handling>
    <on_error action="fallback"/>
    <fallback_capability>return_original</fallback_capability>
    <error_map>
      <error code="UNSUPPORTED_FORMAT" action="try_pillow"/>
      <error code="MEMORY_EXCEEDED" action="reduce_quality"/>
    </error_map>
  </error_handling>
</skill>
```

---

## EXAMPLE: PAYMENT SKILL (STRIPE)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<skill id="payment_stripe" version="1.0.0">
  <metadata>
    <name>Stripe Payment Processor</name>
    <description>Handle payments, subscriptions, refunds via Stripe API</description>
    <category>payment</category>
    <load_cost>low</load_cost>
  </metadata>
  
  <dependencies>
    <npm>stripe</npm>
  </dependencies>
  
  <secrets>
    <!-- References to secure storage, never hardcoded -->
    <secret key="STRIPE_SECRET_KEY" source="env"/>
  </secrets>
  
  <capabilities>
    <capability id="create_charge">
      <trigger>process one-time payment</trigger>
      <params>amount, currency, customer_id, description</params>
      <returns>charge object with id and status</returns>
    </capability>
    <capability id="create_subscription">
      <trigger>set up recurring billing</trigger>
      <params>customer_id, price_id</params>
      <returns>subscription object</returns>
    </capability>
    <capability id="refund">
      <trigger>refund a payment</trigger>
      <params>charge_id, amount (optional)</params>
      <returns>refund object</returns>
    </capability>
  </capabilities>
  
  <scripts>
    <script lang="javascript" capability="create_charge">
      <![CDATA[
const Stripe = require('stripe');
const stripe = Stripe(process.env.STRIPE_SECRET_KEY);

async function createCharge({ amount, currency, customerId, description }) {
  try {
    const paymentIntent = await stripe.paymentIntents.create({
      amount: Math.round(amount * 100), // Convert to cents
      currency: currency || 'usd',
      customer: customerId,
      description,
      confirm: true,
      automatic_payment_methods: {
        enabled: true,
        allow_redirects: 'never'
      }
    });
    
    return {
      success: true,
      id: paymentIntent.id,
      status: paymentIntent.status,
      amount: paymentIntent.amount / 100
    };
  } catch (error) {
    return {
      success: false,
      error: error.message,
      code: error.code
    };
  }
}

module.exports = { createCharge };
      ]]>
    </script>
  </scripts>
  
  <error_handling>
    <on_error action="return_error"/>
    <error_map>
      <error code="card_declined" action="notify_user"/>
      <error code="insufficient_funds" action="notify_user"/>
      <error code="rate_limit" action="retry" delay="1000"/>
    </error_map>
  </error_handling>
</skill>
```

---

## EXAMPLE: INFRASTRUCTURE SKILL (DIGITAL OCEAN)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<skill id="infra_digitalocean" version="1.0.0">
  <metadata>
    <name>Digital Ocean Infrastructure</name>
    <description>Deploy, manage, and scale infrastructure on Digital Ocean</description>
    <category>infrastructure</category>
    <load_cost>medium</load_cost>
  </metadata>
  
  <dependencies>
    <npm>dots-js</npm>
    <!-- Or use their REST API directly -->
    <npm>axios</npm>
  </dependencies>
  
  <secrets>
    <secret key="DO_API_TOKEN" source="env"/>
  </secrets>
  
  <capabilities>
    <capability id="create_droplet">
      <trigger>launch new server</trigger>
      <params>name, region, size, image</params>
      <returns>droplet object with IP</returns>
    </capability>
    <capability id="deploy_app">
      <trigger>deploy application from repo</trigger>
      <params>repo_url, branch, env_vars</params>
      <returns>app URL and status</returns>
    </capability>
    <capability id="scale">
      <trigger>scale infrastructure up or down</trigger>
      <params>resource_id, new_size</params>
      <returns>updated resource status</returns>
    </capability>
  </capabilities>
  
  <scripts>
    <script lang="javascript" capability="deploy_app">
      <![CDATA[
const axios = require('axios');

const DO_API = 'https://api.digitalocean.com/v2';
const headers = {
  'Authorization': `Bearer ${process.env.DO_API_TOKEN}`,
  'Content-Type': 'application/json'
};

async function deployApp({ repoUrl, branch = 'main', envVars = {} }) {
  try {
    // Create App Platform deployment
    const appSpec = {
      name: `app-${Date.now()}`,
      region: 'nyc',
      services: [{
        name: 'web',
        github: {
          repo: repoUrl,
          branch: branch,
          deploy_on_push: true
        },
        envs: Object.entries(envVars).map(([key, value]) => ({
          key,
          value,
          type: 'SECRET'
        }))
      }]
    };
    
    const response = await axios.post(
      `${DO_API}/apps`,
      { spec: appSpec },
      { headers }
    );
    
    return {
      success: true,
      appId: response.data.app.id,
      url: response.data.app.live_url,
      status: response.data.app.phase
    };
  } catch (error) {
    return {
      success: false,
      error: error.response?.data?.message || error.message
    };
  }
}

module.exports = { deployApp };
      ]]>
    </script>
  </scripts>
  
  <error_handling>
    <on_error action="retry"/>
    <max_retries>3</max_retries>
    <error_map>
      <error code="401" action="refresh_token"/>
      <error code="429" action="backoff" delay="5000"/>
      <error code="404" action="check_resource"/>
    </error_map>
  </error_handling>
</skill>
```

---

## AGENT DECISION PATTERN

Instead of hardcoded workflows, let the agent decide:

```javascript
// Agent receives input and decides which capability to use

async function handleTask(input, availableSkills) {
  // Agent analyzes input
  const analysis = await analyzeInput(input);
  
  // Agent selects appropriate capability
  const selectedCapability = selectBestCapability(analysis, availableSkills);
  
  // Load skill on-demand
  const skill = await loadSkill(selectedCapability.skillId);
  
  try {
    // Execute with error handling
    const result = await skill.execute(selectedCapability.id, input);
    return result;
  } catch (error) {
    // Agent decides fallback
    if (skill.errorHandling.fallback) {
      return await executeFallback(skill.errorHandling.fallback, input);
    }
    throw error;
  } finally {
    // Unload skill, return to Zero-Point
    await unloadSkill(skill);
  }
}
```

---

## ERROR HANDLING PATTERNS

### 1. Graceful Fallback
```javascript
async function executeWithFallback(primaryCapability, fallbackCapability, input) {
  try {
    return await primaryCapability.execute(input);
  } catch (error) {
    if (error.code === 'UNSUPPORTED') {
      console.log(`Primary failed, trying fallback: ${fallbackCapability.id}`);
      return await fallbackCapability.execute(input);
    }
    throw error;
  }
}
```

### 2. Adaptive Format Handling
```javascript
async function processImage(inputBuffer) {
  // Detect format dynamically
  const metadata = await sharp(inputBuffer).metadata();
  
  // Agent decides based on detected format
  const formatHandlers = {
    'jpeg': () => sharp(inputBuffer).jpeg({ quality: 85 }),
    'png': () => sharp(inputBuffer).png({ compressionLevel: 9 }),
    'webp': () => sharp(inputBuffer).webp({ quality: 85 }),
    'gif': () => sharp(inputBuffer).gif(),
  };
  
  const handler = formatHandlers[metadata.format];
  if (!handler) {
    // Fallback: convert to safe format
    return await sharp(inputBuffer).png().toBuffer();
  }
  
  return await handler().toBuffer();
}
```

### 3. 404 / Resource Not Found Handling
```javascript
async function fetchWithFallback(primaryUrl, fallbackUrls = []) {
  try {
    const response = await axios.get(primaryUrl);
    return response.data;
  } catch (error) {
    if (error.response?.status === 404 && fallbackUrls.length > 0) {
      // Try next fallback
      return await fetchWithFallback(fallbackUrls[0], fallbackUrls.slice(1));
    }
    throw error;
  }
}
```

---

## SKILL MANIFEST (Zero-Point Index)

Keep this lightweight in always-loaded context:

```yaml
# skills_manifest.yaml (~100 tokens)
skills:
  image_processor:
    capabilities: [convert, resize, optimize]
    load_cost: medium
    
  payment_stripe:
    capabilities: [charge, subscribe, refund]
    load_cost: low
    
  infra_digitalocean:
    capabilities: [deploy, scale, monitor]
    load_cost: medium
    
  database_supabase:
    capabilities: [query, insert, migrate]
    load_cost: low
```

Agent sees capabilities, loads full skill only when needed.

---

## DEVELOPMENT WORKFLOW

### 1. Identify the Package
```bash
npm info sharp
npm info stripe
npm info @supabase/supabase-js
```

### 2. Create Skill Wrapper
- Define capabilities (what it can do)
- Write scripts (how it does it)
- Map errors to fallbacks

### 3. Test in Isolation
```bash
node test_skill.js image_processor convert_format
```

### 4. Add to Manifest
Update the Zero-Point index.

### 5. Deploy
Skill lives as file, loaded on-demand.

---

## BENEFITS OVER MCP

| Aspect | MCP | Lean Skills |
|--------|-----|-------------|
| Context cost | Always loaded | On-demand |
| Dependencies | External process | Embedded script |
| Error handling | Limited | Agent-decided |
| Flexibility | Rigid schema | Adaptive |
| Maintenance | Server + client | Single file |
| Token overhead | High | Minimal |

---

## NEXT STEPS

1. **Audit current MCPs** — List what each one does
2. **Map to packages** — Find NPM/PIP equivalents
3. **Create skill wrappers** — Use templates above
4. **Build manifest** — Lightweight Zero-Point index
5. **Test autonomous decisions** — Let agent choose tools

---

*Lean Skills Development Guide — Skills + Scripts > MCPs*
*Zero-Point Context Strategy*
