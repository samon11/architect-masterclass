# IDesign Method rules

## Call rules (closed architecture)

| Caller → Callee | Sync | Queued | Rationale |
|---|---|---|---|
| Client → Manager | ✅ (one manager per use case) | ✅ | Single point of entry. Stitching managers moves business logic into the client |
| Client → Engine / RA / Resource | ❌ | ❌ | Skips layers. Business logic leaks into the client |
| Manager → Engine | ✅ | ❌ | An engine is an activity inside the manager's use case |
| Manager → RA | ✅ | ❌ | A queued "get me data" means nothing on its own |
| Manager → Manager | ❌ | ✅ (one) | Sync makes the callee an activity of the caller. Queued = deferred, unrelated use case. More than one → publish |
| Engine → RA | ✅ | ❌ | Engines sit on an orthogonal plane and may access resources |
| Engine → Engine | ❌ | ❌ | Not atomic. Everything about the activity belongs inside it |
| RA → Resource | ✅ | — | RA translates atomic business verbs into I/O |
| RA → RA | ❌ | ❌ | No longer atomic |
| Engine / Manager → Resource | ❌ | ❌ | Go through RA, or a schema change breaks business logic |
| Anything → Utility | ✅ | ✅ | Utilities are a vertical bar |
| Utility → business component | ❌ | ❌ | Fails the cappuccino-machine test |
| Any lower layer → higher layer | ❌ | ❌ | Calling up imports volatility: "when the client changes, the database detonates" |

## Events
- **Only managers publish.** A manager knows that a state change matters. Engines, RA,
  clients and resources don't (no DB triggers publishing).
- **Engines never subscribe.** Handling an event starts a use case, and only managers run use cases.
- Replace a manager → client callback with a published event.

## Naming
- Managers and ResourceAccess are **nouns**: `AccountManager`, `AccountAccess`.
  `BillingManager` and `TransferringManager` read as verbs, which is functional decomposition
  wearing the Method's names.
- Engines name an **activity**: `PricingEngine`, `RoutingEngine`.
- RA operations are **atomic business verbs**: `Credit`, `Debit`, `Reserve`. Never
  `Select`, `Insert`, `Read`, `Write`.

## Who / what / how / where
Clients = who. Managers = what. Engines = how (an activity). RA = how (a resource is accessed).
Resources = where. A manager with any "how" in it is suspect.

## Counts
- Managers : engines follow roughly Fibonacci (1:0, 2:1, 3:2, 5:3).
- 5 managers is a stretch. 8 means it has already failed, so make it a system of systems.
- A composable design has on the order of 10 services.
- Engines are the most abused part. Something that's variable isn't necessarily volatile.

## Call-chain shapes and smells

| Shape | Meaning |
|---|---|
| Stick figure | Proper design |
| Fork (client fans out) | Functional decomposition. The client stitches |
| Staircase (A → B → C) | Functional decomposition. "The staircase to hell" |
| Glove (manager ping-pongs tiny engines and RA) | Engines too small. Let them do their own resource access |
| Double-back (same engine first and last) | Commingled use cases, or broken state management |
| Asymmetry between use cases | Red flag: confirm it's intended |

## Ripeness checks
1. Volatility decreases from the top layer down.
2. Reuse increases from the top layer down.
3. Managers are almost expendable: changing a use case means changing the manager, cheaply.

## Volatility triage
- Horizon test: compare how often it has historically changed with the system's lifespan.
- Arch-competitor test: every reason a competitor couldn't use your system is a candidate volatility.
- Never encapsulate the nature of the business (house → skyscraper).
- Speculative design has two telltale signs: the change is possible but extremely rare, and
  you always end up doing a poor job of it.
