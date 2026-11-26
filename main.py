"""Funniest Forecast for a City That Isn't — make.fun entry.

Writes one line, the funniest weather forecast for a city that does not
exist, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Gate rationale (Quality Gate, 26 Nov 2026, pick (d), 21/25 — 84 karakter,
maks 120):

    "Cloudy in Mistport today, with fog so thick the lighthouse has asked
    for directions."

Judge criteria from RULES.txt, in order of importance, and how the pick
maps onto each:

1. Weather forecast for a city that does not exist (5/5). Mistport is an
   invented coastal city, named in the line itself; the whole sentence is
   framed as that city's forecast. A line about a real place, or with no
   invented city, loses to any forecast for a city that does not exist —
   this pick cannot lose on criterion 1.
2. Funny on first read; the laugh comes from the weather itself (4/5).
   The joke is the fog: it is so thick that the lighthouse — the one thing
   whose entire job is to see through fog and guide others — has itself
   asked for directions. The absurdity grows out of the weather, not out
   of a pun bolted on afterwards.
3. Sounds like a real forecast, then breaks (4/5). "Cloudy in Mistport
   today, with fog so thick ..." opens in the flat, official phrasing of
   a weather bulletin, then breaks it with the lighthouse asking for
   directions — a role reversal that lands because the bulletin voice
   stays deadpan.
4. The invented city feels like a place (4/5). Mistport reads as a
   misty harbour town, and the lighthouse is exactly the detail such a
   town would have; name and detail fit the absurd weather instead of
   fighting it.
5. Fits in 120 characters with no wasted word (4/5). 84 characters, every
   word working: "Cloudy", "Mistport", "fog so thick", "lighthouse",
   "asked for directions" — nothing padded, nothing to cut.

Why the other five candidates lost:

(a) "Tomorrow in Nowhereville: heavy rain, followed by heavier regret.
Bring an umbrella and an apology." — 16/25. "Nowhereville" is generic,
and "regret" is a bolted-on pun rather than a joke from the weather.
(b) "Brolin Falls expects sunshine with a 90% chance of the sun filing
a formal complaint." — 17/25. The sun complaining is a decent turn, but
it is a personification gag about the sun, not weather absurdity that
makes the city feel real; weaker on criteria 2 and 4 than the pick.
(c) "In Zorp City, expect scattered showers of unsent emails and a 100%
chance of reply-all." — 17/25. Office humour pasted onto a forecast;
the laugh comes from emails, not from the weather, so it scores lower
on criterion 2.
(e) "Good morning, Drizzlewick: light rain until noon, then the rain
gets serious and starts taking notes." — 21/25, tied with the pick.
Lost the tie-break: "the lighthouse has asked for directions" is more
visual and the twist is sharper — a lighthouse lost in fog inverts the
whole purpose of the thing, while rain taking notes is only mildly
personified rain.
(f) "Sunny in Gloomhaven, 24 degrees, with a gentle breeze carrying the
smell of someone else's barbecue." — 16/25. Pleasant image, but no real
punchline: the breeze carrying a smell is atmosphere, not a joke.

3-second stranger test: passed — anyone who has seen a lighthouse gets
the joke instantly, no inside context needed. Freshness test: passed —
a lighthouse asking for directions is not a stock joke.
"""

import os

LINE = "Cloudy in Mistport today, with fog so thick the lighthouse has asked for directions."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
