<div align="center">

# Jhye O'Meley

### Product engineer · SaaS founder · open-source contributor

I design, build, test, and ship production software — from early product decisions through to reliable delivery.

Tokyo, Japan · Founder at BizBeam

[Portfolio](https://jhye.dev) · [LinkedIn](https://www.linkedin.com/in/jhye-o-meley-529960213/) · [GitHub](https://github.com/TheJhyeFactor)

</div>

---

## What I do

I turn operational problems into focused software products. My work spans product discovery, interface design, full-stack engineering, automation, testing, deployment, and the documentation needed to keep systems maintainable.

I am currently focused on native developer tools, privacy-conscious web products, SaaS platforms, and upstream performance and reliability work across projects including Ollama, OpenTelemetry Go, Charmbracelet Crush, and PyInstaller.

## Featured build — Codex Meter

<a href="https://github.com/TheJhyeFactor/codex-meter">
  <img src="https://raw.githubusercontent.com/TheJhyeFactor/codex-meter/main/docs/images/hero.svg" alt="Codex Meter — a native macOS menu bar app for Codex usage limits and local activity" />
</a>

[Codex Meter](https://github.com/TheJhyeFactor/codex-meter) is a free, open-source macOS menu bar app for monitoring Codex limits, reset times, local model usage, and API-equivalent cost estimates.

- Native Swift 6 application for Apple silicon and Intel Macs
- Local-first activity analysis with no analytics service or external database
- Honest stale and error states instead of invented usage estimates
- Scriptable CLI, CI validation, and automated release workflow
- MIT licensed with downloadable community builds

[Source code](https://github.com/TheJhyeFactor/codex-meter) · [Latest release](https://github.com/TheJhyeFactor/codex-meter/releases/latest) · [Architecture](https://github.com/TheJhyeFactor/codex-meter/blob/main/docs/architecture.md)

## Open-source engineering

### Ollama — streaming performance and network reliability

- [Coalesced high-rate chat stream updates](https://github.com/ollama/ollama/pull/17258), reducing React Query cache commits from 200 to 51 in a deterministic stream test while preserving immediate first output and final state.
- [Closed a first-byte download-stall gap](https://github.com/ollama/ollama/pull/17259), added race-tested regression coverage, and removed a fixed completion polling tail measured at 1.001 seconds down to 689.5 microseconds in the scoped local benchmark.
- [Added retries for interrupted model-manifest pulls](https://github.com/ollama/ollama/pull/17260), covering failures before response headers and mid-body disconnects without increasing healthy-path allocations.

### Charmbracelet Crush — LSP discovery performance

[Moved language-server relevance filtering ahead of PATH lookup](https://github.com/charmbracelet/crush/pull/3370), avoiding thousands of unnecessary filesystem checks for unrelated servers. In the controlled 300-server discovery benchmark, median time fell from 50.82 ms to 308.61 µs, allocated memory fell 238×, and allocations fell 96×. The change includes regression tests, race builds, linting, and CPU/allocation profile evidence.

### OpenTelemetry Go — cross-platform CI

[Added a compile-only cross-build workflow](https://github.com/open-telemetry/opentelemetry-go/pull/8634) covering Go 1.25 and 1.26 across 14 target platforms. The change introduces a 28-job matrix, a stable aggregate check, and a Make target that validates foreign `GOOS`/`GOARCH` combinations without trying to execute cross-compiled test binaries.

### PyInstaller — macOS runtime guidance

[Documented macOS Finder launch context and bundle-safe resource handling](https://github.com/pyinstaller/pyinstaller/pull/9485), including writable-state placement and a reproducible diagnostic workflow. Validation included a warnings-as-errors Sphinx build and a signed windowed application launched through macOS LaunchServices.

### Maintained open source

[Codex Meter](https://github.com/TheJhyeFactor/codex-meter) is maintained as a public MIT-licensed product with native Swift source, CI, release automation, architecture documentation, and downloadable builds. The current public release is [v1.5.0](https://github.com/TheJhyeFactor/codex-meter/releases/tag/v1.5.0).

> The upstream pull requests above are under maintainer review. Benchmark figures describe the linked controlled test harnesses, not whole-application speedups.

## Selected products

| Product | Engineering focus | Links |
| --- | --- | --- |
| CareerLift | Privacy-first resume and cover-letter workflows, browser persistence, live preview, and document export | [Source](https://github.com/TheJhyeFactor/careerlift) · [Live product](https://thejhyefactor.github.io/careerlift/) |
| PDF Power Tools | Client-side PDF splitting, merging, OCR, annotation, signatures, redaction, and compression without document uploads | [Source](https://github.com/TheJhyeFactor/pdf-tools) · [Live product](https://thejhyefactor.github.io/pdf-tools/) |
| WebOS | Browser desktop environment with window management, terminal emulation, applications, and a persistent virtual filesystem | [Source](https://github.com/TheJhyeFactor/browser-os) · [Live product](https://thejhyefactor.github.io/browser-os/) |
| jhye.dev | Responsive product portfolio with structured content, documented architecture, automated checks, and static deployment | [Source](https://github.com/TheJhyeFactor/jhye-dev) · [Live site](https://jhye.dev/) |

## Engineering scope

**Product engineering:** TypeScript, React, Next.js, JavaScript, Node.js, Firebase, Firestore<br/>
**Native and systems:** Go, Swift, Python, macOS application development, networking, CLI tooling, packaging<br/>
**Performance and reliability:** deterministic benchmarks, `pprof`, `benchstat`, race detection, regression testing<br/>
**Quality and delivery:** automated testing, GitHub Actions, cross-platform CI/CD, Docker, Vercel, GitHub Pages<br/>
**Product practice:** workflow design, UX systems, accessibility, technical writing, production readiness

## How I work

- Start with the operating problem and the people who have to use the product.
- Prefer clear workflows and maintainable systems over unnecessary complexity.
- Treat testing, security, accessibility, documentation, and deployment as part of the build.
- Make claims that can be supported by working software, source code, or validation evidence.

<details>
<summary>Contribution activity</summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/TheJhyeFactor/TheJhyeFactor/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/TheJhyeFactor/TheJhyeFactor/output/github-contribution-grid-snake.svg" />
  <img src="https://raw.githubusercontent.com/TheJhyeFactor/TheJhyeFactor/output/github-contribution-grid-snake.svg" alt="Animated contribution graph" />
</picture>

</details>

---

<div align="center">

Open to thoughtful engineering collaborations and product-focused opportunities.

</div>
