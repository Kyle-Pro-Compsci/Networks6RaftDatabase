The high-level design of this was to have three methods that would never return. They represent one of running as a follower, running as a candidate, or running as a leader. The idea was they would either loop indefinitely, like if you were in 'run_as_leader', or hit a condition that would call one of the other two methods for when the replica shifted its state (say going from a candidate to a leader).

This was eventually changed slightly as I was worried this 'recursive' nesting would use up an indefinite amount of memory as the compiler would store the local scopes as each method was called. I decided to change it to a return call.

I used a custom class called LogEntry (seen in replica_util) to store the information needed in each log, relying on MID as a unique identifier.

My biggest issue once I learned Raft was working around the sockets and getting to fully understand the select() call, which I originally had outside the loop. Documentation for this is quite insufficient. The other issue is, quite obviously, a lack of time. I'm working solo and have 2 other coding classes, including Software Development, so despite the generous amount of time given for this final project I still didn't finish it.

The code is quite untested, unoptimized, and missing the ability to repair logs.