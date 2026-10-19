# M10 auxiliary animation-map review

The actual 4283.733333333-second composition produced 24,624 enumerated tweens and 4,191 mapped entries with two samples and a 0.7-second minimum. Matching producer/core 0.8.173 analysis packages ran separately from the pinned production renderer. The raw map remains in full-animation-map/animation-map.json.

The helper reports 3,249 collision, 243 paced-slow and 21 degenerate entries. There are no offscreen or invisible category flags. Its collision routine compares nearby sampled bounding boxes without checking visibility or ancestor clip activity; 948 flagged entries have all samples hidden. Tally rig parts and note border/marker/text also intentionally overlap.

All 21 degenerate entries occur before their owning scene begins and have hidden zero-width samples. Each has visible, nonzero counterparts for the same selector elsewhere in the actual map. animation-map-context.json records every selector, flagged time, scene start and counterpart count. Native chapter frames already show these completed gauges; final encoded late samples check the delivered picture separately.

The 243 paced-slow entries consist of 219 finite 2.4-second target moves and 24 clock drivers. The rule flags durations above two seconds without judging purpose. The 227 dead-zone advisories mark gaps in the mapped motion list; narration and reading holds retain completed diagrams intentionally. Child/proxy timeline duplication is consistent with repeated selectors and early local-time entries; it is not evidence of simultaneous visible duplicates.

All findings remain preserved. Actual active-window full-project checks have zero lint/runtime/layout/contrast errors and warnings. All 58 scenes passed 174 repeated/backward seeks; quiz boundaries passed 64 assertions. Native visual review, final encoded samples and full human viewing/listening remain separately recorded layers.
