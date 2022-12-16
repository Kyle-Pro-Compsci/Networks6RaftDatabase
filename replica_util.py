class Status:
    FOLLOWER = 1
    CANDIDATE = 2
    LEADER = 3

# All must have: [src, dst, type, leader]
class MessageType:
    PUT = 'put'
    GET = 'get'
    REQUEST_VOTE = 'request_vote'  # [latest_term, latest_index]
    VOTE_GRANTED = 'vote_granted'
    REDIRECT = 'redirect'
    APPEND_ENTRIES = 'append_entries'  # [latest_term, latest_index, last_term,, last_index
    READY_TO_COMMIT = 'ready_to_commit'
    OK = 'ok'
    FAIL = 'fail'


class Timeout:
    ELECTION_TIMEOUT_MIN = 150 # Timeout for a follower to start an election
    ELECTION_TIMEOUT_LENGTH = 150
    HEARTBEAT = 100


# Updated for puts
class LogEntry:
    def __init__(self, term, index, mid, key, value):
        self.term = term
        self.index = index
        self.mid = mid
        self.key = key
        self.value = value
