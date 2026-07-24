def detect_event_conflicts(events):

    """
    Detect overlapping events.

    Time Complexity:
    O(n log n)

    Space Complexity:
    O(1)
    """

    if len(events) <= 1:
        return []


    events = sorted(
        events,
        key=lambda event: (
            event.event_date,
            event.start_time
        )
    )


    conflicts = []


    for i in range(len(events) - 1):

        current_event = events[i]

        next_event = events[i + 1]


        if current_event.event_date == next_event.event_date:

            if current_event.end_time > next_event.start_time:

                conflicts.append({

                    "event_1": current_event.title,

                    "event_2": next_event.title,

                    "date": str(
                        current_event.event_date
                    ),

                    "message":
                    "Schedule Conflict Detected"

                })


    return conflicts

