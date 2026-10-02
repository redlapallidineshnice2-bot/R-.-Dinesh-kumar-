import numpy as np # type: ignore

class PAICalculator:
    def __init__(self):
        # Reference thresholds from the research paper Table I
        self.thresholds = {
            "steps": 10000,
            "floors": 8,
            "intensity_minutes_week": 450, 
            "pal": 1.85,
            "active_minutes": 120
        }
        self.weight = 0.2  # wi = 1/N (where N=5 parameters)

    def calculate_partial_percentage(self, value, threshold):
        """Calculates pi: partial percentage of activity."""
        if value is None:
            return 0.0
        if value >= threshold:
            return 1.0
        return value / threshold

    def compute_daily_pai(self, daily_data):
        """
        daily_data: dict containing activity metrics
        """
        p1 = self.calculate_partial_percentage(daily_data.get('steps', 0), self.thresholds['steps'])
        p2 = self.calculate_partial_percentage(daily_data.get('floors', 0), self.thresholds['floors'])
        p3 = self.calculate_partial_percentage(daily_data.get('intensity_mins_weekly_avg', 0), self.thresholds['intensity_minutes_week'])
        p4 = self.calculate_partial_percentage(daily_data.get('pal', 0), self.thresholds['pal'])
        p5 = self.calculate_partial_percentage(daily_data.get('active_mins', 0), self.thresholds['active_minutes'])

        # Formula from Paper: PAI = sum(wi * pi)
        pai = self.weight * (p1 + p2 + p3 + p4 + p5)
        return round(pai * 100, 2)