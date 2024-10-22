def count_batteries_by_health(present_capacities):
    rated_capacity = 120
    battery_health_counts = {
    "healthy": 0,
    "exchange": 0,
    "failed": 0
    }
    
    for capacity in present_capacities:
        soh = 100 * capacity / rated_capacity
        if soh > 83:
            battery_health_counts["healthy"] += 1 #classified as  healthy if SoH > 83
        elif 63 < soh <= 83:
            battery_health_counts["exchange"] += 1 #classified as exchange if SoH is between 63% and 83% 
        else:
            battery_health_counts["failed"] += 1 #classified as failed if SoH is below 63%
    
    return battery_health_counts

def test_bucketing_by_health():
    print("Counting batteries by SoH...\n")
    present_capacities = [113, 116, 80, 95, 92, 70]
    counts = count_batteries_by_health(present_capacities)
    assert(counts["healthy"] == 2)
    assert(counts["exchange"] == 3)
    assert(counts["failed"] == 1)
    
    # additional cases
    assert(count_batteries_by_health([120]) == {"healthy": 1, "exchange": 0, "failed": 0})
    assert(count_batteries_by_health([60]) == {"healthy": 0, "exchange": 0, "failed": 1})
    assert(count_batteries_by_health([80, 81]) == {"healthy": 0, "exchange": 2, "failed": 0})
    
    print("Done counting :)")


if __name__ == '__main__':
    test_bucketing_by_health()
