# Iceberg working-group notes docs: research index (2026-11-13)

raw/*.md = Drive text export (read_file_content .fileContent) of the large docs.
Small docs (spark, vector, read-restrictions, constraints) were read inline; refetch with read_file_content (they fit under the tool limit).

| key | doc id | title | type | sizeBytes | modifiedTime | last meeting | cadence |
|---|---|---|---|---|---|---|---|
| community | 1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg | Iceberg community syncs | notes (2 tabs) | 1,206,364 | 2026-10-30 | 2026-10-28 | 3-weekly Wed |
| catalog | 1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw | Iceberg Catalog Community Sync Notes | notes | 70,895 | 2026-11-05 | 2026-11-04 | 3-weekly Wed |
| mv | 1UnhldHhe3Grz8JBngwXPA6ZZord1xMedY5ukEhZYF-A | Iceberg Materialized View Spec | both (Agenda tab + spec tab) | 351,449 | 2026-11-12 | 2026-11-12 | ~biweekly Thu, irregular |
| index | 1N6a2IOzC6Qsqv7NBqHKesees4N6WF49YUSIX2FrF7S0 | Iceberg secondary indexes | both (Design + Meeting notes tabs) | 267,922 | 2026-11-12 | 2026-11-09 | biweekly Mon |
| vector | 1zA8PskNDFKXXJpzWQr25CFoX_aIZHBNHbkxk0t3PteE | Iceberg Vector Type Support Proposal | both (Design + Sync notes tabs) | 82,591 | 2026-11-12 | 2026-11-05 (+ agenda for 2026-11-19) | biweekly Thu |
| v4sfc | 1k4x8utgh41Sn1tr98eynDKCWq035SV_f75rtNHcerVw | Iceberg Single File Commits | both, ~11 tabs, mostly design | 8,126,880 | 2026-11-10 | 2026-11-02 | biweekly Mon |
| variant | 1IuhLRxw1rcPD_f4jgHuGe3SwFgy7Y5wgEGvLzf6311s | Iceberg - Variant Community Update | status tracker + Meeting Notes tab | 144,553 | 2026-11-05 | 2026-09-03 | monthly 1st Thu (Oct/Nov not recorded) |
| spark | 19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4 | Iceberg - Spark Community Sync Notes | notes | 88,066 | 2026-11-11 | 2026-10-20 held; "Nov 11, 2026" = prepared agenda (3rd Tue = Nov 17) | monthly 3rd Tue |
| readrestr | 1iGNydKY7XT1N5Nz056vDPM0P8v0MFymGqNtOlUGUp-c | Iceberg Read Restrictions: Community Syncs | notes | 30,197 | 2026-10-06 | 2026-09-15 | biweekly Tue (dormant? "Do we need sync?") |
| constraints | 1re65fx3uqC7I_tJuS79IxLiB7HEN2Grt5qRIDjd3p-4 | Constraint Support in Iceberg | design + stub notes | 71,802 | 2026-10-10 | 2026-06-18 | dormant (2 entries) |
| colupdates | 1Bd7JVzgajA8-DozzeEE24mID_GLuz6iwj0g4TlcVJcs | Efficient Column Updates in Iceberg | both (design + Meeting Notes + Status tabs) | 2,785,666 | 2026-11-11 | 2026-10-20 | biweekly Tue |
| python | 1oMKodaZJrOJjPfc8PDVAoTdl02eGQKHlhwuggiw7s9U | Iceberg python library syncs | notes (NOT in calendar list) | 336,976 | 2026-10-27 | 10/27/2026 (agenda only) | monthly last Tue |

Other docs found via Drive search (not in list): Polaris Community Sync Notes (1TAAMjCtk4KuWSwfxpCBhhK9vM1k_3n7YE4L28slclXU, mod 2026-11-12),
Apache Arrow community meeting notes (1xrji8fc6_24TVmKiHJB4ECX1Zy2sy2eRbBjpVJMnPmk, mod 2026-11-04), PyArrow dev community meeting notes
(1ioiJdEYf5mJwQ-rOjzjPYCeHTjOhAPo5ppUHy6iBrxU, mod 2026-10-30), Iceberg Proposal - Collation Support (1m8b7u97uteHYjXk-4DNglJSpQO8OcZOCzW2tApCNTW4, design, mod 2026-10-30).
No Rust/Go/C++ sync docs found. Drive search did NOT return vector/index/spark/constraints/readrestr docs even though readable -> search is not a complete discovery mechanism.
