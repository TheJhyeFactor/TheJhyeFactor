# Profile automation

The workflow in `.github/workflows/workflow.yml` generates the contribution
snake SVGs once per day, on pushes to `main`, or when started manually. It
publishes the generated files to the `output` branch:

- `github-contribution-grid-snake.svg`
- `github-contribution-grid-snake-dark.svg`

The job declares `contents: write` so its `GITHUB_TOKEN` can create or update
the output branch. GitHub must also allow repository workflows to use read and
write permissions: **Settings → Actions → General → Workflow permissions →
Read and write permissions**.

The README references the output branch through `raw.githubusercontent.com`.
The first successful workflow run is therefore required before the snake image
can render.
