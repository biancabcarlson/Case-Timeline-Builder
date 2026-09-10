# Timeline Builder

**🔗 Live demo:** https://biancabcarlson.github.io/Case-Timeline-Builder/

Turns raw, unordered investigator notes (dates + descriptions) into a clean, numbered, chronological timeline. Flags unusually large time gaps between entries so nothing gets missed when compiling the case file. Works entirely on data you provide — no data source is bundled or assumed.

Accepts notes in the shorthand investigators actually write them in — no rigid template. A line
can start with an ISO date (`2026-08-28T18:41`), a US-style date (`8/28`, `8/28/2026`, `8/28/26`),
or a month name (`Aug 28, 2026`, `August 28`); the time is optional and can be 12-hour
(`6:41pm`) or 24-hour (`18:41`); and the timestamp can be separated from the note by a dash,
colon, comma, or nothing at all. Lines with no year default to a "case year" you set; lines
with no time are still placed in the timeline but marked as time-not-specified.

- **Web demo:** loads prefilled with this case's account history (from the
  `simulated-account` fixture) and renders it visually (numbered/icon markers, one
  entry per row) with gap warnings attached inline to the relevant pair of events.
  A **Timeline range** (From/To) filter is prefilled to the suspected fraud dates
  so the default view stays focused instead of showing the account's entire
  history — widen the range to bring earlier context into view. Gap flagging
  states the size of the gap directly, rounded to the nearest whole day (e.g.
  "Gap of 2 days") rather than a generic alert label or a decimal.
  - **Adding a note:** when a new note clearly refers to a known event in the
    account history (e.g. "added beneficiary"), its date/time is matched and
    filled in automatically. When it doesn't match anything (e.g. a short or
    generic note like "test"), you're prompted to set the date/time yourself
    instead of it silently getting today's real-world date — either way the
    range auto-widens if the note falls outside it.
  - **Select event:** click "Select event" to enter edit mode, then click any
    entry in the timeline to edit its note text, move it to a different
    date/time (it re-sorts into place), or delete it (behind a confirm step).
- **Python CLI:** accepts either a JSON file of structured events, or a plain `.txt` file of free-text note lines using the same flexible parsing as the web demo. Outputs a chronological timeline in Markdown.

## Other tools in this series

- [Case Calculator](https://biancabcarlson.github.io/Case-Calculator/)
- [Report Template Filler](https://biancabcarlson.github.io/Report-Template-Filler/)
- [OSINT Tool](https://biancabcarlson.github.io/OSINT-Tool/)
- [Case Doc Tracker](https://biancabcarlson.github.io/Case-Doc-Tracker/)
- [Entity Name Matcher](https://biancabcarlson.github.io/Entity-Name-Matcher/)
- [Timeline Builder](https://biancabcarlson.github.io/Case-Timeline-Builder/) *(this repo)*
