# "Untestable" is always a cost/benefit claim in disguise

There is no such thing as an untestable tool. There is only *not worth
testing*, which is a cost/benefit judgment, which requires estimating both
sides. Calling something untestable skips the estimate and hides the
judgment behind a property the code doesn't have.

The practical consequence: **the set of things worth testing is a function
of the incremental cost of testing**, and that cost is not fixed. It is
mostly fixed *cost of the first test in a new place*: a project to put the
code in, a runner, a CI hook, an import path. `bukzor-tools` already paid
that. Inside it, one more doctest costs approximately nothing, which moves
the line far enough that even teeny things land on the testable side.

So the question is never "is this testable" but:

- what is the incremental cost of a test *here*, given what already exists
- what does the test buy -- and for cheap tools the answer is usually not
  "catches bugs" but "pins a fact that drifts upstream"

That second point is what makes tiny scripts worth packaging. A 12-line
script that encodes a reverse-engineered upstream behavior carries more
test-value per line than a 200-line script that only sequences commands,
because upstream can change the behavior silently.

## Counter-pressure

Reducing incremental cost to near zero is imaginable but not currently the
case: a new package still costs a `pyproject.toml`, a meta-package wiring,
a README row, and lockfile churn. Estimate that as real, and don't let
"the cost is near zero" become the reason a fourth micro-package appears
where one shared leaf would do.
