def calculate_avg_rate(filename):
    with open(filename,'r') as file:
        lines  = file.readlines()
    prof_sums ={}
    prof_counts = {} 
    for line in lines: 
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        part = line.split("|")
        if len(part)>=5: 
            profession  = part[3].strip()
            rate_str = part[4].strip()
            #chck valid num 
            if rate_str.replace(".","").isdigit():
                rate = float(rate_str)
                if profession in prof_sums:
                    prof_sums[profession]+=rate
                    prof_counts[profession]+=1
                else:
                    prof_sums[profession]  = rate
                    prof_counts[profession] = 1 
    for profession in sorted(prof_sums.keys()):
        avg_rate = prof_sums[profession] / prof_counts[profession]
        print(f"{profession}: {avg_rate:.2f}")

if __name__ == "__main__":
    calculate_avg_rate("lab2-data.txt")