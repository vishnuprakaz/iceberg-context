# GitHub, git history and governance: source research (2026-11-13)

## Access in this environment
- **Search API:** works through `gh api -X GET search/issues|commits`. Limits: 30 req/min, 1,000 results per query (slice by date beyond that).
  - Usable qualifiers: `reviewed-by:`, `review:none|approved|changes_requested`, `-linked:pr`, `involves:`, `commenter:`.
  - It **cannot** return merged_by, reviewer lists, review state per PR, or files changed.
- **REST `repos/apache/...`:** blocked in this session. GraphQL is denied too.
- **git clone of upstream works.** Use treeless clones for full history.
- **Who merged is unrecoverable.** 93% of iceberg commits have committer = GitHub (squash merges), and PyIceberg uses a merge queue. **Reviewers are the proxy for gatekeepers.**

## Governance
- **ASF data:** `whimsy.apache.org/public/committee-info.json` (PMC with join dates) and `public_ldap_projects.json` (committers).
- **PMC:** 26 members, chaired by Ryan Blue. Join dates:
  - 2020 founders: aokolnychyi, rdblue, cws, danielcweeks, jamestaylor, julien, omalley, parth, rdsr.
  - 2021: openinx, RussellSpitzer, jackye.
  - 2023: Fokko, stevenzwu, flyrain, szehon-ho.
  - 2024: honahx, liurenjie1024, amogh-jahagirdar, nastra, pvary.
  - Recent: kevinjqliu (2025-11), zeroshade (2025-11), singhpk234 and sungwy (2026-02), wgtmac (2026-09).
- **Other committers (14):** atserakhau, bryanck, dru/geruh, findepi, gooch, huaxingao, lzljs3620320, mxm, rymurr, schang/CTTY, sdd, shardul, xuanwo, yyan.
  - 11 of the 40 PMC members and committers had zero reviews in apache/iceberg in the last 6 months.
  - Logins for long-inactive people are derived guesses.
- **Triage collaborators (`.asf.yaml`):**
  - iceberg: marton-bod, samarthjain, SreeramGarlapati, gaborkaszab, bitsondatadev, ajantha-bhat, jbonofre, manuzhang, anuragmantri, nssalian.
  - pyiceberg: ajantha-bhat, ndrluis, rambleraptor.
- **Rules (site/docs/contribute.md and .asf.yaml):**
  - **Merging:** a committer other than the author merges, with 1 required approval. History is linear (squash or rebase). New public APIs wait at least 24 h before merge.
  - **Spec changes:** anything under `format/` or `open-api/rest-catalog*` needs its own dev@ vote unless an approved proposal covers it.
  - **Proposals:** a GitHub issue labeled `proposal`, then a [DISCUSS] thread, then a vote needing 3 binding PMC +1s.
  - **PR titles:** must match `Module: Description` (CI-enforced).
  - **AI use:** there is an AI-use disclosure policy.
  - **Stale bot:** PRs go stale at 30 days and close 7 days later; issues at 180 days, closing 14 days later.

## Module ownership
All-time / last-12-month commit counts are in brackets. Reviewers are counted on PRs created since 2026-05-13, excluding the reviewer's own PRs.

| Module | All-time owners | Recent contributors (12m) | Top reviewers (6m) |
|---|---|---|---|
| core (2459/426) | rdblue, aokolnychyi, nastra, amogh-jahagirdar | nastra, anoopj, gaborkaszab, dramaticlly, ebyhr | singhpk234, amogh-jahagirdar, nastra, huaxingao, anoopj, rdblue |
| api (892/123) | rdblue, aokolnychyi, nastra | anoopj, nastra, rdblue, uros-b | szehon-ho, huaxingao, nastra, amogh-jahagirdar |
| spark (2038/344) | aokolnychyi, rdblue, nastra, manuzhang, szehon-ho | manuzhang, nastra, aokolnychyi, ebyhr, pvary, anuragmantri | huaxingao, szehon-ho, RussellSpitzer, dramaticlly, nssalian |
| flink (1043/293) | stevenzwu, mxm, Guosmilesmile, openinx, pvary | mxm, Guosmilesmile, swapna267, talatuyarer | pvary, mxm, huaxingao, Guosmilesmile |
| spec/format (171/39) | emkornfield, rdblue, Fokko | huaxingao, danielcweeks, rdblue | RussellSpitzer, singhpk234, rdblue, stevenzwu, danielcweeks |
| open-api/REST (262/96) | nastra, Fokko | singhpk234, ebyhr, adutra | danielcweeks, nastra, singhpk234, gaborkaszab |
| parquet (366/75) | rdblue | nssalian, huan233usc, wombatu-kun | huaxingao, pvary, nssalian |
| data (330/51) | rdblue, aokolnychyi, openinx | Guosmilesmile, joyhaldar | pvary |
| kafka-connect (182/105) | bryanck, ebyhr | ebyhr, wombatu-kun | danielcweeks, bryanck, jbonofre |
| aws/gcp/azure | jackye, nastra, ebyhr | ebyhr, kevinjqliu, tom-s-powell | singhpk234, ebyhr |
| hive/mr/nessie/aliyun | marton-bod, pvary, ajantha-bhat | nearly dormant | — |
| docs/site/build | manuzhang, ajantha-bhat, Fokko, kevinjqliu | kevinjqliu, ebyhr, manuzhang, mxm | kevinjqliu, ebyhr |

