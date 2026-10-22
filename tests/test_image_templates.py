"""Check browser-parsed attributes in both preview and production HTML."""
from html.parser import HTMLParser
from pathlib import Path
import os
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://img.imych.one/now/20261025/20260821-SFO-SantaCruz.jpeg"


class Images(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.images = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            self.images.append(dict(attrs))


class ImageTemplatesTest(unittest.TestCase):
    def test_urls_and_attribute_quotes(self):
        with tempfile.TemporaryDirectory() as directory:
            tmp = Path(directory)
            content = tmp / "content" / "fixture"
            content.mkdir(parents=True)
            (content / "index.md").write_text('''---
title: Image regression
url: /fixture/
---
![Santa Cruz](r2:now/20261025/20260821-SFO-SantaCruz.jpeg)

{{< figure src="r2:now/20261025/20260821-SFO-SantaCruz.jpeg" alt="Santa Cruz" loading="eager" >}}

![Chinese](<r2:旅行/海邊 照片.jpeg?a=1&b=2> "A &quot;quoted&quot; title")
''', encoding="utf-8")
            for minify in (False, True):
                with self.subTest(minify=minify):
                    output = tmp / ("minified" if minify else "plain")
                    command = [
                        "hugo", "--gc", "--cleanDestinationDir", "--noBuildLock",
                        "--source", str(ROOT), "--contentDir", str(tmp / "content"),
                        "--destination", str(output), "--cacheDir", str(tmp / "cache"),
                    ]
                    if minify:
                        command.append("--minify")
                    subprocess.run(command, check=True, capture_output=True, text=True,
                                   env={**os.environ, "HUGO_RESOURCEDIR": str(tmp / "resources")})
                    images = Images((output / "fixture/index.html").read_text()).images
                    self.assertEqual(len(images), 3)
                    for image in images[:2]:
                        self.assertEqual(image["src"],
                            "https://img.imych.one/cdn-cgi/image/"
                            "width=1920,quality=75,fit=scale-down,format=auto/" + SOURCE)
                        candidates = image["srcset"].split(", ")
                        self.assertEqual(len(candidates), 4)
                        for candidate, width in zip(candidates, (640, 960, 1280, 1920)):
                            url, descriptor = candidate.rsplit(" ", 1)
                            self.assertTrue(url.startswith("https://img.imych.one/"))
                            self.assertIn(f"width={width},quality=75,", url)
                            self.assertNotIn('"', url)
                            self.assertEqual(descriptor, f"{width}w")
                        self.assertIn("calc(100vw - 28px)", image["sizes"])
                    self.assertEqual(images[0]["loading"], "lazy")
                    self.assertEqual(images[1]["loading"], "eager")
                    self.assertEqual(images[2]["title"], 'A "quoted" title')
                    self.assertIn("%20", images[2]["src"])
                    self.assertTrue(images[2]["src"].endswith("?a=1&b=2"))


if __name__ == "__main__":
    unittest.main()
