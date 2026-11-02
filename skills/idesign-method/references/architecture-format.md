# Architecture JSON for `validate_architecture.py`

```json
{
  "system": "Clinic Scheduling",
  "components": [
    {"name": "PatientPortal", "layer": "client"},
    {"name": "AppointmentsManager", "layer": "manager",
     "volatility": "Booking workflow differs per clinic and payer"},
    {"name": "SchedulesAccess", "layer": "resourceaccess",
     "operations": ["Reserve", "Release", "Confirm"]},
    {"name": "ClinicDB", "layer": "resource"},
    {"name": "PubSub", "layer": "utility"}
  ],
  "use_cases": [
    {"name": "Book appointment", "calls": [
      {"from": "PatientPortal", "to": "AppointmentsManager"},
      {"from": "AppointmentsManager", "to": "SchedulesAccess"},
      {"from": "SchedulesAccess", "to": "ClinicDB"},
      {"from": "AppointmentsManager", "to": "PubSub", "type": "publish"}
    ]}
  ]
}
```

| Field | Meaning |
|---|---|
| `components[].name` | Unique name |
| `components[].layer` | `client`, `manager`, `engine`, `resourceaccess` (or `ra`), `resource`, `utility` |
| `components[].volatility` | Optional. The volatility it encapsulates. Engines, managers and RA get a note when it's missing |
| `components[].operations` | Optional. For RA, checked for CRUD/I/O verbs |
| `use_cases[].name` | Core use case name |
| `use_cases[].calls[]` | `from`, `to`, `type`. Types: `sync` (default, solid line), `queued` (dashed), `async` (discouraged), `publish` (manager → pub/sub utility) |

Call chains are unordered, like the Method's call-chain diagrams. Use a sequence diagram in
detailed design when order matters.

Exit code: 0 when there are no errors, 1 when there are errors.
