# 🐝 HiveMind@home & La Ruche — The Cyber-Bee Community Supercomputer (`v3.8.0` Season 16 Live)

[![Live GitHub Pages Portal](https://img.shields.io/badge/HiveMind%40home_Web_Portal-Live_on_GitHub_Pages-f59e0b?style=for-the-badge&logo=github)](https://xaviercallens.github.io/HiveMindatHome.github.io/)
[![Live OpenRouter Gateway](https://img.shields.io/badge/Live_OpenRouter_Gateway-7_Models_Online-10b981?style=for-the-badge&logo=googlecloud)](https://hivemind-openrouter-cfhmhmvv5a-uc.a.run.app)
[![Live GCP Cloud Run API](https://img.shields.io/badge/Live_GCP_Cloud_Run_API-hivemind--at--home--ruche-00f0ff?style=for-the-badge&logo=googlecloud)](https://hivemind-at-home-ruche-cfhmhmvv5a-uc.a.run.app)
[![Zenodo DOI v3.8.0](https://img.shields.io/badge/Zenodo_v3.8.0-10.5281%2Fzenodo.23649757-1682d4?style=for-the-badge)](https://doi.org/10.5281/zenodo.23649757)
[![Core Repository](https://img.shields.io/badge/Core_Engine-xaviercallens%2FHiveMind-a855f7?style=for-the-badge&logo=github)](https://github.com/xaviercallens/HiveMind)

> **Strictly Non-Monetary Compute-Reciprocity Charter (`0.00 EUR / 0.00 USD`)**: Share your idle consumer GPU when you are not gaming, earn **HiveMind Compute Points (`HMT`)**, and spend them anytime on your own AI & scientific needs—or download the open pretrained **Sparse Mixture-of-Experts (MoE)** models directly from **`La Ruche`**!

---

> **Weekend campaign notice (14–15 Nov 2026):** the live services are under intense training load. Responses may be slower and some requests may be rate-limited (HTTP 429). Please retry after a minute. Updates: [GitHub Discussions](https://github.com/xaviercallens/HiveMind/discussions).

## 📑 Contents

- [Join the Hive in 5 minutes](#-join-the-hive-in-5-minutes--pick-your-role) — consumer, producer, prosumer, trainer
- [Live services & Season 16 results](#-live-services--season-16-results)
- [The bee & hive concept](#-the-bee--hive-concept-in-simple-terms)
- [Repository layout & contributing](#-repository-layout--contributing)
- [Maintainers: GitHub Pages domain](#-maintainers-github-pages-domain)
- [License & charter](#-license--non-monetary-charter)

---

## 🚀 Join the Hive in 5 Minutes — Pick Your Role

All roles start with the same install, then register with `--role`. Roles are not exclusive.

```bash
git clone https://github.com/xaviercallens/HiveMind.git && cd HiveMind
uv venv && uv pip install -e ".[dev]"
```

| Role | You are… | What to do | Earn / get |
| :--- | :--- | :--- | :--- |
| 💻 **Consumer** | Using the models, no GPU needed | `python scripts/hivemind_connect.py register --handle YOU --role consumer --save-key ~/.hivemind_key`, then `... snippet continue --model coder` (also OpenCode, Cline, Aider, Zed). Or sign in with Google at the gateway's `/signup` (+100 HMT). | Spend HMT on `hivemind/*` models |
| 🐝 **Producer** | Sharing an idle GPU (NVIDIA, ROCm, Apple Silicon) | Run Ollama / vLLM / llama.cpp, put it behind `scripts/hivemind_producer_shield.py` (zero-trust proxy, default port 8787; see `--help`), then `register --role producer`. Pick a model that fits your VRAM: 4 GB `crowd-v1`/`coder-lite`, 6 GB `coder`, 12 GB `coder-plus`. | HMT per token served |
| 🧩 **Prosumer** | Both: produce while idle, consume bigger models | `register --role prosumer`, then `check` for balance, live models and tiers. | Earn on a small GPU, spend on 7B–30B models |
| 🧬 **Trainer** | Leaving a 6 GB+ GPU on overnight | `python -m hivemind.cli.main hardware-check`, then `uv run python scripts/run_community_gpu_benchmark.py --contributor-handle YOU` (< 1.5 GB VRAM) and post the `receipt_sha256` in [Discussion #84](https://github.com/xaviercallens/HiveMind/discussions/84). Nightly QLoRA workunits (22:00–07:00 CET) are accepted only if they pass the non-regression gate. Prefer BOINC? See [BOINC volunteer install](#-boinc-volunteer-install-idle-gpu) below. | Highest HMT yield; new domains via a `[Bee-Proposal]` issue |

Producers see the prompts they serve, so never send secrets. Gaming is never blocked: the node yields in under 1.5 s. HMT have no cash value.

### 🧮 BOINC volunteer install (idle GPU)

Ready-made installers live in [`boinc/`](boinc/). They install the official Berkeley BOINC client, attach it to the La Ruche project (`hivemind_astro_bls`, `hivemind_sundials_ode`) and start an idle-GPU worker that pauses compute the moment you start a game.

| Platform | Command |
| :--- | :--- |
| Linux / macOS | `curl -sSLO https://xaviercallens.github.io/HiveMindatHome.github.io/boinc/install_boinc_hivemind_linux.sh`, read it, then `bash install_boinc_hivemind_linux.sh "@YourHandle"` |
| Windows 10/11 | Download [`Install_BOINC_HiveMind_Windows.ps1`](boinc/Install_BOINC_HiveMind_Windows.ps1), read it, then run `powershell -ExecutionPolicy Bypass -File Install_BOINC_HiveMind_Windows.ps1 -Handle "@YourHandle"` |
| Docker + NVIDIA GPU | `docker compose -f boinc/docker-compose.boinc.yml up -d` (see [`docker-compose.boinc.yml`](boinc/docker-compose.boinc.yml)) |

> Always read a script before running it. The installers use `sudo`/`winget` to install packages. The Docker file sets a default BOINC GUI-RPC password (`hivemind_rpc_local`) and enables remote GUI RPC: change it, and do not expose port 31416 to the internet.

---

## ⚡ Live Services & Season 16 Results

> Season 16 live Production Swarm, Dual-GPU (RTX 2070 inference + Tesla T4 6-domain BOINC MoE QLoRA).

| Portal / Service | Live URL | Key Capabilities & Endpoints |
| :--- | :--- | :--- |
| **🐝 HiveMind@home 5-Language Web Site** | **[`https://xaviercallens.github.io/HiveMindatHome.github.io/`](https://xaviercallens.github.io/HiveMindatHome.github.io/)** & **[`https://xaviercallens.github.io/`](https://xaviercallens.github.io/)** | 5-Screen Interactive Cyber-Bee Portal in `EN • FR • 中文 • ES • DE` + Live S16 Dual-GPU Telemetry Deck |
| **⚡ HiveMind OpenRouter Gateway** | **[`https://hivemind-openrouter-cfhmhmvv5a-uc.a.run.app`](https://hivemind-openrouter-cfhmhmvv5a-uc.a.run.app)** | OpenAI-compatible `POST /v1/chat/completions`, [`/signup`](https://hivemind-openrouter-cfhmhmvv5a-uc.a.run.app/signup) (`+100.0 HMT`), [`/v1/models`](https://hivemind-openrouter-cfhmhmvv5a-uc.a.run.app/v1/models) (**7 live models**), [`/v1/hivemind/t4/status`](https://hivemind-openrouter-cfhmhmvv5a-uc.a.run.app/v1/hivemind/t4/status) |
| **🍯 La Ruche Honeycomb MoE Portal** | **[`https://hivemind-at-home-ruche-cfhmhmvv5a-uc.a.run.app`](https://hivemind-at-home-ruche-cfhmhmvv5a-uc.a.run.app)** | Interactive 8-Alvéole Sparse MoE Vault, [`/night-moe`](https://hivemind-at-home-ruche-cfhmhmvv5a-uc.a.run.app/night-moe) McNemar benchmark report, and live T4/RTX 2070 GPU banner |
| **🛰️ HiveMind@home Tribute Node** | **[`https://hivemind-at-home-cfhmhmvv5a-uc.a.run.app`](https://hivemind-at-home-cfhmhmvv5a-uc.a.run.app)** | Tribute to `SETI@home`, `Folding@home`, and `BOINC` with live Spectrum & $E_8$ Lattice Waterfall |
| **📚 Zenodo `v3.8.0` Deposit** | **[`https://doi.org/10.5281/zenodo.23649757`](https://doi.org/10.5281/zenodo.23649757)** | 33-page Foundational Paper `v3.8.0` + 99 checksum-verified empirical & Lean 4 artifacts (`PR #200`) |

### 🖥️ Dual-GPU Division of Labor (RTX 2070 Live Inference + Tesla T4 Chained 6-Domain BOINC MoE QLoRA)

1. **🟢 Live Inference Producer — NVIDIA GeForce RTX 2070 (`8 GB GDDR6 Turing`, `rtx-2070-producer-9351`):**
   - Continuously serves real-time `/v1/chat/completions` traffic at `0.25 HMT / 1k tokens` (`p50 = 177–296 ms`, `p95 = 469 ms`) across **7 live models**: `hivemind/auto`, `hivemind/bee-stars`, `hivemind/coder`, `hivemind/coder-lite`, `hivemind/coder-plus`, `hivemind/moe-coder`, and `hivemind/moe-general`.
2. **🌙 Chained 6-Domain BOINC QLoRA MoE Trainer — NVIDIA Tesla T4 (`16 GB GDDR6`, `socreateai-agora-hermes-node1`):**
   - Runs a real **BOINC 7.18.1 / 7.24 server stack** (`hivemind_qlora_moe`) training **`ibm-granite/granite-3.1-1b-a400m-base`** (`1.3B` Sparse MoE, `400M` active parameters, NF4 + fp32 LoRA $r=8, \alpha=16$, `1,376,256` trainable parameters) with **6-Domain Interleaved Replay** (`general`, `french`, `edu_web`, `news`, `biomed`, `math`), **Thermodynamic Monotonic Ratchet Gate ($\Delta \mathcal{L}_{\text{eval}} \le 0$)**, and `< 1.0s` automatic inference preemption.

| BOINC Workunit | Focus Domain & Corpus | Chained | 6-Domain Mean Eval Loss | Net $\Delta$ vs Base (`2.2705`) | Per-Domain Held-Out Highlights (`same_class_exact=true`, `div=0.0`) | Ratchet Status |
| :--- | :--- | :---: | :---: | :---: | :--- | :---: |
| **`hmq_00001`** | `general` (`Salesforce/wikitext-2-raw-v1`) | Seed | `2.0992` *(1-dom)* | `-0.1805` *(general)* | **`general`: `2.2796` $\rightarrow$ `2.0992` (`-0.1805`)** | Seed Head |
| **`hmq_00004`** | `news` (`abisee/cnn_dailymail`) | `True` | `2.5860` | — | **`news`: `2.2988` $\rightarrow$ `2.1973` (`-0.1015`)** | Domain Sweep |
| **`hmq_00005`** | `biomed` (`ccdv/pubmed-summarization`) | `True` | `2.8422` | — | **`biomed`: `2.8506` $\rightarrow$ `2.3242` (`-0.5264`, below `2.5017` base)** | Domain Sweep |
| **`hmq_00006`** | `math` (`openai/gsm8k`) | `True` | `2.4582` | — | **`math`: `2.5048` $\rightarrow$ `1.4915` (`-1.0133`, below `1.6440` base)** | Domain Sweep |
| **`hmq_00007`** | `general` + 6-Domain Replay (Shard 1) | `True` | **`2.2288`** | **`-0.0417`** | **All 6 domains dropped simultaneously:** `biomed: 2.3018`, `general: 2.1886`, `math: 1.4550`, `news: 2.2061` | **ACCEPTED** |
| **`hmq_00012`** | `math` + 6-Domain Replay (Shard 1) | `True` | **`2.2196`** | **`-0.0509`** | **`math`: `1.4308` (`-0.2132` vs base)**, `biomed: 2.2836`, `general: 2.1801`, `news: 2.1901` | **ACCEPTED** |
| **`hmq_00013`** | `general` + 6-Domain Replay (Shard 2) | `True` | **`2.2012`** | **`-0.0693`** | `general: 2.1608`, `french: 2.4982`, `edu_web: 2.6538`, `biomed: 2.2726`, `news: 2.1822` | **ACCEPTED** |
| **`hmq_00014`** | `french` + 6-Domain Replay (Shard 2) | `True` | **`2.1972`** | **`-0.0733`** | **`biomed: 2.2606`, `edu_web: 2.6416`, `french: 2.4754`, `general: 2.1522`, `math: 1.4630`, `news: 2.1902`** | **ACTIVE HEAD** |
| **`hmq_00016`** | `news` + 6-Domain Replay (Shard 2) | `True` | `2.2122` | `-0.0583` | **`news` lowered further to `2.1720` (`-0.1268` vs base)**; ratchet kept `hmq_00014` (`2.1972`) as head | Guarded |

- **🌟 `NIGHT-MOE-1` Validated Astrophysics Specialist (`hivemind/bee-stars`):** Trained on GAIA / Hipparcos Stellar Spectral Classification & Luminosity Pack ($n=317$), improving accuracy from **`0.489` $\rightarrow$ `0.893` (`+40.4%`, exact paired McNemar $p < 10^{-4}$, beating shuffled control `193` to `7`)**, now served live 24/7.
- **📊 Community Traffic & Hall of Honor:** **`5,230+` HTTP requests**, **`1,015+` browser visits**, **`40+` registrations**, **`595+` live `/v1/chat/completions`** (`0` HTTP 402/5xx). Special thanks to **Pioneer #1 (`fbc1d3042d377feba6b1e0ac6fd576a4`, `842.37 HMT`)**, **`u/artsnumeriques`** (`r/artificielle`), **`@clark719664`**, **`@pedromineo`**, **`@radialmonster`**, and **`@lyrasol99-dev`**.

---

## 🍯 The Bee & Hive Concept in Simple Terms

1. **🐝 Worker Bees (Your Idle Consumer GPU)**: Millions of gamers, astrophysicists, students, and citizen scientists have powerful consumer GPUs (RTX 2070/3060/4070/5060, Radeon, Apple Silicon) sitting **idle 80% of the day**. Together as a swarm of **Worker Bees**, they form a planetary supercomputer.
2. **🎮 Zero-Lag Gaming Preemption (`< 1.5s` Guarantee)**: The instant you launch *Cyberpunk 2077*, *Elden Ring*, *Steam*, or *Blender*, the hardware WDDM/NVML circuit-breaker detects your game in **under 1.5 seconds**, puts your Worker Bee to sleep, and frees **100% of your GPU & VRAM**.
3. **🍯 Gathering Nectar into `La Ruche` (The Honeycomb MoE Vault)**: When your PC is idle, your Worker Bee trains a compact **QLoRA specialist adapter** on curated scientific datasets and compresses its update **30.89x** using 8-dimensional **Gosset $E_8$ Lattice Quantization**.
4. **⚡ Earn & Spend HiveMind Compute Points (`0.00 EUR / 0.00 USD`)**: Every verified workunit awards **HiveMind Compute Points (`HMT`)** redeemable anytime on the Hive's **Sparse Mixture-of-Experts (MoE)** models.

---

## 🧰 Repository Layout & Contributing

| Path | What it is |
| :--- | :--- |
| `index.html` | The portal: a single self-contained page (5 languages, 6 screens). `hivemind_at_home_dashboard.html` must stay a byte-identical copy. |
| `hivemind_at_home_state.json` | Portal data and i18n dictionary, also embedded in `index.html`. Carries a `dashboard_state_sha256` over its contents. |
| `game.html`, `webgpu.html`, `cockpit-v46.html` | Playable browser games (USS HiveMind Exoplanet Hunter). |
| `boinc/` | BOINC client installers, configs and the idle-GPU worker. |
| `scripts/` | `check_site.py` (CI checks), `activate_hivemindathome_org_domain.sh`. |
| `sitemap.xml`, `robots.txt`, `404.html` | SEO and fallback pages. |

**Before opening a PR:** run `python3 scripts/check_site.py`. It checks for control characters (unescaped LaTeX backslashes), JSON/XML validity, that the dashboard copy and the embedded state match, that the state hash and all 5 languages' keys are consistent, and basic accessibility (skip link, labelled canvases, alt text). The same check runs in GitHub Actions on every push and PR.

**Editing tips:** write LaTeX in this README with doubled care (`\rightarrow`, not `\r`); change `index.html` and then `cp index.html hivemind_at_home_dashboard.html`; after editing the state, recompute the hash with `json.dumps(state_without_hash, sort_keys=True)` + SHA-256. Questions and ideas: [GitHub Discussions](https://github.com/xaviercallens/HiveMind/discussions).

---

## 🌐 Maintainers: GitHub Pages Domain

Activating `https://hivemindathome.github.io/`:

Per [GitHub's official Pages documentation (*Types of GitHub Pages sites*)](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages#types-of-github-pages-sites):
1. **Current Live User & Project Sites (`200 OK` with Enforced HTTPS):**
   - **Project Site (`xaviercallens/HiveMindatHome.github.io`):** **[`https://xaviercallens.github.io/HiveMindatHome.github.io/`](https://xaviercallens.github.io/HiveMindatHome.github.io/)**
   - **Apex User Site (`xaviercallens/xaviercallens.github.io`):** **[`https://xaviercallens.github.io/`](https://xaviercallens.github.io/)**
2. **Activating the Apex Organization Subdomain `https://hivemindathome.github.io/`:**
   - GitHub reserves `https://<account>.github.io/` exclusively for a User or Organization account named `<account>` owning a repository named `<account>.github.io`.
   - Because GitHub's REST API does not allow automated creation of free organizations on `github.com`, simply click **[Create Free Organization on GitHub](https://github.com/account/organizations/new?plan=free)** and enter **`HiveMindatHome`** as the organization name (`10 seconds`), then run:
     ```bash
     ./scripts/activate_hivemindathome_org_domain.sh
     ```
   - This script automatically creates/mirrors `HiveMindatHome/hivemindathome.github.io`, enables GitHub Pages with HTTPS enforcement, and brings **`https://hivemindathome.github.io/`** online immediately.

---

## 📜 License & Non-Monetary Charter

Released under the **Apache-2.0 License** and governed by the **Strictly Non-Monetary Compute-Reciprocity Charter (`0.00 EUR / 0.00 USD`)**.
