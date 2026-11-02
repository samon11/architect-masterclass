# Factoring walkthrough: point-of-sale peripherals

The course's sample project. A point-of-sale system talks to a barcode scanner. The first
contract is the obvious one:

```csharp
interface IScannerAccess
{
    void ScanCode();
    void AdjustBeam();
    void OpenPort();
    void ClosePort();
}
```

Four operations, right in the 3–5 target range. **It's still a bad contract.**

## Step 1: a numeric keypad arrives (factor down)
A keypad also reads codes, but `AdjustBeam` makes no sense for it. `AdjustBeam` is the
**offending operation**: right in some contexts, miserable in others. Push it down into a derived contract:

```csharp
interface IReader          { void ReadCode(); void OpenPort(); void ClosePort(); }
interface IScannerAccess : IReader { void AdjustBeam(); }
interface IKeypadAccess  : IReader { }
```

## Step 2: a conveyor belt arrives (factor sideways)
The belt also needs `OpenPort`/`ClosePort` but has nothing to read. `ReadCode` and the port
operations are only **weakly related**, so split them into independent facets:

```csharp
interface ICommunicationDevice { void OpenPort(); void ClosePort(); }
interface IReader              { void ReadCode(); }
interface IScannerAccess : IReader { void AdjustBeam(); }

class BarcodeScanner : IScannerAccess, ICommunicationDevice { }
class ConveyorBelt   : IBeltAccess,    ICommunicationDevice { }
```

The work inside `BarcodeScanner` is unchanged. But `ICommunicationDevice` can now be reused.

## Step 3: shared operations repeat (factor up)
If several facets (`IScannerAccess`, `IBeltAccess`, ...) each repeat the same logically
related operations, hoist them into a common base. Leaving them out would make each contract
less cohesive. Duplicating them makes bad contracts.

## Step 4: check the metrics
`IReader` now has one operation, which is a red flag. Is it speculative? A near-duplicate of
something else? Ask what else belongs with reading a code. If nothing does, merge it back
with its kinsmen.

## The lesson
- The three techniques only ever make contracts smaller. Metrics are the brake.
- The metrics didn't catch the original `IScannerAccess`, and only the attribute questions
  did. Meeting the metrics proves nothing. Violating them proves something is wrong.
- Every new peripheral used to force a change to existing contracts. After factoring, a new
  peripheral only **implements** existing contracts. That's what resilience to changes in the
  user domain looks like.
