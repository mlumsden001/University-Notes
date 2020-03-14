bucket_capacity = 5.0
bucket_filled = 0.0
sand_handful = 0.2

while bucket_filled < bucket_capacity :
    bucket_filled = bucket_filled + sand_handful
    print("Bucket filled = " + str(bucket_filled))
