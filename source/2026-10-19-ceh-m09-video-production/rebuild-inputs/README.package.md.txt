# Rebuild the M09 source package

Python3.10+ with requirements-source.txt builds the source, evidence and editable deck. Node22+, Puppeteer/Chromium, LibreOffice and Poppler support actual browser/PDF QA. Original locked assets, local fonts and GSAP are bundled; no external voice provider is required for this layer.

Run build_source.py, build_evidence.py, build_companions.py and write_docs.py. The authored_scenes*.txt, authored_chapters.json and authored_questions.json are canonical authored inputs. write_references.py refreshes public-source retrieval metadata only when deliberately run with live access. verify_evidence.py is read-only unless --record is supplied.

Export the actual PPTX through LibreOffice in an isolated profile, rasterize its PDF and run browser_qa.cjs with PUPPETEER_PATH and CHROMIUM_PATH. Inspect all 58boards/18slides/four references and record concrete findings. Run all four HyperFrames checks. Run validate_pack.py and build_release.py only after required QA. Rebuilding invalidates older manifests/QA until verified again. Manifest/self-hash exclusions avoid circular digests. Only actual results establish the named layer.
