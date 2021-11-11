bh-clean.tsv : browser history visits

columns
-------
sql_id : Autoincrement variable
hv_id : A combination of `id` and `visitId`
id : The unique identifier for the history.HistoryItem associated with this visit.
visitId : The unique identifier for this visit.
url : The URL of the page.
visitTime : When this visit occurred, represented in milliseconds since the epoch.
referringVisitId : The visit ID of the referrer.
transition : Describes how the browser navigated to the page on this occasion.
user_id : A unique user ID.
worker_id : Extension worker ID.
timestamp : Extension timestamp.
version : Extension version.
source : User source (inferred from user ID).
time_diff : Time spent on last visit
seq_dupe : Whether this URL is the same as the previously visited one (a sequential duplicate)
session : An integer indicating which user session this visit occurred in (sessions are split on a 30min delimeter)
session_idx : An integer indicating the order of visits within a session
time_elapsed : Time spent on this visit
domain : the web domain parsed from the URL
date : the date this visit occurred


survey.csv: main column you want is `psid` which links to `user_id` in browser history file
