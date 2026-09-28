# DOM-to-UI Synthesizer

A LangGraph-powered agent that clones any public website into a fully editable Next.js codebase — then lets you modify it with plain-English instructions.

---

## Setup Instructions

### Prerequisites

- Python 3.12+
- [Conda](https://docs.conda.io/) (for environment management)
- [uv](https://github.com/astral-sh/uv) 0.9.11 (Python package manager)
- Node.js LTS (`winget install OpenJS.NodeJS.LTS`)
- A [Groq API key](https://console.groq.com/)

### 1. Clone the repo

```bash
git clone https://github.com/HarshitChaudhary108/dom-to-ui-synthesizer.git
cd dom-to-ui-synthesizer
```

### 2. Create and activate the Python environment

```bash
conda create -n website_clone_agent python=3.12
conda activate website_clone_agent
```

### 3. Install Python dependencies

```bash
pip install uv==0.9.11
uv sync
```

### 4. Install Playwright browser

```bash
uv run playwright install chromium
```

### 5. Set up environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 6. Scaffold the Next.js site
```bash
 - Remove the existing site/ folder
Remove-Item -Recurse -Force site
```

```bash
npx create-next-app@latest site --ts --tailwind --app --eslint --use-npm --no-src-dir --import-alias "@/*" --yes
```

### 7. Run the agent

```bash
uv run main.py
```

Enter a website URL when prompted. Once the preview starts at `http://localhost:3000`, use the `modify>` REPL to iteratively change the UI with natural language:

```
modify> make the navbar sticky
modify> change the hero background to dark blue
modify> add a dark mode toggle
```

Type `exit` or `quit` to stop.

---

## Architecture

The agent is built as a **LangGraph state graph** with two modes — `clone` and `modify` — that share the same validate/fix loop.

```
        ┌─────────┐
        │  START  │
        └────┬────┘
             │ route_start()
    ┌────────┴─────────┐
    ▼                  ▼
[scrape]           [modify]
    │                  │
[spec]                 │
    │                  │
[codegen]              │
    └────────┬─────────┘
             ▼
         [validate]  ◄──┐
             │          │
      build_ok? ──No──[fix] (up to 3 retries)
             │
            Yes
             ▼
           END
```

### Node responsibilities

| Node | Responsibility |
|------|----------------|
| **scrape** | Launches Playwright (Chromium), navigates to the URL, injects a custom JS extractor to produce a compact DOM/CSS tree, takes a full-page screenshot |
| **spec** | Converts the raw DOM capture into a structured `DesignSpec` (colors, fonts, sections) using the fast LLM |
| **codegen** | Translates the `DesignSpec` into Next.js App Router components (one `.tsx` per section + `app/page.tsx`) using the code LLM |
| **validate** | Runs `npm run build` in a separate `.next-build` dist dir; passes the build log forward on failure |
| **fix** | Re-invokes the code LLM with the failing build log and current files to produce corrected code |
| **modify** | Sends the user's natural-language instruction + all current files to the code LLM; returns only changed/new files |

---

## Technologies & Models

### Backend

| Package | Version | Purpose |
|---------|---------|---------|
| `langgraph` | ≥1.2.12 | Agent orchestration (state graph) |
| `langchain-groq` | ≥1.1.3 | Groq API integration via LangChain |
| `playwright` | ≥1.63.0 | Headless browser DOM scraping |
| `pydantic` | ≥2.13.5 | Structured output schemas |
| `python-dotenv` | ≥1.2.3 | `.env` config loading |

### Frontend (generated site)

| Technology | Purpose |
|------------|---------|
| Next.js (App Router) | Site framework |
| TypeScript | Type-safe components |
| Tailwind CSS | Utility-first styling |

### Models (via Groq API)

| Model | Used for |
|-------|----------|
| `openai/gpt-oss-20b` | Spec generation (fast, lower cost) |
| `openai/gpt-oss-120b` | Code generation, fix, and modify (higher capability) |

---

## Key Implementation Decisions

### 1. Compact DOM extraction over raw HTML
Rather than sending raw HTML to the LLM (which is large and noisy), a custom JavaScript extractor runs inside Playwright and produces a compact JSON tree — capturing only visible elements, computed styles (bg, color, font, layout), text content, and image URLs. The output is capped at **12,000 characters** to stay within context limits.

### 2. Two-model strategy
A smaller, faster model (`gpt-oss-20b`) handles the spec step (structured classification), while a larger model (`gpt-oss-120b`) handles the heavier codegen, fix, and modify tasks. This balances speed and quality.

### 3. Strict JSON schema compliance for Groq
Groq's strict mode requires all properties to be declared as required and no additional properties. A `_strictify()` helper recursively patches Pydantic-generated schemas to meet these constraints, enabling reliable structured output without manual schema maintenance.

### 4. Auto-fix loop
If `npm run build` fails after code generation or modification, the agent automatically re-invokes the code LLM with the build error log and current files — up to **3 times** — before giving up. This makes the pipeline resilient to common TypeScript/JSX errors.

### 5. Isolated build vs. dev server
Build validation uses a separate `DIST_DIR=.next-build` to avoid conflicting with the Next.js dev server's `.next` directory, allowing both to run simultaneously for a seamless hot-reload experience.

### 6. Path sandboxing
The `safe_path()` function enforces that the LLM can only write to `components/*.tsx` and `app/page.tsx` — blocking path traversal and preventing accidental modification of config or framework files.

---

## Limitations

- **Windows-centric browser channel**: The scraper uses `channel="msedge"`. On macOS/Linux, change this to `"chromium"` in `agent/nodes/scrape.py`.
- **DOM truncation**: Complex pages are truncated at 12,000 characters. Sections near the bottom of large pages may be missing or incomplete in the output.
- **External image URLs**: Images are referenced directly from their original source URLs and are not copied locally. They may fail to load due to CORS policies, hotlink protection, or if the original URL changes.
- **No animations or complex interactivity**: The generated site reproduces layout and content. CSS animations, scroll effects, carousels, and other interactive elements are not replicated.
- **Single-page only**: Only the landing page (root `/`) of the target URL is cloned. Multi-page sites are not supported.
- **Onlg Groq / Groq API dependency**: Requires a valid `GROQ_API_KEY`. Model availability depends on Groq's offerings and may change.
