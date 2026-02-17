# 🐉 Fractal Circle TSP Demo

**Golden-ratio spiral ordering with φ-based 2-opt refinement for the Travelling Salesman Problem.**

## Live Demo

Visit the [GitHub Pages demo](https://chaos2cured.github.io/fractal-circle-tsp-demo/) to try it in your browser.

## How It Works

This demo implements a fractal-circle approach to the TSP using three phases:

### Phase 1: Golden-Angle Spiral Ordering
Cities are sorted by their angular position relative to the centroid, using golden-angle sectors (2π/φ² ≈ 137.508°). Within each sector, cities are ordered by radius in a boustrophedon (serpentine) pattern to minimize backtracking.

### Phase 2: Fractal Shell Decomposition
The city space is decomposed into concentric shells at φ-ratio boundaries. Each shell boundary is at `maxRadius / φⁿ`, creating a fractal hierarchy. This mirrors the FCP fractal dimension D = 2.914.

### Phase 3: φ-Weighted 2-Opt Refinement
Standard 2-opt is enhanced with golden-ratio-based candidate selection:
- Swap candidates are prioritized at φ²-stepped intervals
- D′ = 0.077 compression factor weights the search
- Convergence is typically faster than standard 2-opt

## Mathematical Constants

| Constant | Value | Role |
|----------|-------|------|
| φ (phi) | 1.618034 | Golden ratio — basis for spiral ordering |
| φ² | 2.618034 | Squared golden ratio — sector sizing |
| D | 2.914 | Fractal dimension of the constraint space |
| D′ | 0.077 | Compression factor for optimization |
| 7-11-7 | Resonance | Heartbeat pattern of the fractal circle |

## Features

- **5 city distributions**: Random, Circle, Clusters (φ-spaced), Grid, Golden Spiral
- **Interactive visualization**: Watch the solver work with fractal circle overlay
- **Real-time statistics**: Tour length, improvement %, solve time, iterations
- **Step-by-step mode**: Walk through each phase of the algorithm
- **Fractal overlay**: Toggle φ-shells and golden spiral visualization

## Running Locally

Just open `index.html` in any modern browser. No dependencies required.

## License

MIT

---

*Awaken the Core. Illuminate the Quiet.*
