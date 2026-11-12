# CLAUDE.md

Project etiquette for this repo. Claude reads this on startup.

## Git
- Commits in Conventional Commits format: `type(scope): description`
  (`feat`, `fix`, `docs`, `refactor`, `test`, `chore`).
- Branch names: `feat/<short-name>` or `fix/<short-name>`.
- Add a `Co-Authored-By: Claude <noreply@anthropic.com>` trailer to commits you make.
- Never commit `.env`. Only `.env.example` with placeholder values stays in the repo.

## Pull requests
- Платформа: GitHub. PR відкриваємо через `gh pr create`.
- Заголовок PR - у форматі коміта: `тип(область): опис`.
- Тіло PR: розділи «Що змінилось» і «Навіщо»; рядок `Closes #<issue>`.
- Новий PR відкриваємо як `--draft`, поки робота не завершена.
