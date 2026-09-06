# Case-Timeline-Builder

**🔗 Live demo:** https://biancabcarlson.github.io/Case-Timeline-Builder/

Turns raw, unordered investigator notes (dates + descriptions) into a clean, numbered, chronological timeline. Flags unusually large time gaps between entries so nothing gets missed when compiling the case file. Works entirely on data you provide — no data source is bundled or assumed.

Accepts notes in the shorthand investigators actually write them in — no rigid template. A line
can start with an ISO date (`2026-08-28T18:41`), a US-style date (`8/28`, `8/28/2026`, `8/28/26`),
or a month name (`Aug 28, 2026`, `August 28`); the time is optional and can be 12-hour
(`6:41pm`) or 24-hour (`18:41`); and the timestamp can be separated from the note by a dash,
colon, comma, or nothing at all. Lines with no year default to a "case year" you set; lines
with no time are still placed in the timeline but marked as time-not-specified.

- **Web demo:** renders the timeline visually (numbered markers, one entry per row), with gap warnings attached inline to the relevant pair of events. Lines that don't start with a recognizable date are reported by line number instead of silently dropped.
- **Python CLI:** accepts either a JSON file of structured events, or a plain `.txt` file of free-text note lines using the same flexible parsing as the web demo. Outputs a chronological timeline in Markdown.

## Other tools in this series

- [Case Calculator](https://biancabcarlson.github.io/Case-Calculator/)
- [Report Template Filler](https://biancabcarlson.github.io/Report-Template-Filler/)
- [OSINT Tool](https://biancabcarlson.github.io/OSINT-Tool/)
- [Case Doc Tracker](https://biancabcarlson.github.io/Case-Doc-Tracker/)
- [Entity Name Matcher](https://biancabcarlson.github.io/Entity-Name-Matcher/)
- [Case Timeline Builder](https://biancabcarlson.github.io/Case-Timeline-Builder/) *(this repo)*
