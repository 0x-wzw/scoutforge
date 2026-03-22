# ScoutForge 🔭

> **AI Model Discovery & Intelligence Platform**
> 
> *"Scout the frontier. Forge the future."*

## What is ScoutForge?

Autonomous crawler that discovers, evaluates, and catalogs the latest open-source AI models from across the internet.

**Targets:**
- 🤗 **HuggingFace** — New model releases, trending, downloads
- 🐙 **GitHub** — Model repos, inference code, implementations  
- 🧪 **Ollama Library** — New GGUF models, community uploads
- 🏛️ **PapersWithCode** — SOTA models with implementations
- 📰 **ArXiv** — Latest research with open weights

---

## Architecture

```
ScoutForge Core
    │
    ├── 🔍 Discovery Agents (Parallel)
    │   ├── HuggingFace Scout
    │   ├── GitHub Crawler
    │   ├── Ollama Watcher
    │   └── Research Monitor
    │
    ├── 🧠 Evaluation Engine
    │   ├── Model Card Parser
    │   ├── Benchmark Extractor
    │   └── License Validator
    │
    ├── 📊 Intelligence Layer
    │   ├── Trend Analysis
    │   ├── Performance Ranking
    │   └── Use-Case Matcher
    │
    └── 🔔 Alert System
        ├── New Model Notifications
        ├── Weekly Digests
        └── Telegram/Discord Feeds
```

---

## Quick Start

```bash
# Clone
git clone https://github.com/0x-wzw/scoutforge.git
cd scoutforge

# Install
pip install -r requirements.txt

# Configure
cp config.example.yaml config.yaml
# Edit: Add your HF token, TG bot token

# Run once
python scout.py --mode single

# Or start continuous monitoring
python scout.py --mode daemon
```

---

## Discovery Targets

### HuggingFace

| Source | Endpoint | Data |
|--------|----------|------|
| Trending | `/api/trending` | Weekly trending models |
| New Releases | `/api/models?sort=created` | Latest uploads |
| Top Downloads | `/api/models?sort=downloads` | Most popular |
| Organization | `/api/models/{org}` | Specific org models |

### GitHub

| Source | Search Query |
|--------|--------------|
| New Repos | `GGUF OR safetensors created:>2026-03-01` |
| Inference Code | `llama.cpp OR llamafile stars:>100` |
| Training Frameworks | `axolotl OR unsloth stars:>500` |

### Ollama

| Source | URL |
|--------|-----|
| Library | `https://ollama.com/library` |
| Community | `https://ollama.com/search` |

---

## Output Format

### Model Card (JSON)

```json
{
  "id": "org/model-name",
  "source": "huggingface",
  "discovered_at": "2026-03-22T10:30:00Z",
  "metadata": {
    "architecture": "transformer",
    "parameters": "7B",
    "context_length": 32768,
    "license": "apache-2.0",
    "languages": ["en", "zh"]
  },
  "benchmarks": {
    "mmlu": 0.72,
    "hellaswag": 0.68
  },
  "tags": ["chat", "code", "reasoning"],
  "downloads": 15000,
  "trend_score": 8.5,
  "use_cases": ["agent-orchestration", "coding-assistant"],
  "ollama_ready": true,
  "gguf_available": true
}
```

---

## Automation

### Cron Schedule

```bash
# Every 6 hours: Full sweep
0 */6 * * * cd scoutforge && python scout.py --mode sweep

# Daily: Trend analysis
0 9 * * * cd scoutforge && python analyze.py --report daily

# Weekly: Comprehensive report
0 10 * * 0 cd scoutforge && python analyze.py --report weekly --notify
```

### Telegram Bot

```
/scout now          # Trigger immediate sweep
/status             # Check last discovery
/latest             # Show last 5 models
/trending           # Show trending this week
/search <query>    # Search catalog
/alert <keywords>  # Set custom alerts
```

---

## Scout Agents

### Agent: HuggingFace Scout

```python
class HuggingFaceScout:
    """Discovers models from HuggingFace Hub."""
    
    def scan_trending(self):
        # API: /api/trending
        return models
    
    def scan_new(self, since="24h"):
        # API: /api/models?sort=created
        return new_models
    
    def evaluate_model(self, model_id):
        # Parse model card, benchmarks
        return evaluation
```

### Agent: GitHub Crawler

```python
class GitHubCrawler:
    """Finds model implementations and GGUFs."""
    
    def search_new_repos(self):
        # GitHub search API
        # Query: GGUF OR safetensors created:>{date}
        return repos
    
    def check_ollama_ready(self, repo):
        # Check for Modelfile, GGUF
        return compatibility
```

---

## Roadmap

### v0.1.0 (This Week)
- [ ] HuggingFace Scout
- [ ] GitHub Crawler
- [ ] Basic Model Card parser
- [ ] Telegram notifications

### v0.2.0 (Next Week)
- [ ] Ollama Library watcher
- [ ] Benchmark extraction
- [ ] Trend analysis
- [ ] Weekly digest

### v0.3.0 (Month 2)
- [ ] Research paper linkage (ArXiv)
- [ ] Performance predictions
- [ ] Use-case recommender
- [ ] Community voting

---

## Integration with Swarm

ScoutForge feeds into your existing infrastructure:

```
ScoutForge discovers → SovereignStack evaluates → 
SentientForge optimizes → Ollama runs locally
```

**Auto-Pilot Mode:**
- Discovers promising model
- Evaluates against ACS benchmarks
- Auto-pulls to Ollama if ACS > 0.85
- Notifies Z via Telegram

---

## License

MIT — See [LICENSE](LICENSE)

---

*Part of the 0x-wzw Swarm Ecosystem*  
*Complement to SentientForge & SovereignStack*
