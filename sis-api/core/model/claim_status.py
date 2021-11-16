from enum import IntEnum


class ClaimStatus(IntEnum):
    Rejected = -1
    Resolved = 0
    Submitted = 1
    UnderReview = 2
    EvidenceRequested = 3
    AwaitingCustomerApproval = 4
    Accepted = 5
    Processing = 6