- **Overall iceberg reviewers (6 months, excluding dependabot):** huaxingao 214, pvary 207, singhpk234 173, nastra 151, szehon-ho 121, ebyhr 119, amogh-jahagirdar 103, RussellSpitzer 95, kevinjqliu 90, nssalian 85, dramaticlly 85, anoopj 80, mxm 79, danielcweeks 73, rdblue 69, stevenzwu 67.
- **PyIceberg:**
  - Historical owner: Fokko, in every package.
  - Recent contributors: rambleraptor, kevinjqliu, geruh, ebyhr, rahulsmahadev, nssalian.
  - Reviewers (6 months): Fokko 183, rambleraptor 128, kevinjqliu 104, ebyhr 70, geruh 25. Everyone else is 6 or fewer, so **review capacity rests on about 5 people.**

## PR dynamics (12 months)
- **iceberg:**
  - 3,474 PRs opened (424 dependabot), 1,928 merged. Openings rose from about 200 to about 350 a month while merges stayed at about 170–200 a month: **demand is outgrowing review capacity.**
  - Human PRs: median time to merge 2.7 days (p75 12.7, p90 37).
  - 60% of closed human PRs merged; 681 were closed by the stale bot.
  - 612 authors; 205 of 294 git authors in the window were first-timers.
  - **Open:** 466 PRs.
    - Unreviewed: **383 non-draft PRs have no review, 277 of them 14 or more days old.**
    - 34 are approved but unmerged.
    - By title prefix: core 130, spark 65, api 34, docs 31, spec 26, flink 26.
- **iceberg-python:**
  - 1,315 opened (530 dependabot), 917 merged. Median time to merge 2.3 days; 68% of closed human PRs merged.
  - **Open:** 133, of which 121 are unreviewed (92 of those 14 or more days old).
  - Titles rarely carry module prefixes, so classify by the files they touch instead.

## Opportunity signals
- **iceberg:**
  - Issues: 458 open (134 bugs, 121 improvements, 24 proposals); 202 have no linked PR.
  - Labels: 8 good-first-issue; help-wanted is unused.
  - 19 bugs filed in the last 30 days.
- **pyiceberg:**
  - Issues: 164 open; 64 have no linked PR.
  - Labels: 3 good-first-issue (it uses `kind:*` labels).
  - 21 bugs filed in the last 30 days.
- **Demand without PRs:**
  - Variant proposal (72 👍) apache/iceberg#10392
  - Relative paths V4 #13141
  - File Format API #12225
  - Vortex #15416
  - Week transform #14220
  - PyIceberg: compaction iceberg-python#1092, PyArrow Dataset #30, VariantType #1819, REST views #818
- **Good first issues:** #15924 (stream DV rewrite) and #12937 (remove JUnit4 from Flink).
- **Recent bugs:**
  - #18748 (Flink upsert after spec change)
  - #18713 (Spark WAP with v3 DVs)
  - iceberg-python#4291 (partial deletes resurrect rows)
- **Stalled spec PRs (no review):** void transform #14778, collations #16972, expressions-spec alignment #17343.
- **Approved but unmerged:** the MV spec, #11041.

## Sibling repos
| Repo | Open PRs / issues | Merged per month (May–Oct 2026) | Top merged authors (6m) |
|---|---|---|---|
| iceberg-rust | 134 / 302 | 66→113 | dannycjones, xanderbailey, kevinjqliu, anoopj, blackmwk, mbutrovich, CTTY |
| iceberg-go | 57 / 63 | 87–294 | fallintoplace, Revanth14, badalprasadsingh, laskoviymishka, tanmayrauth, zeroshade |
| iceberg-cpp | 34 / 39 | 35–87 | zhjwpku, manuzhang, wgtmac, WZhuo, HuaHuaY |

## Recommended weekly sync (~150 search calls, under 10 minutes)
1. **git:** `git fetch` the treeless clones and recompute ownership incrementally.
2. **PRs and issues:** fetch by `updated:>=<last_sync>`, date-sliced, for both repos. Upsert by number.
3. **Opportunity filters:** good-first-issue, `-linked:pr`, stale `review:none`, approved-but-open, new bugs. About 15 calls per repo.
4. **Reviewer counts:** refresh monthly, `reviewed-by:` for about 45 logins.
5. **Roster:** re-pull the whimsy roster weekly.
6. **Sibling repos:** snapshot monthly.
7. **Client:** one rate-limited client, at least 2.2 s between calls, backing off on 403/429, with an on-disk cache.
- **Pitfalls:**
  - Dependabot inflates review counts.
  - `author_association` reflects the state at query time.
  - Title prefixes are inconsistent.
  - Git author names have variants, so join through the alias map.
