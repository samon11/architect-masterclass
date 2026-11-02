# Input formats for `contract_metrics.py`

## Contract spec (JSON)

```json
{
  "services": [
    {"name": "SchedulesAccess", "layer": "resourceaccess",
     "contracts": ["ISchedulesAccess", "IDiagnostics"]}
  ],
  "contracts": [
    {"name": "ISchedulesAccess",
     "bases": [],
     "properties": [],
     "operations": [
       {"name": "Reserve", "params": [{"name": "slotId", "type": "string"}]},
       {"name": "Register", "params": [{"name": "patient", "type": "PatientRecord", "fields": 4}]}
     ]}
  ]
}
```

| Field | Meaning |
|---|---|
| `services[].layer` | Optional: `client`, `manager`, `engine`, `resourceaccess`, `utility`. ResourceAccess contracts get the atomic-verb check (so does any contract whose name ends in `Access`) |
| `services[].contracts` | Contracts the service implements. Used for contracts per service and reuse |
| `contracts[].bases` | Contracts this one derives from (factor up / down) |
| `contracts[].properties` | Property names exposed on the contract (each one is an error) |
| `params[].fields` | For a data-contract parameter, its number of fields. Counted as that many arguments |

## History (for the sorting method)

```json
{
  "weights": {"complexity": 1, "defects": 2, "implementation_days": 1, "changes": 2, "reuse": 2},
  "contracts": {
    "ISchedulesAccess": {"complexity": 6, "defects": 1, "implementation_days": 5, "changes": 2, "reuse": 3}
  }
}
```

All fields are optional. `reuse` defaults to the number of services that implement the
contract. Each measure is normalized to its maximum across contracts. Higher complexity,
defects, time and changes count as worse; higher reuse counts as better. The weighted
average gives a badness score from 0 (best) to 1 (worst).

## Source mode

`--source` accepts files or directories containing `.cs`, `.java`, `.ts` or `.tsx` files
(it skips `node_modules`, `bin`, `obj`, `dist`, `build`, `target`). It finds:
- interfaces with their operations and properties,
- classes, records, structs and TS `type` literals, with field counts used to weight parameters,
- `class X : IA, IB` / `implements IA, IB`, which become services.

It's a heuristic, not a compiler. Check `metrics.json` → `parsed` when the numbers look off.
