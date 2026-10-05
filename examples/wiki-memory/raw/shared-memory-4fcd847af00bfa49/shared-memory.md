# Shared agent memory

## Recommendation

For a service used by many customers, expose durable memory through a governed
server interface. Central access checks let multiple clients share business
logic without distributing that logic to every machine.

## Limitation

A server requires operating infrastructure. A small personal collection may
not justify that cost. The correct memory architecture depends on its users
and deployment context, rather than one universal storage recommendation.
