# Input formats for `plan_project.py`

## Network (`plan`, `track`)

```json
{
  "project": "Clinic Scheduling",
  "time_unit": "days",
  "cost_per_unit": 800,
  "core_team": 2,
  "developers": 5,
  "float_thresholds": [10, 30],
  "activities": [
    {"id": "REQ", "name": "Requirements", "duration": 15, "role": "core"},
    {"id": "DB",  "name": "Database",     "duration": 10, "depends_on": ["PD"]},
    {"id": "REL", "name": "Release",      "duration": 0,  "depends_on": ["SYS"]}
  ]
}
```

| Field | Required | Meaning |
|---|---|---|
| `project` | no | Title used in the reports |
| `time_unit` | no | Label only (`days`, `weeks`). Every duration uses this unit |
| `cost_per_unit` | no | Cost of one person for one time unit. Turns on the cost charts |
| `core_team` | no | People present for the whole project (architect, PM). Counted in staffing and cost every period |
| `developers` | no | Cap on concurrent `developer`-role staff. `--developers` on the command line overrides it. Leave it out to staff every activity as early as possible |
| `float_thresholds` | no | `[low, medium]` upper bounds for the red and yellow float bands. Default: 10% and 30% of the critical-path length |
| `activities[].id` | yes | Short unique id |
| `activities[].name` | no | Display name |
| `activities[].duration` | yes | Nominal estimate. Use 0 for milestones |
| `activities[].depends_on` | no | Ids of predecessors |
| `activities[].staff` | no | People on the activity at once. Default 1 (0 for milestones). Keep it at 1 for services |
| `activities[].role` | no | `developer` (default): drawn from the capped pool. `core`: done by the core team, earns value, adds no staffing. Anything else (`tester`, `ux`, ...): adds staffing, uncapped |

Earned-value weight of an activity = `duration × staff` ÷ the sum over all activities.

## Status (`track`)

```json
{
  "tolerance": 0.05,
  "reports": [
    {"time": 40, "completed": ["REQ", "ARCH", "PD"], "effort_to_date": 95},
    {"time": 60, "completed": ["REQ", "ARCH", "PD", "DB"],
     "partial": {"PRA": 0.5}, "effort_to_date": 205}
  ]
}
```

| Field | Meaning |
|---|---|
| `tolerance` | How far from plan (as a fraction) still counts as "on plan". Default 0.05 |
| `reports[].time` | Elapsed time units since project start |
| `reports[].completed` | Activities whose exit criteria are met. Binary: met or not |
| `reports[].partial` | Optional credit for an in-progress activity, as the summed weight of its completed lifecycle phases (e.g. design review passed = 0.3) |
| `reports[].effort_to_date` | Total person-units actually spent so far, core team included |

The diagnosis uses the latest report. The projected finish is a linear fit through the last
three progress points.
