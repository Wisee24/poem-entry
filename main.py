from pathlib import Path


POEM = """At Dad's bedside,
I started the song he taught me.
You turned it down.
His thumb tapped time against the sheet.
I stopped singing.
You kept it playing.
He finished the chorus."""

Path("/output/entry.txt").write_bytes(POEM.encode("utf-8"))
