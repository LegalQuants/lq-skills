# CHANGELOG.md

This tracks the current version mainatained in the lq-skills repository.
For the latest developed version of coquill, refer to https://github.com/houfu/coquill

## v 3.0.0+Cicero -- The "Cicero" release (the original version on lq-skills)
**New Features**
* Markdown templates — .md files are now a fully supported template format, rendered via Jinja2 with optional PDF output (via markdown + weasyprint)
* PDF output for .docx templates — produced automatically when Microsoft Word (docx2pdf) or LibreOffice is available; soft-fails with a warning if neither is found
* Interview transcripts — every document assembly session now saves an interview_log.json and a human-readable transcript.md to the job folder, recording questions asked, answers given, and confirmed values
* Transcriber (coquill-transcriber) — generates transcript.md from the interview log after each document assembly session
* On-demand dependency installation — docx2pdf is installed only for docx jobs, weasyprint only for HTML/markdown jobs; no unnecessary packages loaded
* Modular renderer — rendering logic extracted into a dedicated render.py script for cleaner skill architecture
* Conditional logic with {% if %} / {% else %} / {% endif %} support
* Loop sections with {% for item in items %} / {% endfor %} support
* Developer configuration via optional config.yaml per template
* Interview grouping, conditional groups, and loop groups
* Cross-field validation rules
* Skill separation: Orchestrator, Analyzer, and Renderer skills
* Manifest v2 schema with schema_version: 2, conditionals, loops, and dependencies
* Enhanced Meeting Notes example template (md) demonstrating all v2 features: choice variables, equality and boolean conditionals, loops, and config.yaml
* Simple variable substitution in .docx and .html templates. Jinja2-style {{ variable_name }} placeholders with type inference from name suffixes.
