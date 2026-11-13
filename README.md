# progressbar-demo

A tiny `ttk.Progressbar` tour — the second widget the [cleanroom coverage audit](https://github.com/amanvicky/cleanroom) named as its top blocker (6 of the 20 most-starred tkinter repos use it) and shipped as a real widget.

Three bars, one behavior each:

- **stepped by hand** — `step()` adds 1; at `maximum` the value wraps (`value % maximum`) and keeps cycling, the rule measured against real Tk 9.0 rather than folklore;
- **driven by `start(120)`** — the widget schedules its own `step()` timer through `after()`, `stop()` cancels it, calling `start()` twice does not double-schedule;
- **indeterminate** — the stored value climbs without bound while the bar just bounces; `stop()` stops the bounce.

Runs as-is in [cleanroom](https://amanvicky.github.io/cleanroom/) (open the shelf and pick **progressbar-demo** — the virtual tkinter renders all three bars live) and on a real PC:

```
python progress_demo.py     # needs Tk — ships with the standard Python installer
```
