## 2024-07-25 - Skip Link Implementation Learnings
**Learning:** A "skip to content" link's CSS for hiding it off-screen is more robust using `transform: translateY(-100%)` than absolute positioning like `top: -40px`, as it avoids being clipped by parent elements with `overflow: hidden`.
**Action:** Default to using `transform` for off-screen positioning of focusable elements to ensure they appear as expected.

**Learning:** Site-wide smooth scrolling JavaScript (e.g., `a[href^="#"]`) can conflict with the native functionality of accessibility links like skip links.
**Action:** When implementing a skip link, always check for custom scroll-handling JavaScript and modify the selectors to exclude the skip link (e.g., `a[href^="#"]:not(.skip-link)`).

**Learning:** When adding attributes (like an `id` for a skip link target), double-check that the `class` attribute is not accidentally removed or replaced, as this can lead to significant visual regressions by un-styling critical layout components.
**Action:** Use a "search and replace" strategy that surgically adds the `id` attribute without altering the existing `class` attribute. Always verify layouts on multiple pages after such a change.
