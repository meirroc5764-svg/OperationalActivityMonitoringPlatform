class Anomaly:
    def __init__(
        self,
        event_id,
        source_id,
        timestamp,
        value,
        mean,
        standard_deviation,
        z_score,
        severity,
        detected_at
    ):
        self.event_id = event_id
        self.source_id = source_id
        self.timestamp = timestamp
        self.value = value
        self.mean = mean
        self.standard_deviation = standard_deviation
        self.z_score = z_score
        self.severity = severity
        self.detected_at = detected_at