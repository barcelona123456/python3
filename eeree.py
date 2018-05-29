def baesu_sum(start, end, baesu):
    hap=0
    i=start
    while i<=end:
        if i%baesu==0:
            hap=hap+i
        i=i+1
    return hap

print("합계:",baesu_sum(1,10,4))
