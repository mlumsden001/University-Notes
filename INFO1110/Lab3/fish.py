total_fish = 0
bucket_weight = 0

while True:
    if bucket_weight > max_bucket_weight :
        break
    total_fish += 1
    fish_weight = weightfish()
    bucket_weight += weightfish
    #if bucket_weight > max_bucket_weight:
        #break 

print("Total fish caught: " + str(total_fish))
print("Bucket weight: " + str(bucket_weight))
