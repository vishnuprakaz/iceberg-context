---
id: thread/t-23d6d63c9969129d
type: thread
title: 'Docs: duplicated search results on iceberg.apache.org'
date: '2026-05-14'
url: https://lists.apache.org/thread/vrt3oytl3dwo34wr07tkf73r0kkx0b1h
kind: discuss
status: consensus
messages: 14
sources:
- devlist:vrt3oytl3dwo34wr07tkf73r0kkx0b1h
refs:
- gh:apache/iceberg#14521
- gh:apache/iceberg#16368
- gh:apache/iceberg#16371
- gh:apache/iceberg#16398
links: []
updated: '2026-11-13'
---

# Docs: duplicated search results on iceberg.apache.org

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Docs: Are duplicated results in search on iceberg.apache.org a bug or a feature?](https://lists.apache.org/thread/vrt3oytl3dwo34wr07tkf73r0kkx0b1h) · **Started:** 2026-05-14 by Max Konstantinov · **Messages:** 14 (last 2026-05-19) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Max Konstantinov reported that search on iceberg.apache.org returns the same result many times because every documentation version from 1.4 to 1.10 is indexed, and asked whether that should be fixed. rmoff agreed the behaviour is poor since results do not show a version. Max suggested indexing only one version. RussellSpitzer and stevenzwu preferred search and navigation scoped to a selected version; kevinjqliu said that would mean migrating to mike (issue #14521), which is a lot of work, and supported indexing only latest or nightly. Max tested the mkdocs-exclude-search plugin, which left only nightly in the index, and opened a PR. kevinjqliu reported the fix live, added a fix for a second duplicate issue, suggested pointing the Docs tab and search at latest instead of nightly, and closed the loop once PRs #16368, #16371 and #16398 were merged.

**Why it matters:** Site search now covers a single documentation version, so older versions are reachable by URL but not through search.

## Outcome

Previous documentation versions were removed from the search index and the related PRs (#16368, #16371, #16398) were merged. ([message](https://lists.apache.org/thread/3stzqvrc429dm6trrvhv4g170nntol6x), `devlist:3stzqvrc429dm6trrvhv4g170nntol6x`)

## Positions

- **Max Konstantinov:** Exclude all but one documentation version from the search index as a quick fix, and look at a version selector separately. ([message](https://lists.apache.org/thread/optfgcg9hwhyjbobvymqgqvg1dj9dpm9))
- **[[person/rmoff|Robin Moffatt]]:** The current behaviour is not ideal for users because results are literal duplicates with no version shown. ([message](https://lists.apache.org/thread/tlo89xr7lm7h6d026q0j7745trm1jpdk))
- **[[person/RussellSpitzer|Russell Spitzer]]:** Asks whether a version dropdown could be added to search. ([message](https://lists.apache.org/thread/648ptz48qxk2lg9owp9zph5n6rzrfphy))
- **[[person/kevinjqliu|Kevin Liu]]:** Index only latest or nightly; a version selector would need a migration to mike, which is a lot of work and risks breaking the site. ([message](https://lists.apache.org/thread/b0bmsb0bx7q8zp5207srw3djc6n7coo4))
- **[[person/stevenzwu|Steven Wu]]:** Doc navigation and search should be scoped to a version, and restructuring the doc site might be a good idea. ([message](https://lists.apache.org/thread/j5y6hx6mk2jpxw9khvb3scoxsjgj6mbd))
- **[[person/rmannibucau|Romain Manni-Bucau]]:** Each version could be rendered independently into its own folder with a versions index and some JavaScript to list versions. ([message](https://lists.apache.org/thread/v6wxn21mp2nbflkgy080703on17zc2jc))

References: [iceberg#14521](https://github.com/apache/iceberg/issues/14521), [iceberg#16368](https://github.com/apache/iceberg/issues/16368), [iceberg#16371](https://github.com/apache/iceberg/issues/16371), [iceberg#16398](https://github.com/apache/iceberg/issues/16398)
<!-- kb:generated:end -->

## Notes
