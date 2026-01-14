## 2024-07-25 - Keep PRs Focused

**Learning:** Pull requests must be narrowly focused on a single concern. For Palette, UX improvements should not be bundled with unrelated project configuration changes (e.g., adding `.gitignore` or `package.json`), as this is considered "over-reaching" and will be rejected in review.

**Action:** When implementing a UX fix, ensure the commit only contains files directly related to that fix. Create separate PRs for any proposed changes to the project's tooling or configuration.