# Northwind Home Services brand guidelines

For anything Northwind puts in front of a customer, a board or our own team: dashboards, reports, proposals. One page. If something is not covered here, keep it plain and use Harbor Navy on Fog.

Northwind is a Portland, Maine company. The look is the working waterfront on a grey morning: navy hulls, fog, granite, sea glass on the tideline, and one orange buoy you notice because it is the only bright thing in the harbor.

## Palette

| Token | Hex | Role |
|---|---|---|
| Harbor Navy | `#1C2B3A` | All headings, body text, axis lines, the wordmark. The structure of the page. |
| Sea Glass | `#3F8F7F` | The single data color. The series or bar that matters. Nothing decorative is ever Sea Glass. |
| Buoy Orange | `#E2572B` | Alerts and flags only: a customer over 25%, a margin that fell, an exception. If nothing is wrong, there is no orange on the page. |
| Fog | `#F4F5F2` | Page background. |
| Paper | `#FFFFFF` | Card and table background. |
| Granite | `#5B6670` | Secondary text: labels, captions, axis text, footnotes. |
| Ledge | `#B9C0C6` | Every data series that is not the one that matters. |
| Mist | `#E3E6E8` | Card borders, table rules and gridlines. |

Area fills may use Sea Glass at 15% opacity. No other tints, no gradients.

## Type

| Use | Font | Fallback stack | Size and weight |
|---|---|---|---|
| H1 (page title) | Fraunces | Georgia, "Times New Roman", serif | 32px, 600 |
| H2 (section and chart headlines) | Fraunces | Georgia, "Times New Roman", serif | 20px, 600 |
| Body and notes | Source Sans 3 | -apple-system, "Segoe UI", Helvetica, Arial, sans-serif | 16px, 400, line height 1.6 |
| Labels (KPI names, axis titles, table headers) | Source Sans 3 | same as body | 12px, 600, uppercase, letter spacing 0.06em, Granite |
| Numbers (KPIs, table figures, chart labels) | IBM Plex Mono | ui-monospace, "SF Mono", Menlo, Consolas, monospace | KPI values 32px, 500. Table and chart numbers 13 to 14px, 400 |

The three fonts may be linked from Google Fonts:

```
https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600&family=Source+Sans+3:wght@400;600&family=IBM+Plex+Mono:wght@400;500&display=swap
```

Always include the fallback stack, so a file opened offline still reads correctly.

## Layout

- Left-aligned. Headlines, text and KPI values all start on the left edge. Nothing centered except a lone number inside a small card.
- 12-column grid, 24px gutters, max content width 1200px, 32px outer padding. The KPI row is 4 cards of 3 columns each.
- Generous whitespace: 48px between sections, 24px inside cards.
- Cards: Paper background, 1px Mist border, no shadow. Corner radius 2px, never more than 4px.
- No icons beside KPIs, no emoji, no background images.

## Charts

- One accent color. The series that carries the point is Sea Glass; everything else is Ledge.
- The flagged item (the customer over 25%, the month the margin broke) is Buoy Orange, and it is the only orange on the chart.
- Label lines and bars directly at their ends. Use a legend only when direct labels would overlap.
- No pie or donut charts. Shares are horizontal bars, sorted largest first.
- No gradients, no 3D, no drop shadows, no animation.
- Gridlines: horizontal only, 1px Mist. No chart border.
- Bar axes start at zero. Line charts may start above zero if the axis says so.
- Lines are 2px. Mark only the last point, with its value.
- Mix over time is a stacked bar per month in Sea Glass, Ledge and Granite, not a stacked area rainbow.

## Numbers

- Large money: `$2.78M`, `$862K`. Table money: `$1,184.60`, thousands separators always.
- Percentages to one decimal: `51.8%`, `31.0%`.
- Numbers right-aligned in tables, set in IBM Plex Mono with tabular figures (`font-variant-numeric: tabular-nums`) so columns line up.
- Months as `Sep 2026` on screen. Never show `2026-09` or a raw date to a reader.

## Headline voice

Every section and chart headline states the finding as a sentence. A reader who reads only the headlines should get the story.

- Yes: "Handyman margin fell from 63% to 45%"
- Yes: "Eastern Promenade is 31.0% of revenue"
- No: "Margin Trend", "Customer Concentration", "Revenue Overview"

Sentence case. No exclamation marks. No "Insights" or "Key Takeaways" labels.

## Wordmark

`NORTHWIND` in Fraunces 600, all caps, letter spacing 0.12em, Harbor Navy, with a small compass-rose glyph (a simple 4-point star, drawn in inline SVG, 18 to 20px, Harbor Navy) to its left. Under it, in Source Sans 3 12px Granite: "Home Services, Portland, Maine". No image files needed.

## Do / Don't

| Do | Don't |
|---|---|
| One Sea Glass series per chart, everything else Ledge | A different color for every customer or service line |
| Buoy Orange on the one thing that needs action | Orange as decoration, or red and green traffic lights |
| Headlines that state the finding | Headlines that name the chart type |
| 1px borders, square corners, flat Paper cards | Rounded cards with shadows, glass effects, gradients |
| Direct labels at the end of a line or bar | Legends in a box below the chart |
| Horizontal bars for shares | Pie or donut charts |
| A source line under each chart in Granite 12px | Unlabeled numbers with no file behind them |
