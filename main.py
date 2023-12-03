#updated code
def count_batteries_by_health(present_capacities):

#initialize basic information of variable for number of battries available
    battery_information = { "healthy": 0, "exchange": 0, "failed": 0 }

#initialize the total capcity i.e, 120Ah    
    total_capacity=120


    for i in range(len(present_capacities)):

#calculate SoH of each battery
        SoH = 100*(present_capacities[i])/total_capacity

#categorise them into 3 sections depending 
        if SoH > 80 and SoH<=100:
           battery_information['healthy']+=1

        elif SoH >=62 and SoH<=80:
           battery_information['exchange']+=1

        else:
           battery_information['failed']+=1    

#return battery number information
    return battery_information


def test_bucketing_by_health():
  
  print("Counting batteries by SoH...\n")
#additional test cases
  present_capacities = [113, 116, 80, 95, 92, 70, 0, 74.4, 96, 20, 120]
  
  counts = count_batteries_by_health(present_capacities)

#addition of border test cases
# healthy - 120, 
# failed - 0, 
# exchange - 96, 74.4, 20
#border test cases are - 120, 0, 74.4(62%) and 96(80%)

  assert(counts["healthy"] == 3)
  assert(counts["exchange"] == 5)
  assert(counts["failed"] == 3)

  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
