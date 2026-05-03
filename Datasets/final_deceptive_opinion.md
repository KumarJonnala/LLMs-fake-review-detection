# Final Deceptive Opinion Dataset Information

This document provides administrative and statistical details for the `final_deceptive_opinion.csv` dataset.

## Dataset Overview
- **File Path**: [fake_reviews_prediction/Old_dataset/final_deceptive_opinion.csv](fake_reviews_prediction/Old_dataset/final_deceptive_opinion.csv)
- **Total Samples**: 2396
- **Total Columns**: 4
- **Unique Hotels Involved**: 20

## Column Definitions
| Column | Description |
| :--- | :--- |
| `label` | Classification of the review (truthful, deceptive, CG, OR) |
| `hotel` | The name of the hotel being reviewed |
| `source` | The platform or method used to obtain the review |
| `text` | The full content of the review |

## Data Distribution

### Label Distribution
- **truthful**: 796
- **deceptive**: 800
- **CG** (Computer Generated): 400
- **OR**: 400

### Source Distribution
- **MTurk**: 800
- **amazon**: 800
- **TripAdvisor**: 400
- **Web**: 400

## Summary
This dataset is primarily used for fake review detection and analysis, combining human-written (truthful/deceptive) and potentially machine-generated or web-scraped content across a variety of platforms and hotels.
