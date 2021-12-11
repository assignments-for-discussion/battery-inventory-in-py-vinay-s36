
def countBatteriesByUsage(cycles):
  return {
    "lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
  }


def testBucketingByNumberOfCycles():
  print("Counting batteries by usage cycles...\n");
  counts = countBatteriesByUsage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 1)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 2)
  print("Done counting :)")


if __name__ == '__main__':
  testBucketingByNumberOfCycles()
