# @ApacheIceberg YouTube: source research (2026-11-13)

**Bottom line:** YouTube auto-captions (the `en-orig` json3 track via `yt-dlp`) exist on every recent video and take seconds to fetch. Audio download is blocked from cloud IPs (HTTP 403 or a bot check), so Whisper only works as a fallback if audio can come from somewhere else.

## Inventory
- **Catalogue:** 383 videos, about 292 hours. No Shorts, and no /streams tab: recordings are uploaded after each meeting.
- **Cadence:** excluding conference batches, 2–4 sync recordings a week.
- **Upload delay:** a median of 2 days after the meeting, but 13 of 57 took 10–33 days, and uploads arrive out of order. **Detect new videos by ID, not by date window.**
- **Playlists (17), largest:**
  - Community Syncs 67, Summit 2026 72, Summit 2025 62, Talks 43, Summit 2024 32.
  - Index Support 17, MV 16, Read Restrictions 14, Tutorials 13, Column Updates 12.
  - UDF 11, V4 Single File Commit 10, Rust 8 (plus a duplicate playlist), Spark 7, Constraints 2.
  - 51 videos are in no playlist. There is no playlist for the Catalog, Variant or Shared Conformance Testing syncs.
- **Metadata:** descriptions usually hold only the series name and a link to the notes doc. Tags are generic and useless.

## Transcripts
- **Track:** `en-orig` auto-captions. The `en` track is a translation and returns 429s.
- **Size and speed:** 6.5k–9.9k words per meeting (about 9–11k words, 60–70k tokens, per hour). Three videos fetched in 31 s.
- **Quality:**
  - Good: punctuation, word timings, and `>>` speaker-change markers.
  - Bad: **no speaker names**, filler words, and misheard terms ("ice rust", "Pi iceberg").
- **Speaker attribution has to be inferred** from the notes doc agenda (`[Name] topic`), self-introductions and context. Mark it as inferred.

## Reliability for unattended runs
- **Metadata fetches:** about 30% hit "confirm you're not a bot" without a JS runtime. With `yt-dlp[default]` plus deno and 2–3 s sleeps there were no failures, though the bot check is intermittent.
- **Always-reliable listings:** `--flat-playlist` channel listing and the RSS feed (`https://www.youtube.com/feeds/videos.xml?channel_id=UCAg-s6wxgQRmEBohfuWTEXA`, last 15 uploads).
- **Job rules:**
  - Upgrade yt-dlp every run.
  - Retry with backoff.
  - Never mark a video done after a failure.

## Whisper fallback benchmark (CPU, 4 cores, int8)
- **faster-whisper:** base ≈ 3.4 min, small ≈ 7.7 min per hour of audio. Multi-speaker audio will likely be about 1.5× slower.
- **Limits:** no diarization, and it is only usable if audio is reachable.

## Old pipeline (Drive backup, built 2026-08-01, last update 2026-08-04)
- **Layout:** one folder per series (16 syncs plus `talks/`), with `index.md` and `YYYY/MM/<date>-<title>.md`.
- **Per-video file:** front matter and one long transcript paragraph. There are no timestamps and **no summaries**.
- **Coverage:** ends around early August 2026, so about 26 or more videos are missing.
- **Bug:** series indexes are not sorted correctly.
- **Verdict:** its layout is a reasonable template; the content needs regenerating with timestamps and summaries.

## Recommended sync
1. **Detect new videos:** a weekly flat listing (plus the RSS feed) against a processed-ID state file.
2. **For each new ID:** fetch metadata and `en-orig` json3 with 3–5 s sleeps. On failure, retry next run.
3. **Map the video to a working group:**
   1. Playlist membership.
   2. Otherwise, title regex rules.
   3. Otherwise `other-syncs` or `talks`.
   - Parse the meeting date from the title (`2026 11 09`, `10 28 2026`, `Oct 23 2026`, `08/24/2026`), falling back to the upload date.
4. **Storage:**
   - **Raw:** json3 plus a cleaned markdown transcript with timestamp links. Cheap to regenerate.
   - **Derived:** the meeting record (summary, decisions, actions, PRs and docs mentioned), joined with the notes-doc section for the same working group and date.
