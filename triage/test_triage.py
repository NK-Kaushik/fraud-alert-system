from risk_prioritizer import assign_priority

samples = [
    (0.92, 1200, False, False),
    (0.65, 800, True, False),
    (0.40, 50, False, False),
]

for s in samples:
    print(assign_priority(*s))
